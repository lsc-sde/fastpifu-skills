---
name: fastpifu-cardiology
description: >
  Assess cardiology outpatients for follow-up disposition using NHS England PIFU guidelines
  and the local SOP. Reasons internally using four classifications — ELIGIBLE, NOT_ELIGIBLE,
  BORDERLINE (with % confidence), DISCHARGE (to GP — no further specialist input) — then
  reports using the FastPIFU-suite verdict vocabulary: PIFU, RETAIN_FOLLOW_UP (including a
  distinct RETAIN_FOLLOW_UP — BORDERLINE flag for grey-zone cases), INSUFFICIENT_DATA, or
  DISCHARGE. Discharge candidates are identified first — this is the primary goal per GIRFT
  guidance.

  Use when reviewing any cardiology clinic letter, discharge summary, or outpatient note to
  decide what happens next with the patient's specialist follow-up. Trigger phrases: "screen
  this letter for PIFU", "is this patient for PIFU or discharge?", "assess follow-up
  disposition", "PIFU eligibility". Handles: arrhythmia (AF all subtypes, SVT, flutter, VT,
  ectopy, post-ablation, CRM devices), valve disease (AS, AR, MR, MS, MVP, BAV,
  post-TAVI/TEER/repair), heart failure (HFrEF/HFpEF/HFmrEF), POTS, stable angina, post-MI,
  cardiomyopathy. Fully self-contained — no internet required.
---

## Overview

This skill answers one question: *what should happen next with this patient's specialist
follow-up?* There are three possible answers, and getting the distinction right matters:

- ✅ **For PIFU** — the specialist relationship continues, but the patient contacts the
  service when something changes rather than being booked in routinely. The clinician is
  still responsible; the trigger mechanism shifts to the patient.
- ❌ **Not for PIFU** — the specialist relationship continues, but follow-up must be
  *timed and scheduled* by the clinician. The patient is not stable or informed enough to
  self-initiate safely (e.g. NYHA III, recent admission, medication being uptitrated,
  pending investigations).
- 🔄 **Discharge** — no ongoing specialist follow-up is needed at all. The patient is
  handed back to GP entirely. The cardiologist's episode of care is complete. Common
  examples: asymptomatic PAF with no structural disease; persistent AF rate-controlled
  with good LV function; mild stable valve disease explicitly discharged to GP.

**The first clinical question is always: can this patient be discharged?** (GIRFT guidance)
Identifying discharge candidates is more important than identifying PIFU candidates — it
creates clinic capacity and reduces waiting lists. Only if discharge is not appropriate does
the PIFU vs timed follow-up question apply. A discharge case should never be recorded as
PIFU-eligible — if a letter appears clinically clean but describes the clinician handing
the patient back to GP with no ongoing specialist role, classify as 🔄 Discharge.

**ELIGIBLE vs Borderline vs Not for PIFU — the three-way distinction:**

The pattern across all NHS-pathway conditions is:
*stable + optimised + informed + low-risk → ELIGIBLE. Active + changing + complex + monitored → NOT_ELIGIBLE. One grey factor alongside an otherwise strong case → BORDERLINE.*

- **ELIGIBLE**: All inclusion criteria clearly met, no exclusion flags, stability documented. Do not downgrade to BORDERLINE when nothing in the letter creates genuine uncertainty — manufactured uncertainty is as wrong as missed uncertainty.
- **BORDERLINE**: Exclusion flag present alongside meaningful mitigating factors (e.g. recent admission but clearly restabilised); or a single clinical value is genuinely ambiguous; or the clinician expresses doubt in the letter. BORDERLINE requires a specific, named reason grounded in the letter's content.
- **NOT_ELIGIBLE**: An exclusion criterion is **clearly and positively met** — not merely possible, not merely undocumented, not merely unclear. Reserve NOT_ELIGIBLE for cases where an exclusion trigger is unambiguous. Absence of evidence of eligibility is NOT the same as evidence of ineligibility.

**The critical test before writing NOT_ELIGIBLE:** Can you name a specific, clearly-met exclusion criterion? If not — if the uncertainty is due to missing data, hedging language, or an undetermined clinical plan — the verdict is BORDERLINE, not NOT_ELIGIBLE.

**Scenarios that are always BORDERLINE, never NOT_ELIGIBLE unless an independent hard exclusion is also clearly met:**
- Patient age not stated in the letter (assume adult; flag as data gap; → BORDERLINE)
- Clinical stability described as variable, uncertain, or "on good and bad days" without clear NYHA III–IV documentation
- Follow-up plan deferred or undetermined — clinician has not committed to either PIFU or timed follow-up
- Medication optimisation status unclear — not clearly subtherapeutic, not clearly at target, or only partially documented
- Condition severity or LV status unclear due to technical limitations or absence of serial data
- Medications recently initiated but letter documents symptoms are now fully resolved on treatment

Having an exclusion flag does not automatically mean NOT_ELIGIBLE. If exclusion criteria are present alongside significant mitigating factors or clinical ambiguity, it may still be BORDERLINE. When genuinely uncertain between NOT_ELIGIBLE and BORDERLINE, prefer BORDERLINE — unnecessary timed follow-up is also a clinical problem per GIRFT.

The key signal for discharge: *does the clinician intend any ongoing specialist relationship?*
If the letter ends with "no further follow-up required", "discharged to your care", or "no
further specialist input needed" → 🔄 Discharge, regardless of how clinically stable the
patient appears.

**NHS-pathway conditions** (dedicated eligibility criteria — Steps 1 + 2d):
Arrhythmia, heart valve disease, heart failure. Cardiomyopathy (ischaemic, non-ischaemic)
and inherited channelopathy are covered under the arrhythmia source and have a specific
rule in Step 2d/`condition-rules.md` — they are NOT general non-pathway conditions and
should not be run through the Step 2b six-criteria test; the NHS source places them in
ongoing specialist/shared-care follow-up as a matter of course, not PIFU.

**GIRFT-informed condition** (operational pathway guidance, not a full NHS PIFU eligibility
document — Step 2d): Chest pain / stable angina / post-MI. The GIRFT Outpatient Operational
Guide has an explicit chest-pain pathway (nurse-led PIFU/SPoA, 6–12 months, post-PCI
assessed virtually) — do not treat this condition as if no guidance exists. Apply the
chest-pain rules in `condition-rules.md` alongside the universal SOP criteria (Step 2a);
do not apply the elevated "all six criteria must be clearly met" bar reserved for true
non-pathway conditions below.

**Non-pathway conditions** (no NHS or GIRFT guidance at all — general SOP criteria only,
Step 2b, higher threshold): POTS, and any other cardiology condition not covered by NHS
England PIFU specialty guidance or the GIRFT operational guide. Always disclose this
explicitly in the output.

---

## Workflow

### STEP 1 — Load NHS Reference Files

Read the following local reference files. All content is pre-extracted from NHS England and
GIRFT sources (re-verified against the live sources 2 July 2026). No internet access is
required or used.

**What PIFU is (general NHS guidance):**
`references/nhs-pifu-what-is-pifu-extracted-2026-07-02.md`

**Arrhythmia PIFU guidelines (AF, SVT, flutter, VT, ectopy, ablation, devices):**
`references/nhs-pifu-arrhythmia-extracted-2026-07-02.md`

**Valve disease PIFU guidelines (AS, AR, MR, MS, MVP, BAV, post-TAVI/TEER/repair):**
`references/nhs-pifu-valve-disease-extracted-2026-07-02.md`

**Heart failure PIFU guidelines (HFrEF, HFpEF, HFmrEF):**
`references/nhs-pifu-heart-failure-extracted-2026-07-02.md`

**GIRFT Outpatient Operational Guide (AF, aortic stenosis, chest pain, LBBB, heart failure):**
`references/girft-outpatient-cardiology-extracted-2026-07-02.md`

**Fallback:** If any of the above .md files cannot be read, use `references/nhs-pifu-criteria-summary.md`.

From each file, extract and internally note:
- Which patients ARE eligible (inclusion criteria)
- Which patients are NOT eligible (exclusion criteria / red flags)
- Any monitoring requirements or caveats specific to that condition

Note: Files were last re-verified against live NHS/GIRFT sources on 2 July 2026. If more than
12 months have passed, consider re-extracting from the original NHS England sources.

---

### STEP 2 — Learn the Local SOP

Read `references/prn02169-ii-patient-initiated-follow-up-standard-operating-procedure-template.md`

**2a. Universal SOP conditions (apply to ALL patients regardless of condition):**

Patient IS likely suitable if:
- Low risk of urgent follow-up and satisfies specialty criteria
- Understands and accepts responsibility for self-initiated care
- Sufficient health literacy and patient activation (confidence, knowledge, skills)
- Knows their "traffic light" symptoms — which changes should prompt re-contact
- Has the tools to monitor their condition (devices, apps, leaflets, weight scales)
- Can contact the service easily

Requires CAREFUL CONSIDERATION (not automatic exclusion) if:
- 3+ significant comorbidities with uncertain interactions
- Medicines requiring regular secondary care monitoring
- Difficulty contacting the service
- Low health literacy or patient activation
- Clinical requirement for timed follow-ups
- Safeguarding concerns
- Frailty — flag as a data gap if no formal score; do not exclude automatically, but
  reduce certainty

**Absolute exclusions (apply universally):**
- Active decompensation or acute illness
- End-of-life or palliative care pathway
- Pending investigations or procedures that will directly determine whether to intervene,
  initiate device therapy, or significantly change the treatment plan. Routine surveillance
  imaging to better characterise known stable disease (e.g. scheduled echo, characterisation
  MRI for known moderate AR or BAV) does NOT constitute an "outstanding investigation" under
  this criterion — it is a BORDERLINE trigger that reduces certainty but does not mandate
  NOT_ELIGIBLE
- Patient unable or unwilling to take responsibility for self-initiated care — NHS-sourced
  examples of "unable": rapidly progressing dementia, severe memory loss, severe learning
  disability. A willing and capable carer taking on this responsibility (or administrative
  support from a care home/GP surgery for booking specifically) mitigates this exclusion —
  do not treat cognitive impairment as an automatic bar to PIFU if a carer/support route is
  clearly documented in the letter; if no carer/support route is documented, treat as
  NOT_ELIGIBLE, not BORDERLINE.
- Recently initiated medication requiring active secondary care monitoring
  (e.g. new antiarrhythmic, new ARNI, new diuretic titration)

**2b. General SOP criteria for true non-pathway conditions (POTS, and any other condition
with no NHS or GIRFT guidance at all — NOT angina/post-MI/chest pain, which use the
GIRFT-informed Step 2d rules instead, and NOT cardiomyopathy/channelopathy, which use the
NHS-pathway Step 2d rules instead):**

When no dedicated NHS PIFU pathway exists, ALL six must be met:
1. Clinically stable — no active decompensation, acute symptoms, or pending intervention
2. Diagnosis established — no outstanding investigations that would change management
3. Treatment optimised — not in active titration or initiation phase
4. No secondary care drug monitoring requirement (no warfarin INR, no antiarrhythmic
   monitoring, no frequent U&Es for recently changed nephrotoxic drugs)
5. Patient activation confirmed — documented evidence they understand their condition,
   know red flag symptoms, and feel confident to self-manage
6. No device safety concern requiring timed follow-up (ICD with recent therapies,
   pacemaker without remote monitoring, CRT requiring optimisation)

If ALL six met → PIFU under general SOP. If ANY one fails → Not for PIFU; state which.
For non-pathway conditions, all six must be *clearly* met — apply a higher threshold and
disclose in the output that no NHS condition-specific pathway exists. See Reasoning
Transparency for full rationale.

---

### STEP 2c — POTS-Specific Guidance

There is NO dedicated NHS England PIFU pathway for POTS. Always include this statement:
> "No dedicated NHS England PIFU pathway exists for POTS. This assessment applies
> general NHS PIFU SOP eligibility criteria."

Read `references/pots-guidance.md` for full POTS-specific factors for and against PIFU.
Key factors: confirmed diagnosis (tilt table / NASA lean test, HR increment ≥30bpm),
symptoms stabilised, conservative measures in place, no syncopal episodes past 3 months,
patient actively self-monitoring. PIFU timescale: 12 months. Patient should be given
written information on POTS symptom triggers and a clear re-contact pathway.

---

### STEP 2d — Condition-Specific Decision Rules

Read `references/condition-rules.md` now for the full subtype rule tables — discharge-to-GP
scenarios, heart failure (HFpEF/HFrEF/HFmrEF), arrhythmia by subtype (PAF, permanent AF,
persistent AF, SVT, VT, pre-excitation, ventricular ectopy, atrial flutter), heart valve
disease by subtype (AS, AR, MR, MS, MVP, BAV, post-valve intervention), chest pain / stable
angina / post-MI (GIRFT pathway), and the universal exclusion lists for arrhythmia and valve
disease. Apply these rules during Step 3 alongside the general SOP criteria from Step 2a.

`condition-rules.md` is the single source of truth for this content — read it fresh each
time rather than relying on memory, since it may be updated independently of this file.

---

### STEP 3 — Screen the Clinical Document

**Accepted formats:** PDF, Word (.docx), plain text, or pasted text. Read all documents
provided before reaching a verdict. If no document is provided, ask for it.

Identify:
1. **Sub-specialty and subtype** — which arrhythmia / which valve and lesion / which HF
   subtype / POTS / other? If NOT a cardiology document, state clearly and stop.
2. **Diagnosis and clinical status** — primary condition, severity, stability
3. **Current management** — medications (doses, how recently initiated), devices
   (pacemaker/ICD/CRT — remote monitoring in place?), planned procedures
4. **Red flags** — features that exclude PIFU per Step 2d subtype rules
5. **Enabling factors** — features supporting PIFU eligibility
6. **Patient activation** — documented concerns about self-management; traffic light plan
7. **Data gaps** — flag and reduce certainty % if any of these are missing:

| Value | Why it matters | Flag if missing for... |
|---|---|---|
| NYHA class | Determines HF eligibility threshold | All heart failure |
| LVEF (quantified %) | Borderline 40–50% range affects classification | HF, valve, post-intervention |
| Serial echo data | Rate of progression matters as much as current severity | AS, AR, MR, BAV |
| Anticoagulation stability | Unstable INR excludes mechanical valve patients | AF, mechanical prosthesis |
| eGFR trend | Post-ARNI drop may exclude even stable-looking HF | HFrEF/HFmrEF on ARNI |
| Frailty assessment | Unscored frailty reduces certainty, not automatic exclusion | Any letter mentioning frailty |
| Patient age | Must be ≥18 | Any letter where age not stated → assume adult, classify as BORDERLINE (do NOT use absence of stated age as a basis for NOT_ELIGIBLE) |
| Remote monitoring status | ICD/pacemaker without remote = hard exclusion | All device patients |
| Date of last admission | Recent admission = instability signal; single recent admission with positive trajectory = BORDERLINE; multiple or ongoing = NOT_ELIGIBLE | All heart failure |
| Antiarrhythmic drug class | Class I/III = exclusion regardless of apparent stability | All arrhythmia on medication |
| Syncopal frequency | ≥1/month syncope = POTS exclusion | POTS cases |

Apply: NHS-pathway criteria (Steps 1 + 2d) for arrhythmia / valve / HF / cardiomyopathy /
channelopathy; GIRFT-informed Step 2d rules + universal SOP (Step 2a) for chest pain /
stable angina / post-MI; general SOP + POTS criteria (Steps 2b + 2c) for POTS; general SOP
only (Step 2b), with the elevated six-criteria bar, for any other condition with no NHS or
GIRFT guidance at all.

**Common traps:**
- Biochemistry contradicts clinical stability (falling eGFR post-ARNI, rising LFTs on
  amiodarone, hyperkalaemia on MRA) — check labs, not just symptoms
- Echo looks stable but *rate of change* between serial studies is the red flag (AS: Vmax ≥0.3 m/s/year)
- Primary condition suitable but co-medication requires secondary care monitoring (e.g. warfarin
  in prosthetic valve patient with variable INR)
- Patient is functionally NYHA II but has documented non-compliance with self-monitoring
  or diuretic non-compliance causing recurrent fluid overload → not suitable for PIFU
- Subtherapeutic dose with no documented reason = not optimised, even if "no further titration planned"
- "Will reassess after uptitration" → Not for PIFU until that reassessment occurs
- Clinician expresses reservations in the letter → flag borderline, do not override

---

### STEP 3b — External Verdict Word (FastPIFU suite interoperability)

The internal classification used throughout this file (ELIGIBLE / NOT_ELIGIBLE / BORDERLINE /
DISCHARGE) is what drives all reasoning above and what the eval harness scores against — it does
not change. Before writing the Structured Output in Step 4, translate the internal classification
to the external verdict word shared across the FastPIFU specialty suite, using this mapping:

| Internal classification | External verdict word |
|---|---|
| ELIGIBLE | `PIFU` |
| NOT_ELIGIBLE | `RETAIN_FOLLOW_UP` |
| DISCHARGE | `DISCHARGE` |
| BORDERLINE, confidence ≥70% | `RETAIN_FOLLOW_UP — BORDERLINE` |
| BORDERLINE, confidence <70% | `INSUFFICIENT_DATA` |

The word BORDERLINE must always appear literally in the output when applicable — it is never
collapsed into a bare `RETAIN_FOLLOW_UP` with only a percentage to distinguish it. A borderline
case and a clearly-excluded case must never read identically; the percentage alone is not a
reliable enough signal for a clinician scanning a list of results. `INSUFFICIENT_DATA` is reserved
for the existing <70%-confidence band (see calibration table above) — this is not a new category
of judgement, just the existing "insufficient information" band given its own verdict word.

---

### STEP 4 — Structured Output

```
PATIENT: [Name, DOB, NHS Number if available]
CONDITION: [Sub-specialty, subtype, primary diagnosis]
DOCUMENT TYPE: [Clinic letter / Discharge summary / MDT note / Other]
PATHWAY TYPE: [NHS-defined pathway / General SOP criteria / POTS — no dedicated pathway]

DATA GAPS (if any):
  - [e.g. LVEF not quantified; NYHA class not stated; frailty not formally scored]

PIFU ELIGIBILITY FACTORS:
  For PIFU:
    - [supporting factors]
  Against PIFU:
    - [excluding or cautionary factors]

APPLICABLE CRITERIA SOURCE:
  - [e.g. NHS Arrhythmia PIFU Guidelines + General SOP; or "General NHS PIFU SOP —
    no condition-specific pathway exists for [condition]"]

VERDICT: [PIFU / RETAIN_FOLLOW_UP / RETAIN_FOLLOW_UP — BORDERLINE / INSUFFICIENT_DATA / DISCHARGE]
  ([X]% confidence)
  (Internal classification: ELIGIBLE / NOT_ELIGIBLE / BORDERLINE / DISCHARGE — see Step 3b mapping)

REASONING:
  [2–4 sentences citing specific criteria. For non-pathway conditions, state that no
  dedicated NHS guideline exists. For borderline cases, name the specific factor(s)
  driving uncertainty.]

SUGGESTED PIFU TIMESCALE (if PIFU):
  [Condition-specific — do NOT default to a flat "6-12 months" for every verdict. See the
  "PIFU Timescales by Condition" table at the top of references/condition-rules.md. Most
  GIRFT-general and HF/valve continuous pathways are 6-12 months, but arrhythmia has
  specific longer time-limited pathways (2 years for post-ablation persistent AF/VT,
  3 years for medically-managed VT) and POTS is 12 months — cite the specific figure for
  the condition in hand, not a generic default.]
```

---

## Reasoning Transparency

### How eligibility decisions are made

The skill uses a two-layer decision process:

**Layer 1 — Condition-specific NHS criteria (Steps 1 & 2d)**
For arrhythmia, valve disease, and heart failure, NHS England has published explicit
eligibility criteria. The skill reads these and maps the patient's clinical status against
subtype-specific rules (Step 2d). If the patient clearly meets inclusion criteria and has
no exclusion criteria → binary verdict, high confidence.

The pattern is the same across all three NHS-pathway conditions:
*Stable + optimised + informed + low-risk = ELIGIBLE. Active + changing + complex + monitored = NOT_ELIGIBLE. One grey factor in an otherwise strong case = BORDERLINE.*

**Example (HF — HFrEF/HFmrEF):** NYHA I–II, GDMT drug classes optimised, clinically
stable, stable renal function, documented self-monitoring plan → ELIGIBLE. Multiple recent
admissions, NYHA III, active titration just started, declining eGFR, or pending device
therapy → NOT_ELIGIBLE. Single recent admission but patient now restabilising; or one
medication class sub-target but otherwise stable → BORDERLINE.

**Layer 2 — Universal SOP criteria (Step 2a)**
Applied to every patient regardless of condition. Even if the primary condition is
suitable, the patient must also pass:
1. No active decompensation or pending intervention
2. Diagnosis established — no outstanding investigations that would change management
3. Treatment optimised — not in active titration; medications at therapeutic doses
4. No secondary care drug monitoring requirement
5. Demonstrated patient activation (understands condition, knows red flags, has a plan)
6. No device safety concern requiring timed follow-up

Failing any single criterion excludes PIFU even if the primary condition qualifies.

**What to do when no guideline exists at all (POTS, and any other condition not covered by
NHS PIFU specialty guidance or the GIRFT operational guide):**
1. Explicitly state that no condition-specific pathway exists — always disclosed in output.
2. Fall back entirely to the six general SOP criteria above.
3. Apply a higher threshold — all six must be clearly met, not mostly met, because the
   absence of a validated pathway means more uncertainty.
4. Err toward ❌ Not for PIFU in genuinely ambiguous cases — a false negative (continued
   timed follow-up) is a safe default; a false positive (unsuitable patient on PIFU) risks
   delayed recognition of deterioration.

**Note — chest pain / stable angina / post-MI and cardiomyopathy/channelopathy are NOT
in this "no guideline exists" bucket.** Chest pain/angina/post-MI has explicit GIRFT
operational guidance (Step 2d) — apply it directly, without the elevated six-criteria bar.
Cardiomyopathy/channelopathy is covered by the NHS arrhythmia source (Step 2d) with its
own specific — and generally stricter, not more lenient — rule (ongoing specialist/shared
care follow-up as a matter of course). Only route a condition through this elevated-bar
general-SOP fallback when Step 1/2d genuinely has nothing to say about it.

---

### How the % certainty score is calibrated

| Dimension | Raises confidence | Lowers confidence |
|-----------|------------------|------------------|
| **Guideline fit** | Clearly meets NHS inclusion criteria | Sits on the borderline of a criterion |
| **Exclusion flags** | Zero red flags | One or more amber flags present |
| **Information completeness** | All key data points present | Key clinical values missing |
| **Pathway type** | NHS-defined condition-specific pathway | General SOP only — more interpretive |

- **>95%** — criteria unambiguously met or failed; no meaningful clinical disagreement expected
- **85–95%** — strong case, one minor uncertainty that wouldn't change the overall picture
- **70–85%** — genuine grey zone; a senior clinician might reasonably reach a different verdict
- **<70%** — insufficient information; output will list what additional data would resolve it

**Common borderline scenarios:** medication titration incomplete; recent admission >6 months
without confirmed restabilisation; LVEF 40–50% without clear stability trajectory; valve
severity described qualitatively only; frailty unscored; clinician expresses reservations;
3+ comorbidities with uncertain interactions; follow-up plan deferred.

---

### Guidance for supervisors

- **New condition with NHS guidance:** add a dated .md extract to `references/`, add Read in
  Step 1, add criteria to `nhs-pifu-criteria-summary.md`, add subtype rules to
  `condition-rules.md`.
- **Adjust POTS criteria:** edit `references/pots-guidance.md`.
- **Adjust SOP criteria:** edit Step 2b (numbered — change individually; update hard/soft language).
- **Adjust subtype rules:** edit Step 2d or `references/condition-rules.md`.
- **Adjust confidence thresholds:** edit the calibration table above.

---

## Hard Rules

- Never give a PIFU verdict for a non-cardiology patient. State the specialty mismatch.
- Always cite the criteria source. For non-pathway conditions, always state the absence of
  a dedicated guideline — never imply one exists.
- POTS must always include the "no dedicated NHS PIFU pathway" statement.
- If the document says the patient is already on a PIFU pathway, confirm existing status
  rather than re-assessing from scratch.
- If key clinical information is missing (EF, valve gradient, NYHA class, POTS HR increment,
  syncopal frequency, frailty score), flag as a data gap and reduce certainty %. Do not fabricate values.
- **Data gaps produce BORDERLINE, not NOT_ELIGIBLE.** Missing data means uncertainty, not
  exclusion. NOT_ELIGIBLE requires a POSITIVE, clearly-met exclusion criterion — not merely
  the absence of evidence of eligibility. This applies to: age not stated, stability
  undocumented, medication optimisation unclear, follow-up plan undetermined, LV status
  unknown. Absent information is not the same as information of absence.
- End-of-life / palliative care is an absolute hard exclusion — never recommend PIFU.
- Strong exclusion flags — these typically preclude PIFU but indicate BORDERLINE (not
  NOT_ELIGIBLE) when clear mitigating factors are present: active decompensation; recent
  hospitalisation (HF instability signal, arrhythmia post-cardioversion <3 months);
  pending investigations that will directly determine intervention or device therapy (not
  routine surveillance imaging); newly initiated medications requiring active secondary care
  monitoring; ICD with recent therapies without remote monitoring. When ONE such flag is
  present alongside a clearly positive trajectory, prefer BORDERLINE. NOT_ELIGIBLE is
  reserved for flags that are unambiguous and unmitigated.
- 🔄 Discharge is NOT the same as PIFU. If the letter describes GP discharge, record as
  Discharge — not a PIFU verdict. Discharge-to-GP maps to NOT_ELIGIBLE in structured output.
- Both error directions are clinically harmful: a false negative (missed PIFU candidate)
  means unnecessary timed follow-up, wasting clinic capacity and denying access to new
  patients — the exact problem GIRFT and PIFU exist to solve. A false positive (unsuitable
  patient on PIFU) risks delayed detection of deterioration. For NHS-pathway conditions
  (arrhythmia, valve disease, HF, cardiomyopathy/channelopathy) and the GIRFT-informed
  chest pain/angina/post-MI pathway, apply condition-specific criteria directly without
  adding a conservative bias. For true non-pathway conditions (POTS, and anything else
  with no NHS or GIRFT guidance at all), where no validated guideline exists, apply a
  higher threshold and err toward NOT_ELIGIBLE.
- An exclusion flag alone does not mandate NOT_ELIGIBLE. If exclusion criteria are present
  alongside meaningful mitigating factors or clinical ambiguity, classify as ⚠️ BORDERLINE.
  Reserve NOT_ELIGIBLE for cases where the exclusion is unambiguous and leaves no doubt.
- If uncertain between NOT_ELIGIBLE and BORDERLINE, prefer BORDERLINE — it prompts
  clinician review rather than defaulting to unnecessary timed follow-up.
- Do not call BORDERLINE when no exclusion flags are present and clinical stability is
  clearly documented. ELIGIBLE means the criteria are met — do not manufacture uncertainty
  that isn't grounded in the letter's content.
- Never interpret subtherapeutic medication doses as "optimised". Optimisation means at or
  approaching guideline-directed target doses, or a documented clinical reason for a lower dose
  (e.g. bradycardia limiting beta-blocker uptitration).
- If the clinician's own letter expresses doubt about PIFU suitability, do not override with
  ELIGIBLE — flag as borderline and note the concern.
