# Condition-Specific Decision Rules

<!-- concept_ids: (completed by data team) -->
<!-- author: Karthik | reviewed_by: (pending clinical review) | last_updated: 2026-07-02 -->

These rules are drawn from NHS England PIFU guidelines and GIRFT guidance.
Apply them during Step 3 alongside the general SOP criteria from Step 2a.

---

## PIFU Timescales by Condition (do not default to a flat "6–12 months")

Different sources specify different lengths for the "timed"/"time-limited" PIFU pathways.
Continuous PIFU pathways (heart failure, ongoing arrhythmia review, valve surveillance)
don't have a fixed end date in the same way — they run alongside surveillance imaging or
ongoing MDT access. Cite the specific figure below rather than a generic default.

| Condition / scenario | Timescale | Source |
|---|---|---|
| Persistent AF, post-successful ablation, good LV function | 2 years, time-limited | NHS arrhythmia (verbatim) |
| VT (structurally normal heart), post-successful ablation | 2 years, time-limited | NHS arrhythmia (verbatim) |
| VT (structurally normal heart), medically managed | 3 years, timed PIFU | NHS arrhythmia (verbatim) |
| PAF, symptomatic, managed successfully with ablation | 3–6 month review, then 2 years time-limited | NHS arrhythmia (verbatim) |
| SVT, general GIRFT-style review (no more specific NHS figure given) | 6–12 months | GIRFT general principle |
| Ventricular ectopy — asymptomatic, high burden, normal LV | 1 year, then discharge if no concerns | NHS arrhythmia (verbatim) |
| Ventricular ectopy — post-ablation (previously impaired LV) | 2 years, then discharge if LV recovered | NHS arrhythmia (verbatim) |
| Ventricular ectopy — symptomatic, treated with ablation/beta-blocker/CCB | Time-limited, at physician's discretion (no fixed figure stated) | NHS arrhythmia (verbatim) |
| Other arrhythmias (inappropriate sinus tachycardia, low-burden SVE) | Discharge or PIFU at clinician's discretion (no fixed figure stated) | NHS arrhythmia (verbatim) |
| AF / aortic stenosis / chest pain / LBBB / heart failure — GIRFT nurse-led PIFU/SPoA | 6–12 months | GIRFT (verbatim, "ideally limited to") |
| Chest pain / stable angina / post-MI | 6–12 months | GIRFT (verbatim) |
| Heart failure — continuous PIFU | No fixed end date (continuous access to HF MDT); review per local protocol | NHS heart failure |
| Heart valve disease — surveillance-linked PIFU | Follows the imaging surveillance interval for the specific lesion: AS 1–2yr, BAV 2–5yr (12mo if root >40mm), AR 1–2yr, MR 18mo–2yr, MS 2–3yr, MVP 3–5yr (or MR interval if moderate MR present), TAVI/bioprosthetic/repair/TEER 1–2yr, mechanical valve (no associated aortopathy) — NO imaging follow-up required at all | NHS valve disease (verbatim per subtype) |
| POTS | 12 months, then re-assess for continuation or discharge | Local SOP / pots-guidance.md |
| Pre-excitation managed without EPS, or post-ablation | Long-term, with periodic outpatient review (no fixed end date stated) | NHS arrhythmia (verbatim) |
| Atypical flutter/AT with recurrent arrhythmias, long-term management | Long-term PIFU pathway (no fixed end date stated) | NHS arrhythmia (verbatim) |
| General SOP fallback (no condition-specific figure available) | 6–12 months as a conservative default only when nothing more specific applies | GIRFT general principle |

---

## Discharge-to-GP Scenarios

Check these BEFORE concluding a patient is PIFU-eligible. These scenarios commonly
present as clinically clean (no exclusion flags) but are appropriate for GP discharge,
not PIFU. The key signal is always: does the clinician intend any ongoing specialist
relationship? If the letter ends with "no further follow-up required", "discharged to
your care", or "no further specialist input needed" — that is always 🔄 Discharge.

| Scenario | Correct verdict |
|---|---|
| PAF — first episode, reversible cause identified and treated | 🔄 Discharge |
| PAF — recurrent, referred to EP and accepted for ablation | 🔄 Discharge (EP takes over) |
| PAF — asymptomatic, no structural disease, no antiarrhythmic needed, no ongoing intervention | 🔄 Discharge |
| Permanent AF — rate controlled (HR <110), symptoms controlled, no change in heart function, no structural disease needing follow-up | 🔄 Discharge |
| Persistent AF — cardioverted and improved, no further referral needed | 🔄 Discharge |
| Persistent AF — referred to electrophysiologist, no other follow-up needed | 🔄 Discharge |
| Persistent AF — rate-controlled, good LV function, asymptomatic, no rhythm control planned | 🔄 Discharge |
| PAF or persistent AF treated with AV node ablation + pacemaker, echo done at 3–6 months, handed to pacing clinic (+/- HF clinic) | 🔄 Discharge (from general cardiology — follow-up continues at pacing/HF clinic, not PIFU) |
| PAF or persistent AF on class I/III antiarrhythmic (flecainide, amiodarone, sotalol) | ❌ Not for PIFU (requires long-term follow-up or GP shared care) |
| Typical atrial flutter — symptom-free, sinus rhythm (or stable well-controlled flutter), stable LV function, at 3–6 months | 🔄 Discharge |
| Atypical atrial flutter / atrial tachycardia — successfully treated, after 6 months | 🔄 Discharge or referral back to originating team |
| Post-successful ablation (AF, flutter, SVT, VT) — GIRFT: routine doctor clinic not needed | ✅ PIFU (nurse-led, 6–12 months; NHS arrhythmia source specifies 2 years time-limited for persistent AF/VT post-ablation — see condition-specific timescales) |
| Post-cardioversion — GIRFT: routine doctor clinic not needed, ECG/symptom review required | ✅ PIFU (6–12 months) |
| Post-valve intervention, fully recovered, normally functioning prosthesis, preserved LV, no ongoing specialist need | 🔄 Discharge |
| Aortic stenosis — no intervention needed, asymptomatic, stable | Physiologist-led echo surveillance (not routine doctor PIFU) |
| Mild stable valve disease explicitly handed to GP, no further imaging surveillance planned | 🔄 Discharge |
| Bicuspid aortic valve with no significant haemodynamic lesion, no aortic root concern, explicitly discharged to GP | 🔄 Discharge |
| Valve disease patient (any severity) whom the clinician has deemed unsuitable for valvular intervention due to frailty or multiple co-morbidities, with no valve-specific PIFU/surveillance plan documented | 🔄 Discharge to GP — NHS valve source (verbatim): "Patients deemed by their clinician to be unsuitable for valvular intervention (e.g. frailty, multiple co-morbidities) — these should be discharged back to their GP." This is a distinct disposition from ordinary severe/symptomatic valve disease (which is otherwise ❌ NOT_ELIGIBLE) — a documented clinician decision against intervention on frailty/comorbidity grounds, with no ongoing surveillance plan, maps to Discharge, not timed follow-up. |
| Heart failure — fully investigated, on optimal treatment, stable | ✅ PIFU where appropriate (GIRFT) |
| HFpEF — hospital clinic rarely needed; community HF team managing | 🔄 Discharge or community HF team follow-up |
| Hypertension — specialist episode concluded, management optimised, handed to GP | 🔄 Discharge |
| LBBB — without concerning history/investigations including echo, no structural disease | 🔄 Discharge (no cardiology referral needed per GIRFT) |
| Ischaemic cardiomyopathy, once optimised (medically or with ablation) | 🔄 Discharge from general cardiology to shared care (HF team + device team + GP) — NOT PIFU, regardless of device status |

> **⚠️ Scope note:** The AF/flutter DISCHARGE entries above (PAF, Persistent AF, typical
> flutter) apply exclusively to those specific subtypes. **Atypical atrial flutter and
> atrial tachycardia (AT) are distinct arrhythmias** — a clinician letter stating "discharge
> to GP" for atypical flutter or AT without completed ablation maps to ❌ NOT_ELIGIBLE, not
> 🔄 Discharge, UNLESS the letter specifically documents successful treatment after 6 months
> (see Atrial Flutter subtype rules), in which case Discharge is correct. Do NOT apply the
> AF/typical-flutter DISCHARGE rules to atypical flutter/AT by default.
>
> **⚠️ Cardiomyopathy/channelopathy scope note:** Non-ischaemic cardiomyopathy and inherited
> channelopathy (LQT, Brugada, etc.) are NEVER PIFU or general discharge — the NHS source
> requires long-term follow-up or shared care with the inherited cardiomyopathy/channelopathy
> team regardless of stability. Only ischaemic cardiomyopathy maps to a discharge-to-shared-
> care disposition (row above); non-ischaemic cardiomyopathy/channelopathy map to
> ❌ NOT_ELIGIBLE (ongoing specialist follow-up required, just not from general cardiology
> PIFU). See Cardiomyopathy/Channelopathy subtype rules under Arrhythmia below.

---

## Heart Failure (HFpEF / HFrEF / HFmrEF)

**Source fidelity note:** the NHS HF PIFU document itself is brief on numeric detail — it
states only that patients must be "STABLE" with "MEDICINES OPTIMISED," and lists exclusions
as: outstanding investigations/decisions pending; candidate for device therapy (CRT/ICD)
still awaiting diagnostics or intervention; "UNCONTROLLED SYMPTOMS"; end-of-life pathway. It
gives no eGFR number, no K+ number, no titration-window number, and no drug-class-by-class
GDMT breakdown. The specific numbers below (eGFR<30, K+>5.5, 8–12 week titration window,
the four-drug-class HFrEF breakdown) are supplementary clinical judgement drawn from general
HF management guidance (NICE NG106/ESC), not the NHS PIFU source itself — they are clinically
sound but should not be presented as if literally NHS-PIFU-sourced. NYHA class, admission
history, and self-monitoring/traffic-light criteria ARE consistent with the source's general
framing (stability + optimisation + patient activation).

**Disclosed policy choice (same pattern as valve disease below):** the NHS HF source's
"Patient details" list under "Patients NOT Suitable for PIFU" also names "patients unable
to contact the service in a timely way" and "patients with low levels of knowledge, skills
and confidence to manage their follow-up care and/or no carer support" as hard exclusions.
As with valve disease, Step 2a's Universal SOP treats these same concepts (difficulty
contacting the service; low health literacy/patient activation) as "requires careful
consideration, not automatic exclusion" rather than a hard bar — an intentional, disclosed
choice to avoid the v4 regression pattern, not a missed source detail. The source's ~10%
cognitive-impairment-with-no-carer-support figure (under Health Inequalities) reinforces why
carer/support documentation matters, and is consistent with the dementia/carer exclusion
clarification already in SKILL.md Step 2a.

**For PIFU — all of the following must be present:**
- Clinically stable (NYHA Class I–II, no acute decompensation) — NHS-sourced ("stable").
  A single past admission that has resolved does not automatically disqualify; what
  matters is whether stability is established at time of assessment.
- Medicines optimised — NHS-sourced ("medicines optimised"). Supplementary clinical detail
  on what "optimised" means (not the NHS source itself): HFrEF — all four drug classes
  (ACEI/ARB/ARNI, beta-blocker, MRA, SGLT2i) at or approaching target doses; HFmrEF —
  ACEi/ARB/ARNI, beta-blocker, MRA at or approaching target doses, SGLT2i if prescribed
  but absence alone does NOT constitute "not optimised" (flag as data gap only, do NOT
  downgrade ELIGIBLE to BORDERLINE solely on SGLT2i absence in HFmrEF); HFpEF — diuretic
  optimised, SGLT2i if clinically indicated. Subtherapeutic doses without documented
  reason = NOT optimised. No active medication titration or recently initiated agent
  (<8–12 weeks is a supplementary clinical heuristic, not an NHS-stated window).
- Stable renal function and no electrolyte instability — supplementary clinical judgement
  (eGFR trend, hyperkalaemia risk with MRA/ARNI); the NHS source does not give numeric
  renal/electrolyte thresholds, but a patient who is biochemically unstable is not
  genuinely "stable" per the source's own requirement.
- Evidence of patient self-monitoring (weight diary, fluid balance awareness, traffic
  light symptom plan) — NHS-sourced (traffic-light system, patient/carer confidence).

**Not for PIFU — any of the following excludes:**
- NYHA Class III–IV (even if partially treated) — consistent with NHS "uncontrolled
  symptoms" / not "stable."
- Active decompensation, or multiple unplanned admissions in past 6 months indicating a
  pattern of instability — consistent with NHS "uncontrolled symptoms" / not "stable." A
  single recent admission where patient is now clearly restabilising with positive
  trajectory is BORDERLINE, not automatically NOT_ELIGIBLE. (The specific "6 months"
  window is a supplementary heuristic — the NHS source gives no time-bound number.)
- End-of-life / palliative care pathway (absolute hard exclusion) — NHS-sourced verbatim.
- Awaiting device therapy (CRT, ICD) or cardiac resynchronisation — NHS-sourced verbatim
  ("candidates for device therapy... still awaiting further diagnostic investigations
  and/or therapeutic interventions").
- Key medication wholly unoptimised or major drug class just initiated with no
  established response — consistent with NHS "medicines optimised" requirement not being
  met. The specific "<8 weeks" figure and "minor gaps = BORDERLINE" (e.g. SGLT2i not
  started in HFmrEF) are supplementary clinical judgement, not NHS-sourced.
- eGFR <30 or actively declining, or significant electrolyte abnormality (K+ >5.5 or
  actively rising) — supplementary clinical thresholds, not stated in the NHS source;
  applied here as a reasonable proxy for "not stable," not as an NHS-cited number.
- Outstanding investigation or decision regarding device therapy, surgery, or major
  management intervention still pending — NHS-sourced verbatim.

**Borderline triggers (flag with uncertainty %):**
- Single recent unplanned admission (including where the letter IS the discharge summary)
  but patient now clearly restabilising with positive trajectory
- Recent medication change (<12 weeks) but otherwise stable — re-assess after titration complete
- LVEF in borderline range (40–50%) without clear documented stability trajectory
- Recent admission >6 months ago but restabilisation not explicitly confirmed in the letter
- Diuretic use unclear (PRN vs regular) — not optimised if not on a fixed regimen
- NYHA class not formally documented — flag as data gap
- Multiple comorbidities (3+) with uncertain interactions
- Medication partially optimised (one drug class missing or subtherapeutic) but patient
  otherwise stable

---

## Arrhythmia

### Paroxysmal AF (PAF)
- First episode with reversible cause (hyperthyroidism, sepsis, GA, thoracic surgery, etc.)
  → 🔄 Discharge. Treat the cause; no ongoing cardiology follow-up needed.
- Recurrent PAF, rhythm control strategy being considered → refer to electrophysiology.
  If accepted for ablation → 🔄 Discharge from general cardiology (EP takes over).
  If ablation declined/deferred but ongoing review wanted → ✅ PIFU.
- Patient does not want ablation but wants to remain under review → ✅ PIFU.
- For PIFU: recurrent PAF, stable, no class I/III antiarrhythmic, no recent cardioversion
  (<3 months), stable anticoagulation, no structural heart disease.
- Not for PIFU: newly diagnosed, class I/III antiarrhythmic just initiated, recent
  cardioversion, symptomatic with functional limitation.
- Discharge: first episode with reversible cause resolved; or asymptomatic PAF with no
  structural disease and no ongoing intervention needed.

### Permanent AF (rate control strategy, HR <110 bpm)
- The following can be discharged to GP — no cardiology follow-up needed:
  adequate rate control + symptom control + no change in heart function + no other
  valvular or structural heart disease requiring follow-up → 🔄 Discharge.
- If any of those criteria are not met → ❌ Not for PIFU (timed follow-up needed).

### Persistent AF (>7 days, with cardioversion attempts)
- Is rhythm control strategy being considered?
  - If cardioverted and improved (symptoms, heart function), no further referral needed
    → 🔄 Discharge.
  - If cardioverted but further treatment deferred (patient choice, other pathway, etc.)
    → ✅ PIFU (patient may need reassessment when ready).
  - If referral to electrophysiologist made → 🔄 Discharge from general cardiology.
  - If rate-controlled with good LV function, asymptomatic, no rhythm control planned
    → 🔄 Discharge to GP.
- Not for PIFU: poor LV function, ongoing antiarrhythmic therapy, recent cardioversion,
  symptomatic, heart failure co-existing.

### PAF or Persistent AF treated with AV Node Ablation + Pacemaker
- NHS source (verbatim): "these patients should have an echocardiogram at 3-6 months and
  can then be discharged to follow-up at a pacing clinic and if appropriate a heart failure
  clinic." This is a distinct disposition from the general AF rules above — it is neither
  ✅ PIFU nor plain ❌ Not for PIFU under general cardiology; it is 🔄 Discharge from general
  cardiology, with ongoing follow-up transferred to the pacing clinic (and HF clinic if
  indicated), not the arrhythmia/PIFU service.
- If the letter describes AV node ablation + pacemaker with the 3–6 month echocardiogram
  already done (or planned) and follow-up handed to pacing/device clinic → 🔄 Discharge
  (from general cardiology).
- If this echocardiogram has not yet occurred and no pacing-clinic handover is documented →
  ❌ Not for PIFU (outstanding investigation).

### SVT (including AVNRT, AVRT)
- NHS source: "SVT managed successfully with medication: consider LONG-TERM PIFU."
  Medically managed SVT with stable symptoms is ELIGIBLE; "pre-ablation" alone is not
  a hard exclusion if ablation is only being discussed/considered.
- For PIFU: post-successful ablation, symptom-free ≥3 months, no antiarrhythmic needed;
  or medically managed with stable, well-tolerated medication, infrequent episodes.
- Not for PIFU: newly initiated antiarrhythmic (<8 weeks), frequent breakthrough episodes
  causing functional limitation.
- Borderline: ablation being considered or discussed (not yet committed or scheduled);
  medication recently changed with symptom response still being assessed.

### Ventricular Tachycardia (VT)
- NHS source (verbatim), structurally normal heart: "medically managed: consider TIMED PIFU
  for 3 years at the physician's discretion; managed successfully with ablation: see once
  post ablation and perform an ECG, then discharge or place on a time-limited PIFU pathway
  for 2 years."
- For PIFU: VT in structurally normal heart — either (a) medically managed, stable,
  asymptomatic, medications stable → ✅ PIFU, timed for 3 years; or (b) successful ablation,
  asymptomatic, preserved LV function, no ICD, medications stable → ✅ PIFU, timed for
  2 years (or 🔄 Discharge, at physician's discretion per source).
- Not for PIFU: VT in the context of ischaemic cardiomyopathy (see Cardiomyopathy/
  Channelopathy below); VT in non-ischaemic cardiomyopathy or inherited channelopathy (LQT,
  Brugada — see below, requires specialist long-term follow-up regardless of the VT itself
  being controlled); ICD in situ without established remote monitoring; recent ICD therapy.
- Borderline: VT with structurally normal heart but clinician explicitly expresses
  reservations, or beta-blocker/antiarrhythmic recently initiated with response not yet
  assessed.

### Cardiomyopathy and Inherited Channelopathy (as primary diagnosis, not only in VT context)
- NHS source (verbatim): "Ischaemic Cardiomyopathy (regardless of device status): Once
  optimised (medically or with ablation) these patients are not suitable for PIFU and
  should be moved to shared care with the heart failure team and pacing team or device
  team and their GP." "Non-Ischaemic Cardiomyopathy: patients should have long-term
  follow-up or shared care with the inherited cardiomyopathy team." "Inherited
  Channelopathy: patients should have long-term follow-up from the inherited channelopathy
  clinic."
- This applies regardless of whether the presenting reason is arrhythmia, routine review,
  or another trigger — a diagnosis of ischaemic cardiomyopathy, non-ischaemic
  cardiomyopathy, or an inherited channelopathy (LQT, Brugada, HCM with high-risk features,
  etc.) is NOT suitable for general-cardiology PIFU even if currently well-controlled and
  optimised. **Do not apply the general non-pathway-condition SOP test to these patients as
  if they might pass general SOP criteria and become ELIGIBLE — the NHS arrhythmia source
  places them in ongoing specialist/shared-care follow-up as a matter of course.**
- Ischaemic cardiomyopathy, once optimised → shared care with HF team + device team + GP,
  which maps to ❌ Not for PIFU (or 🔄 Discharge from general cardiology specifically if the
  letter frames it as a handover to those specific teams with no further general cardiology
  input — use clinical judgement on which label fits the letter's own framing).
- Non-ischaemic cardiomyopathy or inherited channelopathy → ❌ Not for PIFU (long-term
  specialist follow-up required, not patient-initiated).
- Borderline: letter describes a mild/low-risk cardiomyopathy phenotype (e.g. borderline
  HCM criteria) where specialist long-term follow-up is mentioned but not clearly
  established as ongoing, or where discharge/handover status is ambiguous.

### Pre-excitation (WPW pattern)
- NHS source: "Pre-Excitation (managed without EPS): Consider LONG-TERM PIFU with the
  option of periodic outpatient review." When a specialist/MDT has reviewed and determined
  no EP study is required, the risk stratification is complete — PIFU is appropriate.
- For PIFU: pre-excitation managed without EPS where electrophysiologist or MDT has
  explicitly assessed risk and determined no EP study is required, patient stable on agreed
  regimen with no presyncope; or post-ablation, symptom-free ≥3 months.
- Not for PIFU: pre-excitation where formal specialist risk assessment has NOT yet been
  performed (EP study still outstanding/undecided); EP study already scheduled; class I
  antiarrhythmic in active use.
- **WPW + AF (pre-excitation with co-existing atrial fibrillation) — clinical safety
  note:** this combination carries a distinct risk (rapid conduction over the accessory
  pathway during AF, with potential for degeneration to VF) that is not addressed
  explicitly in the NHS PIFU source. Do not default to BORDERLINE just because "an MDT has
  reviewed" the patient generically — the risk stratification that matters here is
  specific: has the accessory pathway's refractory period/risk been formally assessed
  (EP study, or exercise test confirming loss of pre-excitation at higher heart rates)?
  - Not for PIFU: pre-excitation with AF where the accessory pathway's risk has NOT been
    specifically characterised (i.e. general MDT review without EP-study-equivalent risk
    stratification of the pathway itself) — treat as high-risk by default, not borderline.
  - Borderline only if: pre-excitation with AF where the accessory pathway HAS been
    specifically risk-stratified (EP study, or exercise-test-confirmed loss of
    pre-excitation) but the letter doesn't explicitly endorse PIFU.
  - For PIFU only if: accessory pathway specifically risk-stratified AND clinician has
    explicitly endorsed PIFU suitability.
- Borderline (other than WPW+AF above): pending exercise test to assess accessory pathway;
  prior presyncope not yet fully explained.

### Ventricular Ectopy
- NHS source (verbatim), three distinct scenarios: "Asymptomatic high burden with normal
  ventricular function: patients should be offered a repeat echocardiogram at 1 year, and
  then discharged if there are no clinical concerns." "Asymptomatic or symptomatic causing
  impaired LV function, successfully treated with ablation: offer 2-year follow-up and then
  discharge if LV function has fully recovered." "Symptomatic treated with ablation, beta
  blocker or calcium channel blocker: consider time-limited PIFU at the physician's
  discretion." Note the NHS source explicitly includes calcium channel blockers alongside
  beta-blockers — not beta-blockers alone.
- Asymptomatic, high burden, normal LV: repeat echo at 1 year, then 🔄 Discharge if no
  clinical concerns — this is a timed re-check pathway, not PIFU and not immediate discharge.
- Previously impaired LV (symptomatic or asymptomatic), successfully ablated: 2-year timed
  follow-up, then 🔄 Discharge if LV function has fully recovered.
- Symptomatic, treated with ablation, beta-blocker, or calcium channel blocker: ✅ PIFU,
  time-limited, at physician's discretion. Beta-blockers or calcium channel blockers used for
  symptom control do NOT constitute antiarrhythmics requiring secondary care monitoring — a
  patient with improved or resolved symptoms on bisoprolol (or a rate-limiting CCB) and
  preserved LV is ELIGIBLE, not merely borderline.
- For PIFU (confirmed response): if the letter explicitly states symptoms are fully resolved
  or well-controlled on beta-blocker/CCB → ELIGIBLE. "Recently initiated" BORDERLINE applies
  only when symptom response has not yet been assessed.
- Not for PIFU: high ectopic burden causing LV dysfunction not yet ablated/treated
  (ectopy-induced cardiomyopathy, still active); symptomatic on class I/III antiarrhythmic
  not yet optimised; structural heart disease.
- Borderline: recently initiated beta-blocker/CCB where symptom response has not yet been
  assessed in the letter (at most BORDERLINE — not NOT_ELIGIBLE unless LV dysfunction present);
  high-burden asymptomatic case where the 1-year echo recheck has not yet occurred and no
  clinical concerns are otherwise documented.

### Other Arrhythmias (inappropriate sinus tachycardia, low-burden supraventricular ectopy)
- NHS source (verbatim): "Discharge where appropriate but may be suitable for PIFU at
  clinician's discretion." This is a distinct, explicitly lenient NHS-sourced category —
  do NOT route these conditions through the elevated non-pathway six-criteria test; treat
  them as arrhythmia-pathway conditions with a low bar for either discharge or PIFU.
- For PIFU or Discharge: low-burden supraventricular ectopy or inappropriate sinus
  tachycardia with no structural heart disease and no functional limitation — clinician
  discretion between the two, both are appropriate defaults.
- Not for PIFU: symptomatic with functional limitation not yet assessed or treated;
  structural heart disease; features suggesting a different, more specific arrhythmia
  diagnosis that should be classified under its own subtype instead.
- Borderline: clinician has not indicated a preference between discharge and PIFU, and
  the letter does not clarify ongoing specialist intent either way.

### Atrial Flutter (typical and atypical)
- NHS source, typical flutter (verbatim): "Symptom free and in sinus rhythm or stable
  well-controlled flutter with stable LV function: these patients can be discharged at
  3-6 months." "Persistent significant LV dysfunction: these patients may need ongoing
  care under a heart failure clinic." "Co-existing AF: patients should be managed under
  the AF pathway."
- NHS source, atypical flutter/AT (verbatim): "Successfully treated: patients can be
  discharged or referred back to the referring team after 6 months." "With recurrent
  atrial arrhythmias: consider suitability for a LONG-TERM PIFU pathway." Recurrent
  atypical flutter/AT under long-term management can be ELIGIBLE or BORDERLINE.
- Discharge: typical flutter, symptom-free, in sinus rhythm (or stable well-controlled
  flutter) with stable LV function, at 3–6 months → 🔄 Discharge. Atypical flutter/AT,
  successfully treated → 🔄 Discharge or referral back to originating team after 6 months.
- For PIFU: post-successful ablation, symptom-free, no recurrence, anticoagulation stable;
  atypical flutter/AT with recurrent arrhythmias under long-term management where
  clinician has considered PIFU suitability.
- Not for PIFU: typical atrial flutter where ablation is already scheduled and imminent;
  symptomatic flutter with functional limitation awaiting urgent intervention; typical
  flutter with persistent significant LV dysfunction (→ heart failure clinic, not PIFU);
  co-existing AF (→ managed under the AF pathway, apply those rules instead).
- Borderline: atypical flutter/AT where ablation is being discussed or considered (not
  yet committed or scheduled); rate-control medication recently changed; recurrent
  symptoms still under active management review; recent dose increase; typical flutter
  described as "stable" without explicit confirmation of sinus rhythm or LV function;
  recent unplanned admission >6 months ago without confirmed restabilisation.

### Universal Arrhythmia Exclusions
**Correction (2 July 2026, second deep-verification pass):** an earlier pass on this same
sweep incorrectly stated "the NHS arrhythmia document contains no single universal-
exclusions section." That was wrong — a full line-by-line re-read of the source found it
under the heading **"General Inclusion and Exclusion Criteria"** at the very top of the
document, before the condition-specific sections. The corrected sourcing below replaces
the previous (inaccurate) note.

**NHS-sourced, verbatim, universal (applies regardless of arrhythmia subtype):**
- **Inclusion:** "Aged 18 and over." "Patient or carer understands the principles of a PIFU
  pathway and feels confident using it." "Regardless of the type of arrhythmia, patient is
  stable, and their medicines have been optimised."
- **Exclusion:** "Patients with outstanding investigations or decisions still to be made
  regarding further options for care." "Cannot easily contact the service (e.g. lack of
  access to telephone/internet)." "Low level of knowledge, skills and confidence to manage
  their follow-up care and/or no carer support."

**Disclosed policy choice (same pattern as valve disease and heart failure below):** the
source treats "cannot easily contact the service" and "low knowledge/skills/confidence
and/or no carer support" as hard universal exclusions. Step 2a's Universal SOP deliberately
treats these same two concepts as "requires careful consideration, not automatic exclusion"
— BORDERLINE-capable, not a hard bar — for consistency across all three NHS-pathway
conditions and to avoid the v4 regression pattern. Intentional, disclosed, not an oversight.

**The four bullets below are NOT the verbatim universal list above — they are a mix of
per-subtype synthesis and unsourced supplementary judgement, kept because they are
clinically sound, but must not be presented as the NHS universal exclusion list:**
- Any device patient (pacemaker, ICD, CRT) without remote monitoring in place —
  **re-checked this pass: this is NOT actually traceable to the CRM Devices section as
  previously claimed.** That section only says devices already on PIFU can use remote
  monitoring "to identify cause of symptoms" during review — it does not state remote
  monitoring is a mandatory precondition for device patients to enter PIFU at all. This
  bullet is supplementary clinical judgement, not NHS-sourced.
- Newly initiated class I or III antiarrhythmic drug (amiodarone, flecainide, sotalol) —
  this IS consistent with per-subtype PAF/SVT sections ("symptomatic, managed with class 1
  or class 3 anti-arrhythmic drug: PIFU is NOT suitable"), so this one bullet is genuinely
  subtype-verbatim, just not phrased as a standalone universal NHS statement.
- Reversible cause not yet addressed (thyroid disease, electrolyte abnormality) —
  **supplementary clinical judgement, not NHS-sourced**
- High-risk arrhythmia without curative intervention (e.g. VT in channelopathy, Brugada,
  complete heart block without pacemaker) — **supplementary clinical judgement, not
  NHS-sourced**; the channelopathy/Brugada long-term-follow-up requirement itself IS
  NHS-sourced (see Cardiomyopathy/Channelopathy above), only the "complete heart block
  without pacemaker" example and the "curative intervention" framing are not

---

## Heart Valve Disease

### Aortic Stenosis (AS)
- NHS source entry criterion (verbatim): "Low to moderate aortic stenosis (Vmax <3.5 m/s
  with preserved left ventricular function)." Leave-PIFU trigger (verbatim): "Aortic valve
  Vmax >3.5m/sec or AVA <1.2cm2." **This 3.5 m/s threshold is the NHS PIFU-suitability
  cutoff and is deliberately more conservative than the general cardiology "severe AS"
  definition (Vmax ≥4.0 m/s) — do not use 4.0 m/s as the PIFU entry threshold.**
- For PIFU: Vmax <3.5 m/s, preserved LV function, normal flow, asymptomatic, stable on
  serial echo with no rapid progression.
- Not for PIFU: Vmax >3.5 m/s or AVA <1.2 cm² (NHS leave-PIFU trigger); symptomatic AS;
  low-flow physiology (NHS source excludes low-flow states from this pathway given
  assessment complexity in the context of LV impairment); awaiting TAVI/SAVR. General
  cardiology "severe AS" thresholds (Vmax ≥4.0 m/s, mean gradient ≥40mmHg, AVA <1.0cm²)
  are unambiguously NOT_ELIGIBLE but are not the operative cutoff for this pathway — the
  3.5 m/s NHS threshold applies first.
- Borderline: Vmax approaching 3.5 m/s with genuine ambiguity in the reading; AVA close to
  1.2cm² boundary. (Rate-of-progression figures such as ">0.3 m/s/year" are a supplementary
  clinical heuristic, not stated in the NHS source — use only as a soft signal, not a hard
  threshold.)

### Aortic Regurgitation (AR)
- NHS-sourced imaging surveillance interval: 1–2 years.
- NHS source entry criterion: "Moderate aortic regurgitation with preserved LVEF." Leave-PIFU
  triggers (verbatim): "left ventricular dilatation" (no numeric threshold given); "aortic
  dimensions ≥40mm" (this refers to aortic root/dimension, given the aortopathy association
  with AR — NOT an LV chamber size); "progression to severe AR"; "PA systolic pressure
  >50mmHg." **The source does not give an LVESD number for AR at all — any LVESD threshold
  (e.g. "50mm") is a supplementary clinical heuristic, not NHS-sourced, and should not be
  presented as if it were.**
- For PIFU: mild-to-moderate AR, preserved LV size and function, asymptomatic, aortic root
  <40mm.
- Not for PIFU: severe AR; LV dilatation (qualitative — no NHS-specified number; use clinical
  judgement); aortic root ≥40mm; EF <50% in context of AR; symptomatic; awaiting surgery.
- Borderline: aortic root approaching 40mm; LV size/function described qualitatively as
  "borderline" or "mildly dilated" without quantification.

### Mitral Regurgitation (MR)
- NHS-sourced imaging surveillance interval: 18 months – 2 years.
- NHS source entry criterion: "Moderate mitral valve disease: preserved LVEF, PA pressure
  <50mmHg" — no specific LVEF% cutoff for ENTRY. "Leave PIFU if LVEF <60%" is a
  surveillance exit trigger, NOT an entry exclusion. LVEF ≥55% with stable symptoms is
  the practical entry threshold; LVEF 55–59% is BORDERLINE (not NOT_ELIGIBLE). **The NHS
  source gives no LVESD or EROA number anywhere for MR — the 38–40mm LVESD band and
  0.35–0.40cm² EROA band below are supplementary clinical heuristics (general
  echocardiography practice), not NHS-sourced, and should be treated as softer signals
  than the sourced LVEF/PA-pressure criteria.**
- For PIFU: mild-to-moderate MR, preserved LV function (LVEF ≥55%, PA pressure <50mmHg),
  asymptomatic.
- Not for PIFU: severe MR; EF <55%; symptomatic; surgical referral made; PA pressure
  >50mmHg; new/worsening LV or RV dysfunction; new tricuspid regurgitation ≥moderate
  (all NHS-sourced leave-triggers).
- Borderline: LVEF 55–59% with otherwise stable picture; supplementary heuristics only —
  LVESD 38–40mm or EROA 0.35–0.40cm² if reported, flagged as soft signals, not
  independently NHS-sourced thresholds.

### Mitral Stenosis (MS)
- NHS-sourced imaging surveillance interval: 2–3 years.
- NHS source (verbatim): "Mild to moderate mitral stenosis (MVA > 1.5cm2)" is the
  PIFU-suitable entry criterion; leave-PIFU trigger is "mitral valve area <1.5cm2." The
  source explicitly notes some patients with MVA <1.5cm² are symptomatic and need closer
  evaluation — not suitable for PIFU.
- For PIFU: MVA >1.5cm², no haemodynamic compromise, asymptomatic.
- Not for PIFU: MVA <1.5cm² (NHS leave-trigger, verbatim); symptomatic; awaiting
  intervention; new PA pressure >50mmHg; new tricuspid regurgitation ≥moderate.

### Mitral Valve Prolapse (MVP)
- NHS-sourced imaging surveillance interval (no/mild MR): 3–5 years. If moderate MR is
  present, follow the Mitral Regurgitation imaging interval (18 months – 2 years) instead.
- NHS source: MVP with no/mild MR follows the MVP imaging pathway. MVP with moderate MR
  follows the Moderate MR pathway (entry: preserved LVEF, PA <50mmHg — no hard % for
  entry). LVEF 55–59% with stable symptoms ≥12 months and clinician explicitly placing
  on PIFU is ELIGIBLE; LVEF 55–59% without explicit clinician PIFU endorsement is BORDERLINE.
- For PIFU: non-severe MVP (mild-moderate MR if present), asymptomatic, preserved LV
  (LVEF ≥55%), no malignant arrhythmia pattern, stable symptoms ≥12 months.
- Not for PIFU: severe MR from MVP; MVP with complex arrhythmia (malignant MVP syndrome);
  significant LV dilatation; LVEF <55%.
- Borderline: moderate MR from MVP with LVEF 55–59% without explicit clinician PIFU
  endorsement; recent new symptoms not yet fully assessed.

### Bicuspid Aortic Valve (BAV)
- NHS source (verbatim): imaging interval "2-5 years (12 months in the presence of aortic
  dilatation >40mm)." Leave-PIFU triggers: new/worsening symptoms, new dysrhythmia, new
  LV/RV dysfunction, "significant aortic dilatation" (unquantified in the leave-trigger
  itself), progression to moderate valve disease, PA pressure >50mmHg. **The 40mm figure
  is the point at which imaging surveillance tightens to 12 months — it does not by itself
  mean the patient leaves PIFU. A distinct, larger root size (e.g. >45mm, a general
  aortopathy surgical threshold) is a supplementary heuristic for "significant" dilatation
  warranting NOT_ELIGIBLE, not an NHS PIFU-specific number.**
- **NHS-sourced imaging-adequacy caveat (verbatim, previously missing from this file —
  found on a full re-read of the source): "Association of aortopathy with this condition.
  Consider cross-sectional imaging to check for underlying aortopathy at baseline. If
  echocardiogram cannot assess aortopathy alone, patient is NOT suitable for PIFU."** This
  is a distinct exclusion from the aortic-root-size triggers above — it is about whether
  the imaging modality itself is adequate to characterise the aortic root, not about the
  root size being abnormal. If a letter describes echo as unable to adequately visualise
  the aortic root/proximal aorta (and no cross-sectional imaging such as CT/MRI has been
  done to supplement it), this is NOT_ELIGIBLE regardless of how stable the valve lesion
  itself appears — not merely a data gap/BORDERLINE trigger, since the NHS source states
  this outright as a "NOT suitable" condition, not an ambiguity.
- For PIFU: BAV with mild-moderate non-severe valve disease (AS or AR), asymptomatic,
  preserved LV, stable on serial imaging (with imaging confirmed adequate to assess the
  aortic root, per the caveat above), aortic root ≤40mm (or >40mm but stable and under
  12-month surveillance with no other leave-trigger present).
- Not for PIFU: severe valve disease; clearly significant aortic root dilatation (using
  ~45mm as a supplementary clinical reference point, since the NHS source does not
  quantify "significant" for the leave-trigger); awaiting intervention; echocardiogram
  unable to assess aortopathy/aortic root with no supplementary cross-sectional imaging
  performed (NHS-sourced, verbatim, see above).
- Borderline: aortic root in the 40–45mm range where "significant" is not clearly
  established either way; mild-moderate severity at the upper end of the range
  (Vmax 3.5–3.8 m/s); recent decompensation >6 months ago without confirmed
  restabilisation.

### Post-Valve Intervention — TAVI, Bioprosthetic Valve, Mitral Repair, TEER
- NHS-sourced imaging surveillance interval: 1–2 years.
- NHS source: TAVI, TEER, bioprosthetic valve, and repair are SUITABLE for PIFU. The
  ONLY pre-condition is: "Ensure routine post-operative TTE performed before entering
  patient onto PIFU." There is NO timing restriction. If TTE is done and normal, PIFU
  is appropriate regardless of time since procedure. "Patients with abnormal baseline echo
  should NOT be considered for PIFU." Some units may only start bioprosthetic surveillance
  after 5–10 years depending on patient/valve risk factors (young age at implant, smokers,
  diabetes, renal disease may need more frequent imaging at the overseeing clinician's
  discretion).
- For PIFU: fully recovered, normally functioning prosthesis confirmed on post-operative
  TTE, stable anticoagulation (therapeutic and stable INR for warfarin; DOAC if
  bioprosthetic), preserved LV function (EF ≥50%), no complications, NYHA I–II.
- Not for PIFU: no post-operative TTE yet performed; abnormal post-op TTE (LV impairment
  EF <50%, significant paravalvular leak, patient-prosthesis mismatch); NYHA III–IV
  post-intervention; unstable or subtherapeutic anticoagulation; prosthetic valve concern
  (stenosis, regurgitation, thrombosis); significant increase in mean valve gradient vs
  previous echo ≥10mmHg (NHS-sourced leave-trigger, verbatim); new tricuspid regurgitation
  ≥moderate; new valve prosthesis regurgitation ≥moderate.
- Borderline: post-op TTE performed and normal but patient still in early clinical
  recovery with ongoing specialist review; multiple comorbidities (3+); frailty not
  formally assessed.

### Post-Valve Intervention — Mechanical Valve Prosthesis (distinct pathway — NOT the same as above)
- NHS source (verbatim): "Mechanical valve prosthesis with no associated aortopathy" has
  its own, distinct NHS entry: imaging follow-up interval "n/a" — "No imaging follow-up
  required" at all, unlike the bioprosthetic/TAVI/TEER/repair pathway above. The only
  precondition is the same routine post-operative TTE before entering PIFU.
- NHS source (verbatim) caveats: "Patients with bicuspid aortic valve or co-existent
  untreated valve lesions may not be suitable for PIFU." "Consider TTE at 5 years in
  isolated mechanical MVR to assess right heart and for tricuspid regurgitation."
- For PIFU: isolated mechanical valve prosthesis, no associated aortopathy, no co-existent
  untreated valve lesion, no BAV, post-operative TTE performed and normal, stable
  anticoagulation (therapeutic and stable INR for warfarin).
- Not for PIFU: co-existent BAV or untreated valve lesion (NHS-sourced caveat — treat as
  a reason to NOT default to this simpler no-surveillance pathway); no post-operative TTE
  performed; unstable or subtherapeutic anticoagulation; prosthetic valve concern.
- Borderline: isolated mechanical MVR approaching the 5-year mark where a TTE to assess
  right heart/tricuspid regurgitation has not yet been arranged or documented.
- Do not apply the 1–2 year imaging-surveillance requirement above (for TAVI/bioprosthetic/
  repair/TEER) to mechanical valve prostheses without associated aortopathy — they follow
  this separate, less imaging-intensive NHS pathway instead.

### Universal Valve Exclusions
**Source fidelity note:** unlike arrhythmia, the NHS valve disease document DOES contain an
explicit, verbatim "NOT Suitable for Heart Valve PIFU" universal list: "Patients with SEVERE
valvular disease. Patients with SYMPTOMATIC valvular disease. Patients with LEFT
VENTRICULAR IMPAIRMENT. Patients with outstanding investigations or decisions still to be
made. Patients with complex HVD or who would benefit from regular review of clinical
status. Patients who do not have the knowledge, skills and confidence to manage follow-up.
Patients who cannot easily contact the service. Patients deemed by their clinician to be
unsuitable for valvular intervention (e.g. frailty, multiple co-morbidities) — these should
be discharged back to their GP." The bullets below map onto that verbatim list, but the
specific "EF <50%" number and "rapid echocardiographic progression" framing are NOT
part of that universal list — the source only says "LEFT VENTRICULAR IMPAIRMENT"
(unquantified) and does not mention echo progression rate as a universal criterion at all;
those two specifics are supplementary clinical judgement drawn from the per-subtype
"Leave PIFU" triggers instead (see subtype sections above).
- Any moderate valve disease with symptoms (dyspnoea, syncope, chest pain) — maps to
  NHS-sourced "Patients with SYMPTOMATIC valvular disease" (source says symptomatic
  generally, not specifically "moderate with symptoms")
- Severe valve disease of any type — NHS-sourced verbatim ("Patients with SEVERE
  valvular disease")
- LV dysfunction (EF <50% for AR/MR; EF <50% post-intervention) — NHS-sourced concept
  ("Patients with LEFT VENTRICULAR IMPAIRMENT"); the specific 50% cutoff is supplementary
  clinical judgement, not an NHS-stated number
- Awaiting intervention (surgical or TAVI) — maps to NHS-sourced "outstanding investigations
  or decisions still to be made"
- Rapid echocardiographic progression (serial echo showing significant change) —
  **supplementary clinical judgement, not part of the universal NHS list**; individual
  subtype "Leave PIFU" triggers do reference progression (e.g. "progression to severe AR"),
  but there is no universal echo-progression-rate criterion in the source

**Disclosed policy choice — three NHS-listed valve exclusions deliberately NOT hardened
here:** the verbatim list above also names "complex HVD or who would benefit from regular
review of clinical status," "do not have the knowledge, skills and confidence to manage
follow-up," and "cannot easily contact the service" as things that make a patient NOT
suitable for valve PIFU. The general Step 2a Universal SOP criteria in SKILL.md treat these
same three concepts (3+ comorbidities with uncertain interactions; low health literacy/
patient activation; difficulty contacting the service) as "requires careful consideration,
not automatic exclusion" — i.e. BORDERLINE-capable, not a hard bar. This is an intentional,
disclosed choice, not an oversight: hardening these into automatic NOT_ELIGIBLE for valve
patients specifically would reintroduce the exact v4 regression pattern (treating soft/
uncertain factors as exclusion rather than uncertainty) that this skill was rebuilt to fix.
If a supervisor wants valve disease to apply the NHS wording more strictly than other
conditions on these three points, that would need an explicit, separate policy decision —
it should not be inferred silently from this quote.

---

## Chest Pain / Stable Angina / Post-MI (GIRFT pathway)

This is not one of the three NHS-pathway conditions (arrhythmia, valve disease, heart
failure) with a dedicated PIFU eligibility document, but it is NOT a true non-pathway
condition either. The GIRFT Outpatient Operational Guide has an explicit "Cardiology —
Chest Pain" pathway with concrete PIFU guidance. Do not apply the elevated "all six general
SOP criteria must be clearly met" bar used for POTS/cardiomyopathy — apply these
GIRFT-sourced rules directly, alongside the universal SOP criteria in Step 2a.

**GIRFT source, verbatim substance:** "PIFU should be used where appropriate, particularly
in the following: if symptoms require reassessment, this can be delivered via (nurse-led)
PIFU/SPoA. PIFU should ideally be limited to 6-12 months. Where PIFU is requested, clinical
triage is advisable to ensure most effective review undertaken." Post-PCI outcome
assessment "assesses symptoms and can be done virtually." Reviewing anti-anginal medication
and secondary prevention "should not require face-to-face discussion" (GIRFT, chest pain
pathway) — the same principle GIRFT applies to aortic stenosis medication review.

**For PIFU:**
- Stable angina, secondary prevention optimised (statin, antiplatelet, anti-anginal
  medication at an established, tolerated dose), no high-risk features on non-invasive
  assessment, no further invasive workup planned
- Post-PCI, symptoms stable or resolved, outcome assessable virtually, no further
  intervention planned
- Post-MI, fully investigated, secondary prevention established, no residual ischaemia
  requiring further action, cardiac rehabilitation completed or in progress

**Not for PIFU:**
- Acute coronary syndrome / unstable angina, or any presentation still being actively
  worked up (troponin pending, awaiting CTCA/functional imaging/angiogram decision) —
  this is an outstanding-investigation exclusion, same as the universal SOP rule
- High-risk features on non-invasive assessment with MDT discussion or invasive
  investigation (angiogram, PCI) still pending or scheduled
- Anti-anginal medication just initiated or being actively titrated, response not yet
  established

**Borderline:**
- Symptom control described qualitatively as "improved" without confirmation that no
  further ischaemia workup is planned
- Recent anti-anginal dose change where response is still being assessed in the letter
- Post-PCI but very early in recovery, virtual outcome assessment not yet documented

**PIFU timescale:** 6–12 months per GIRFT, with clinical triage on request — consistent
with the aortic stenosis and AF GIRFT timescales, not the longer NHS-arrhythmia-specific
2–3 year timed pathways (those apply only to arrhythmia, not chest pain/angina/post-MI).
