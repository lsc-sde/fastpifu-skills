---
name: fastpifu-cardiology
description: >
  Cardiology-specific delta for the FastPIFU suite: condition routing, cardiology's three-tier
  pathway classification, data-gap cautions, and cardiology-specific hard rules. Apply under
  `alternate-orchestrator-prompt.md`, which supplies the universal PIFU reasoning (four
  dispositions, the BORDERLINE safety rule, the SOP checklist, output format, confidence
  calibration, universal hard rules) shared across every FastPIFU specialty. Use when deciding
  what should happen next with a cardiology patient's follow-up — whether they can move to
  patient-initiated follow-up, be discharged, or stay in timed follow-up. Trigger phrases:
  "screen this letter for PIFU", "is this patient for PIFU or discharge?", "assess follow-up
  disposition", "PIFU eligibility". Covers arrhythmia (AF all subtypes, SVT, flutter, VT,
  ectopy, post-ablation, CRM devices), valve disease (AS, AR, MR, MS, MVP, BAV,
  post-TAVI/TEER/repair), heart failure (HFrEF/HFpEF/HFmrEF), chest pain/stable angina/post-MI,
  cardiomyopathy/channelopathy, and POTS. Fully self-contained references — no internet
  required.
---

# FastPIFU — Cardiology

Cardiology PIFU assessment. Routing, cautions, and hard rules specific to cardiology; apply under
`alternate-orchestrator-prompt.md`'s universal operating instructions (the four dispositions,
the BORDERLINE-vs-RETAIN_FOLLOW_UP safety rule, the universal SOP checklist, output format,
confidence calibration, and universal hard rules all live there — read that file first).

## Condition routing

| Condition / material | Reference file |
|---|---|
| General PIFU background (what PIFU is, NHS-wide) | `references/nhs-pifu-what-is-pifu-extracted-2026-07-02.md` |
| Local SOP template (see alternate-orchestrator-prompt.md's Universal SOP Checklist) | `references/prn02169-ii-patient-initiated-follow-up-standard-operating-procedure-template.md` |
| Arrhythmia — AF, flutter, SVT, VT, ectopy, pre-excitation, devices | `references/nhs-pifu-arrhythmia-extracted-2026-07-02.md` |
| Heart valve disease — AS, AR, MR, MS, MVP, BAV, prosthetic | `references/nhs-pifu-valve-disease-extracted-2026-07-02.md` |
| Heart failure — HFrEF, HFmrEF, HFpEF | `references/nhs-pifu-heart-failure-extracted-2026-07-02.md` |
| GIRFT Outpatient Operational Guide (AF, aortic stenosis, chest pain, LBBB, heart failure) | `references/girft-outpatient-cardiology-extracted-2026-07-02.md` |
| POTS — no dedicated NHS pathway (see below) | `references/pots-guidance.md` |
| All subtype decision rules (discharge-to-GP table, arrhythmia/valve/HF subtypes, chest pain/angina/post-MI, PIFU timescales by condition) | `references/condition-rules.md` — single source of truth; read fresh each time, not from memory |
| Fallback if any NHS/GIRFT extract above cannot be read | `references/nhs-pifu-criteria-summary.md` |

All reference files were re-verified against live NHS/GIRFT sources on 2 July 2026. If more than
12 months have passed, consider re-extracting from the original sources.

`condition-rules.md` is read alongside whichever NHS/GIRFT extract applies — the extract gives
the source guidance, `condition-rules.md` gives the operationalised subtype-by-subtype rule.

From each NHS/GIRFT extract, extract and internally note: which patients ARE eligible (inclusion
criteria), which patients are NOT eligible (exclusion criteria / red flags), and any monitoring
requirements or caveats specific to that condition.

**Eval-scoring note:** the current 150-case eval dataset (`evals/eval_sample_150_v3.json`) has
only three ground-truth classes — ELIGIBLE, NOT_ELIGIBLE, BORDERLINE — with no separate DISCHARGE
class. For scoring against that dataset only, DISCHARGE cases are treated as NOT_ELIGIBLE. This
does not change the actual clinical verdict shown in the Structured Output, which reports
DISCHARGE as its own distinct outcome per the alternate orchestrator's verdict mapping.

## Cardiology's three-tier pathway classification

Cardiology conditions split into three tiers, each with a different criteria bar. Determine the
tier before applying any eligibility logic:

**NHS-pathway conditions** (dedicated NHS eligibility criteria): arrhythmia, heart valve disease,
heart failure. Cardiomyopathy (ischaemic, non-ischaemic) and inherited channelopathy are covered
under the arrhythmia source and have a specific rule in `condition-rules.md` — they are NOT
general non-pathway conditions and should not be run through the six-criteria non-pathway test;
the NHS source places them in ongoing specialist/shared-care follow-up as a matter of course, not
PIFU.

**GIRFT-informed condition** (operational pathway guidance, not a full NHS PIFU eligibility
document): chest pain / stable angina / post-MI. The GIRFT Outpatient Operational Guide has an
explicit chest-pain pathway (nurse-led PIFU/SPoA, 6-12 months, post-PCI assessed virtually) — do
not treat this condition as if no guidance exists. Apply the chest-pain rules in
`condition-rules.md` alongside the alternate orchestrator's universal SOP checklist; do not apply
the elevated non-pathway six-criteria bar to this condition.

**Non-pathway conditions** (no NHS or GIRFT guidance at all — general SOP criteria only, higher
threshold per the orchestrator's non-pathway fallback): POTS, and any other cardiology condition
not covered by NHS England PIFU specialty guidance or the GIRFT operational guide. Always
disclose this explicitly in the output. For cardiology, the sixth non-pathway criterion (no
safety-monitoring concern requiring timed follow-up) concretely means: no device safety concern
requiring timed follow-up (ICD with recent therapies, pacemaker without remote monitoring, CRT
requiring optimisation).

## POTS disclosure requirement

There is NO dedicated NHS England PIFU pathway for POTS. Always include this statement in the
output:
> "No dedicated NHS England PIFU pathway exists for POTS. This assessment applies general NHS
> PIFU SOP eligibility criteria."

Read `references/pots-guidance.md` for full POTS-specific factors for and against PIFU. Key
factors: confirmed diagnosis (tilt table / NASA lean test, HR increment ≥30bpm), symptoms
stabilised, conservative measures in place, no syncopal episodes past 3 months, patient actively
self-monitoring. PIFU timescale: 12 months. Patient should be given written information on POTS
symptom triggers and a clear re-contact pathway.

## Specialty-specific cautions (data-gap traps)

Flag and reduce certainty if any of these are missing — per the orchestrator's core safety rule,
a gap here means BORDERLINE, not RETAIN_FOLLOW_UP:

| Value | Why it matters | Flag if missing for... |
|---|---|---|
| NYHA class | Determines HF eligibility threshold | All heart failure |
| LVEF (quantified %) | Borderline 40-50% range affects classification | HF, valve, post-intervention |
| Serial echo data | Rate of progression matters as much as current severity | AS, AR, MR, BAV |
| Anticoagulation stability | Unstable INR excludes mechanical valve patients | AF, mechanical prosthesis |
| eGFR trend | Post-ARNI drop may exclude even stable-looking HF | HFrEF/HFmrEF on ARNI |
| Frailty assessment | Unscored frailty reduces certainty, not automatic exclusion | Any letter mentioning frailty |
| Patient age | Must be ≥18 | Any letter where age not stated → assume adult, classify as BORDERLINE (do NOT use absence of stated age as a basis for RETAIN_FOLLOW_UP) |
| Remote monitoring status | ICD/pacemaker without remote = hard exclusion | All device patients |
| Date of last admission | Recent admission = instability signal; single recent admission with positive trajectory = BORDERLINE; multiple or ongoing = RETAIN_FOLLOW_UP | All heart failure |
| Antiarrhythmic drug class | Class I/III = exclusion regardless of apparent stability | All arrhythmia on medication |
| Syncopal frequency | ≥1/month syncope = POTS exclusion | POTS cases |

**Common traps:**
- Biochemistry contradicts clinical stability (falling eGFR post-ARNI, rising LFTs on
  amiodarone, hyperkalaemia on MRA) — check labs, not just symptoms
- Echo looks stable but *rate of change* between serial studies is the red flag (AS: Vmax
  ≥0.3 m/s/year)
- Primary condition suitable but co-medication requires secondary care monitoring (e.g.
  warfarin in prosthetic valve patient with variable INR)
- Patient is functionally NYHA II but has documented non-compliance with self-monitoring or
  diuretic non-compliance causing recurrent fluid overload → not suitable for PIFU
- Subtherapeutic dose with no documented reason = not optimised, even if "no further titration
  planned"
- "Will reassess after uptitration" → RETAIN_FOLLOW_UP until that reassessment occurs
- Clinician expresses reservations in the letter → flag BORDERLINE, do not override

**Common borderline scenarios (cardiology-specific):** medication titration incomplete; recent
admission >6 months without confirmed restabilisation; LVEF 40-50% without clear stability
trajectory; valve severity described qualitatively only; frailty unscored; clinician expresses
reservations; 3+ comorbidities with uncertain interactions; follow-up plan deferred.

## Specialty-specific hard rules

- Recent hospitalisation <6 months (heart failure) or cardioversion <3 months (arrhythmia)
  excludes PIFU as a strong flag — rationale: high early-deterioration risk regardless of
  current appearance. Per the orchestrator's strong-exclusion-flag framework, this indicates
  BORDERLINE (not RETAIN_FOLLOW_UP) when a clearly positive trajectory is documented, and
  RETAIN_FOLLOW_UP only when unmitigated or recurrent.
- ICD with recent therapies, or any cardiac device without remote monitoring in place, excludes
  PIFU — rationale: requires scheduled device review.
- Newly initiated class I/III antiarrhythmic (amiodarone, flecainide, sotalol) excludes PIFU —
  rationale: active secondary-care monitoring requirement.
- Low/sub-therapeutic GDMT doses are not "optimised" without a documented clinical ceiling
  reason (e.g. bradycardia limiting beta-blocker uptitration).
- HFrEF/HFmrEF worked example: NYHA I-II, GDMT drug classes optimised, clinically stable, stable
  renal function, documented self-monitoring plan → PIFU. Multiple recent admissions, NYHA III,
  active titration just started, declining eGFR, or pending device therapy → RETAIN_FOLLOW_UP.
  Single recent admission but patient now restabilising; or one medication class sub-target but
  otherwise stable → BORDERLINE.
- Chest pain / stable angina / post-MI and cardiomyopathy/channelopathy are NOT in the "no
  guideline exists" non-pathway bucket — see the three-tier classification above. Only route a
  condition through the elevated-bar non-pathway fallback when the routing table and
  `condition-rules.md` genuinely have nothing to say about it.

## Guidance for maintainers

- **New condition with NHS guidance:** add a dated .md extract to `references/`, add it to the
  Condition routing table above, add criteria to `nhs-pifu-criteria-summary.md`, add subtype
  rules to `condition-rules.md`.
- **Adjust POTS criteria:** edit `references/pots-guidance.md`.
- **Adjust subtype rules or PIFU timescales:** edit `references/condition-rules.md`.
- **Adjust universal logic (confidence thresholds, the BORDERLINE safety rule, output format):**
  edit `alternate-orchestrator-prompt.md` instead — changing it there changes it for every
  specialty, not just cardiology.
