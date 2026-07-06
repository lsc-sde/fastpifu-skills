---
name: fastpifu-cardiology
description: >
  Assess cardiology outpatients for follow-up disposition: Discharge to GP, For PIFU
  (patient-initiated follow-up), Not for PIFU (timed scheduled follow-up), or Borderline
  with a certainty %. Use when reviewing a cardiology clinic letter, discharge summary, or
  outpatient note to decide what should happen next with the patient's specialist follow-up.
  Triggers on: "is this patient for PIFU", "can this patient be discharged", "screen this
  letter for PIFU eligibility", "assess follow-up", "PIFU or discharge?". Handles arrhythmia
  (AF, SVT, flutter, VT, ectopy, post-ablation, devices), valve disease (all subtypes,
  post-TAVI/TEER), heart failure (HFrEF/HFpEF/HFmrEF), POTS, stable angina, post-MI,
  and cardiomyopathy. Entirely self-contained — no internet required.
---

## Overview

This skill assesses whether a cardiology patient is eligible for a Patient-Initiated Follow-Up
(PIFU) pathway. It works by first loading up-to-date NHS guidance on PIFU eligibility for three
cardiology sub-specialties (arrhythmia, valve disease, heart failure), then applying the local
Standard Operating Procedure (SOP), and finally screening the patient's clinical documentation
to reach a clear, evidence-based verdict.

**NHS-pathway conditions** (dedicated eligibility criteria exist):
- Arrhythmia (AF, SVT, palpitations, atrial flutter, ventricular ectopy, VT, pre-excitation, post-ablation, device patients)
- Mild-to-moderate heart valve disease (including bicuspid aortic valve, post-valve intervention)
- Heart failure (HFpEF, HFrEF, and HFmrEF)

**Non-pathway conditions** (apply general SOP criteria — see Step 2b):
- POTS (Postural Orthostatic Tachycardia Syndrome)
- Stable angina / chronic stable IHD / post-MI
- Cardiomyopathies (DCM, HCM — low-risk non-obstructive only)
- Any other cardiology condition not covered by NHS England PIFU specialty guidance

For non-pathway conditions the skill must explicitly state that no dedicated NHS PIFU pathway
exists and that the verdict is based on general SOP criteria alone.

The output is always one of:
- ✅ **For PIFU** — patient meets eligibility criteria (`ELIGIBLE`)
- ❌ **Not for PIFU** — patient does not meet criteria (`NOT_ELIGIBLE`)
- ⚠️ **Uncertain — [X]% likely For PIFU** — criteria partially met; include reasoning (`BORDERLINE`)
- 🔄 **Discharge** — patient appropriate for GP discharge, not specialist follow-up (`NOT_ELIGIBLE`)

**Critical distinction — Discharge vs Not for PIFU vs For PIFU:**

This skill is designed for patients who are **already in outpatient cardiology follow-up**.
The question it answers is: *what should happen next with this patient's specialist follow-up?*
There are three possible answers:

- ✅ **For PIFU** — the specialist relationship continues, but the patient contacts the service
  when something changes rather than being booked in routinely. The clinician is still
  responsible; the trigger mechanism shifts to the patient.
- ❌ **Not for PIFU** — the specialist relationship continues, but follow-up must be
  *timed and scheduled* by the clinician. The patient is not stable or informed enough to
  self-initiate safely (e.g. NYHA III, recent admission, medication being uptitrated,
  pending investigations).
- 🔄 **Discharge** — no ongoing specialist follow-up is needed at all. The patient is handed
  back to GP entirely. The cardiologist's episode of care is complete. Common examples:
  asymptomatic PAF with no structural disease; persistent AF rate-controlled with good LV
  function; mild stable valve disease explicitly discharged to GP; post-valve intervention
  fully recovered with no ongoing specialist need.

The key question to distinguish Not for PIFU from Discharge: *does the clinician intend to
see this patient again in a specialist setting?* If yes → Not for PIFU (timed) or For PIFU.
If no → Discharge. If the letter ends with "no further follow-up required", "discharged to
your care", or "no further specialist input needed", that is always a Discharge.

**Prioritisation principle (GIRFT guidance):** Identifying patients who can be safely
discharged is MORE important than identifying PIFU candidates. Reducing unnecessary
follow-up appointments creates clinic capacity for new patients and reduces waiting lists.
The first clinical question is therefore always: *can this patient be discharged entirely?*
Only if the answer is no does the PIFU vs timed follow-up question apply. The initial clinic
appointment should be set up with enough time and information to aim to avoid any need for
further face-to-face follow-up.

A discharge case should never be recorded as PIFU-eligible. If a letter appears clinically
clean (no flags, no borderline reasons) but describes a scenario where the clinician is
handing the patient back to GP with no ongoing specialist role, classify as 🔄 Discharge.

**Borderline vs Not for PIFU — when to use each:**
Having an exclusion flag does not automatically mean NOT_ELIGIBLE. If a case has one or more
exclusion flags but also has significant mitigating factors or clinical ambiguity (e.g. recent
admission but now clearly restabilised; medication not fully optimised but plan documented),
it may still be BORDERLINE. Reserve NOT_ELIGIBLE for cases where exclusion criteria are
unambiguous and no meaningful clinical uncertainty remains. When genuinely in doubt between
NOT_ELIGIBLE and BORDERLINE, prefer BORDERLINE — it is safer than both over- and under-calling.

---

## Workflow

### STEP 1 — Gain Background Knowledge (NHS-pathway conditions)

Read the following local reference files. All content is pre-extracted from NHS England and
GIRFT sources (extracted 25 June 2026). This skill is fully self-contained — no internet access
is required or used.

**What PIFU is (general NHS guidance):**
Read `references/nhs-pifu-what-is-pifu-extracted-2026-06-25.docx`

**Arrhythmia PIFU guidelines (AF, SVT, flutter, VT, ectopy, ablation, devices):**
Read `references/nhs-pifu-arrhythmia-extracted-2026-06-25.docx`

**Valve disease PIFU guidelines (AS, AR, MR, MS, MVP, BAV, post-TAVI/TEER/repair):**
Read `references/nhs-pifu-valve-disease-extracted-2026-06-25.docx`

**Heart failure PIFU guidelines (HFrEF, HFpEF, HFmrEF — continuous PIFU pathway):**
Read `references/nhs-pifu-heart-failure-extracted-2026-06-25.docx`

**GIRFT Outpatient Operational Guide — cardiology pathways (AF, aortic stenosis, chest pain, LBBB, heart failure):**
Read `references/girft-outpatient-cardiology-extracted-2026-06-25.docx`

**Fallback:** If any .docx file cannot be read, use `references/nhs-pifu-criteria-summary.md`
which contains a condensed summary of all NHS PIFU eligibility criteria.

From each file, extract and internally note:
- Which patients ARE eligible (inclusion criteria)
- Which patients are NOT eligible (exclusion criteria / red flags)
- Any monitoring requirements or caveats specific to that condition

Note: Reference files were last extracted on 25 June 2026. If more than 12 months have passed
since this date, consider re-extracting from the original NHS England sources.

---

### STEP 2 — Learn the Local SOP

Read the Standard Operating Procedure document:
`References/prn02169-ii-patient-initiated-follow-up-standard-operating-procedure-template.docx`

**2a. Universal SOP eligibility conditions (apply to ALL conditions):**

Patient IS likely suitable if:
- Low risk of urgent follow-up care and satisfies specialty criteria
- Understands and accepts responsibility for their care on the PIFU pathway
- Has sufficient health literacy and patient activation (confidence, knowledge, skills)
- Understands which symptom changes should prompt re-contact (knows their "traffic light" symptoms)
- Has the tools needed to monitor their condition (devices, apps, leaflets, weight scales)
- Able to contact the service easily (telephone/digital access)

Patient requires CAREFUL CONSIDERATION (not automatic exclusion) if:
- Health issues are particularly complex or involve 3+ significant comorbidities with uncertain interactions
- Medicines require regular and robust secondary care monitoring
- Difficulty contacting the service
- Low health literacy or patient activation
- Clinical requirement for timed follow-ups
- Safeguarding concerns
- Frailty — flag as a data gap if no formal frailty assessment is documented; do not
  automatically exclude, but reduce certainty if frailty is mentioned without formal scoring

**Absolute exclusions from PIFU (apply universally):**
- Active decompensation or acute illness
- End-of-life or palliative care pathway (hard exclusion)
- Pending investigations or procedures that would change management
- Patient unable or unwilling to take responsibility for self-initiated care
- Recently initiated medication requiring active secondary care monitoring
  (e.g. new antiarrhythmic, new ARNI, new diuretic titration)

**2b. General SOP criteria for non-pathway conditions (POTS, stable angina, post-MI, etc.):**

When no dedicated NHS PIFU pathway exists, ALL of the following must be met:
1. Clinically stable — no active decompensation, acute symptoms, or pending intervention
2. Diagnosis established — no outstanding investigations that would change management
3. Treatment optimised — not in an active titration or initiation phase requiring monitoring
4. No secondary care drug monitoring requirement (e.g. no warfarin INR, no frequent U&Es
   for recently changed nephrotoxic drugs, no antiarrhythmic drug monitoring)
5. Patient activation confirmed — documented evidence they understand their condition,
   know their red flag symptoms, and feel confident to self-manage
6. No device safety concern requiring timed follow-up (e.g. ICD with recent therapies,
   pacemaker without remote monitoring, CRT requiring optimisation)

If ALL six are met → eligible for PIFU under general SOP criteria.
If ANY one is not met → Not for PIFU; state which criterion failed.

---

### STEP 2c — POTS-Specific Guidance

**Important:** There is NO dedicated NHS England PIFU pathway for POTS. All POTS assessments
must use general SOP criteria (Step 2b) and must include this explicit statement in the output:

> "No dedicated NHS England PIFU pathway exists for POTS. This assessment applies
> general NHS PIFU SOP eligibility criteria."

**POTS: Factors supporting PIFU (when general SOP criteria are met):**
- Diagnosis confirmed (tilt table test or NASA lean test with HR increment ≥30bpm)
- Symptoms significantly improved or stabilised on current management
- Conservative measures in place (salt/fluid loading, compression, graded exercise)
- If on medication (e.g. Ivabradine, Propranolol, Midodrine): stable dose ≥3 months,
  no monitoring requirement in secondary care
- No syncopal episodes in past 3 months (presyncope alone may be acceptable if improving)
- Patient actively self-monitoring (symptom diary, HR tracking)
- Returned to meaningful daily activities (work, education, independent living)
- Understands triggers and knows when to re-contact

**POTS: Factors against PIFU:**
- Newly diagnosed (within 3 months) — diagnosis and management not yet established
- Medication just initiated or being titrated — requires response monitoring
- Outstanding investigations (autoimmune screen, genetic testing, secondary cause workup)
- Frequent syncopal episodes (≥1/month) — safety concern
- Significant functional limitation preventing self-monitoring
- Comorbidities complicating management (e.g. hypermobile EDS, mast cell disorder)
  that require coordinated specialist review
- No improvement after ≥6 months of optimised conservative management — warrants
  reassessment before PIFU

**POTS PIFU timescale:** 12 months (review at end of period; re-assess for continuation
or discharge). Patient should be given written information on POTS symptom triggers and
a clear re-contact pathway.

---

### STEP 2d — Condition-Specific Decision Rules

These rules are drawn from analysis of real-world PIFU eligibility patterns across the
three NHS-pathway conditions. Apply them during Step 3 alongside the general SOP criteria.

#### Discharge-to-GP Scenarios (check these BEFORE deciding PIFU-eligible)

These scenarios commonly present as clinically clean (no exclusion flags, no borderline
reasons) but are actually appropriate for GP discharge rather than PIFU. Always check
whether the letter describes one of these patterns before concluding ELIGIBLE:

| Scenario | Correct verdict |
|---|---|
| PAF — first episode, reversible cause identified and treated | 🔄 Discharge |
| PAF — recurrent, referred to EP and accepted for ablation | 🔄 Discharge (EP takes over) |
| PAF — asymptomatic, no structural disease, no antiarrhythmic needed, no ongoing intervention | 🔄 Discharge |
| Permanent AF — rate controlled (HR <110), symptoms controlled, no change in heart function, no structural disease needing follow-up | 🔄 Discharge |
| Persistent AF — cardioverted and improved, no further referral needed | 🔄 Discharge |
| Persistent AF — referred to electrophysiologist, no other follow-up needed | 🔄 Discharge |
| Persistent AF — rate-controlled, good LV function, asymptomatic, no rhythm control planned | 🔄 Discharge |
| PAF or persistent AF on class I/III antiarrhythmic (flecainide, amiodarone, sotalol) | ❌ Not for PIFU (requires long-term follow-up or GP shared care) |
| Post-successful ablation (AF, flutter, SVT, VT) — GIRFT: routine doctor clinic not needed | ✅ PIFU (nurse-led, 6–12 months) |
| Post-cardioversion — GIRFT: routine doctor clinic not needed, ECG/symptom review required | ✅ PIFU (6–12 months) |
| Post-valve intervention, fully recovered, normally functioning prosthesis, preserved LV, no ongoing specialist need | 🔄 Discharge |
| Aortic stenosis — no intervention needed, asymptomatic, stable | physiologist-led echo surveillance (not routine doctor PIFU) |
| Mild stable valve disease explicitly handed to GP, no further imaging surveillance planned | 🔄 Discharge |
| Bicuspid aortic valve with no significant haemodynamic lesion, no aortic root concern, explicitly discharged to GP | 🔄 Discharge |
| Heart failure — fully investigated, on optimal treatment, stable | ✅ PIFU where appropriate (GIRFT) |
| HFpEF — hospital clinic rarely needed; community HF team managing | 🔄 Discharge or community HF team follow-up |
| Hypertension — specialist episode concluded, management optimised, handed to GP | 🔄 Discharge |
| LBBB — without concerning history/investigations including echo, no structural disease | 🔄 Discharge (no cardiology referral needed per GIRFT) |

The key signal for discharge vs PIFU is whether the clinician intends any ongoing specialist
relationship at all. If the letter ends with "no further follow-up required", "discharged to
your care", or "no further specialist input needed", that is a discharge — regardless of how
clinically stable the patient appears.

---

#### Heart Failure (HFpEF / HFrEF / HFmrEF)

**For PIFU — all of the following must be present:**
- Clinically stable (NYHA Class I–II, no acute decompensation)
- No unplanned hospital admission in the past 6 months (the training data shows this is
  the single strongest exclusion flag — recent admission disqualifies even patients who
  look stable in clinic)
- Optimised GDMT: for HFrEF/HFmrEF, look for all four drug classes (ACEI/ARB/ARNI,
  beta-blocker, MRA, SGLT2i) at or approaching target doses; for HFpEF, look for
  diuretic optimisation and SGLT2i if indicated; medications at low/sub-therapeutic doses
  that haven't been uptitrated are NOT optimised
- No active medication titration or recently initiated agent (<8–12 weeks)
- Stable renal function (eGFR trend not declining; watch for post-ARNI eGFR drops)
- No electrolyte instability (hyperkalaemia with MRA/ARNI is a common trap)
- Evidence of patient self-monitoring (weight diary, fluid balance awareness, traffic
  light symptom plan)

**Not for PIFU — any of the following excludes:**
- NYHA Class III–IV (even if partially treated)
- Recent admission <6 months (hard exclusion regardless of current clinical appearance)
- End-of-life / palliative care pathway (absolute hard exclusion)
- Awaiting device therapy (CRT, ICD) or cardiac resynchronisation
- Medication not yet optimised or currently being uptitrated
- eGFR <30 or actively declining after a recent medication change
- Significant electrolyte abnormality (K+ >5.5 or actively rising)
- Complex comorbidities with uncertain interaction requiring coordinated specialist review

**Borderline triggers (flag with uncertainty %):**
- Recent medication change (<12 weeks) but otherwise stable — re-assess after titration complete
- LVEF in borderline range (40–50%) without clear documented stability trajectory — request
  serial echo data; classify as borderline until trajectory is confirmed
- Recent admission >6 months ago but restabilisation not explicitly confirmed in the letter
- Diuretic use unclear (PRN vs regular) — not optimised if not on a fixed regimen
- NYHA class not formally documented — flag as data gap
- Multiple comorbidities (3+) with uncertain interactions

#### Arrhythmia

**Subtype-specific rules:**

*Paroxysmal AF (PAF):*
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

*Permanent AF (rate control strategy, HR <110 bpm):*
- The following can be discharged to GP — no cardiology follow-up needed:
  adequate rate control + symptom control + no change in heart function + no other
  valvular or structural heart disease requiring follow-up → 🔄 Discharge.
- If any of those criteria are not met → ❌ Not for PIFU (timed follow-up needed).

*Persistent AF (>7 days, with cardioversion attempts):*
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

*SVT (including AVNRT, AVRT):*
- For PIFU: post-successful ablation, symptom-free ≥3 months, no antiarrhythmic needed;
  or medically managed with stable, well-tolerated medication, infrequent episodes
- Not for PIFU: newly initiated medication, frequent breakthrough episodes, pre-ablation
  EP study pending

*Ventricular Tachycardia (VT):*
- For PIFU: VT in structurally normal heart, successful ablation, asymptomatic, preserved
  LV function, no ICD, medications stable
- Not for PIFU: VT in non-ischaemic cardiomyopathy (requires inherited cardiomyopathy
  pathway, not PIFU); VT in inherited channelopathy (LQT, Brugada — requires specialist
  long-term follow-up); ICD in situ without established remote monitoring; recent ICD therapy
- Borderline: VT with structurally normal heart but clinician explicitly expresses reservations,
  or beta-blocker recently initiated

*Pre-excitation (WPW pattern):*
- For PIFU: asymptomatic pre-excitation on medication, normal LV function, no AF, EP study
  not indicated; post-ablation, symptom-free
- Not for PIFU: pre-excitation with persistent AF (WPW + AF = high-risk combination
  requiring specialist oversight); pre-ablation with pending EP study; class I antiarrhythmic
  in use
- Borderline: pending exercise test or EP study; patient currently asymptomatic but prior
  presyncope not fully explained

*Ventricular Ectopy:*
- For PIFU: benign, asymptomatic, no structural heart disease, no antiarrhythmic needed
- Not for PIFU: high ectopic burden causing LV dysfunction, symptomatic on medication not yet optimised

*Atrial Flutter (typical and atypical):*
- For PIFU: post-successful ablation, symptom-free, no recurrence, anticoagulation stable
- Not for PIFU: recurrent flutter on antiarrhythmic; pre-ablation pending; persistent
  flutter managed with rate control (→ consider discharge/GP pathway)
- Borderline: recent dose increase of rate-control medication, weekly symptoms, recent
  unplanned admission >6 months ago without confirmed restabilisation

**Universal arrhythmia exclusions:**
- Any device patient (pacemaker, ICD, CRT) without remote monitoring in place
- Newly initiated class I or III antiarrhythmic drug (amiodarone, flecainide, sotalol)
- Reversible cause not yet addressed (thyroid disease, electrolyte abnormality)
- High-risk arrhythmia without curative intervention (e.g. VT in channelopathy, Brugada,
  complete heart block without pacemaker)

#### Heart Valve Disease

**Subtype-specific rules:**

*Aortic Stenosis (AS):*
- For PIFU: mild-to-moderate AS (Vmax <4.0 m/s), asymptomatic, preserved LV function
  (EF ≥50%), stable on serial echo with no rapid progression
- Not for PIFU: severe AS (Vmax ≥4.0 m/s, mean gradient ≥40 mmHg, AVA <1.0 cm²);
  symptomatic AS; rapid progression on serial echo (Vmax increase >0.3 m/s/year is
  a surveillance warning; >0.6 m/s/year is a hard concern); awaiting TAVI/SAVR
- Borderline: Vmax 3.5–4.0 m/s (moderate-severe borderline); EF 45–50% with uncertainty

*Aortic Regurgitation (AR):*
- For PIFU: mild AR, preserved LV size and function, asymptomatic
- Not for PIFU: moderate-severe or severe AR; LV dilatation (LVESD >50mm for AR);
  EF <50% in context of AR; symptomatic; awaiting surgery

*Mitral Regurgitation (MR):*
- For PIFU: mild-to-moderate MR, preserved LV function (EF ≥60% for primary MR),
  asymptomatic, LVESD <40mm
- Not for PIFU: severe MR; EF <60% with primary MR; LVESD ≥40mm; EROA ≥0.40 cm²;
  symptomatic; surgical referral made
- Borderline: EROA 0.35–0.40 cm², LVESD 38–40mm — flag and reduce certainty

*Mitral Stenosis (MS):*
- For PIFU: mild MS, no haemodynamic compromise, asymptomatic
- Not for PIFU: moderate-severe MS; symptomatic; awaiting intervention

*Mitral Valve Prolapse (MVP):*
- For PIFU: non-severe MVP (mild-moderate MR if present), asymptomatic, preserved LV,
  no malignant arrhythmia pattern
- Not for PIFU: severe MR from MVP; MVP with complex arrhythmia (malignant MVP syndrome)

*Bicuspid Aortic Valve (BAV):*
- For PIFU: BAV with mild-moderate non-severe valve disease (AS or AR), asymptomatic,
  preserved LV, stable on serial imaging, no aortic root dilatation requiring surveillance
- Not for PIFU: severe valve disease; significant aortic root dilatation (>45mm) requiring
  timed surveillance; awaiting intervention
- Borderline: mild-moderate severity at the upper end of the range (Vmax 3.5–3.8 m/s);
  recent decompensation >6 months ago without confirmed restabilisation

*Post-Valve Intervention (surgical repair, replacement, TAVI):*
- For PIFU: fully recovered, normally functioning prosthesis (mechanical or bioprosthetic),
  stable anticoagulation (therapeutic and stable INR for warfarin; DOAC if bioprosthetic),
  preserved LV function, no complications
- Not for PIFU: LV impairment (EF <50%); NYHA III–IV post-intervention; unstable or
  subtherapeutic anticoagulation (especially mechanical valve + warfarin with variable INR);
  prosthetic valve concern (stenosis, regurgitation, thrombosis); recent intervention <3 months
- Borderline: multiple comorbidities (3+) with uncertain interaction; frailty mentioned
  but not formally assessed

**Universal valve exclusions:**
- Any moderate valve disease with symptoms (dyspnoea, syncope, chest pain)
- Severe valve disease of any type
- LV dysfunction (EF <50% for AR/MR; EF <50% post-intervention)
- Awaiting intervention (surgical or TAVI)
- Rapid echocardiographic progression (serial echo showing significant change)

---

### STEP 3 — Screen the Clinical Document

**Accepted input formats:** PDF, Word (.docx), plain text (.txt), or pasted text.
The skill reads whichever format is provided — there is no requirement to convert documents
before uploading. If multiple documents are provided for the same patient (e.g. a clinic
letter plus a discharge summary), read all of them before making a verdict.

If no document is provided, ask the user to upload or paste the clinical letter before proceeding.

Read the patient's clinical document (clinic letter, discharge summary, MDT note, or similar).

Identify:
1. **Cardiology sub-specialty and subtype** — arrhythmia (which type?) / valve disease
   (which valve, which lesion?) / heart failure (HFpEF / HFrEF / HFmrEF?) / POTS / other?
   - If NOT a cardiology document, state this clearly and stop.
2. **Diagnosis and clinical status** — primary condition, current severity, stability
3. **Current management** — medications (doses, how recently initiated), devices
   (pacemaker, ICD, CRT — is remote monitoring in place?), planned procedures
4. **Red flags** — any features that would exclude PIFU (use Step 2d subtype rules)
5. **Enabling factors** — features that support PIFU eligibility
6. **Patient capacity and activation** — documented concerns about self-management ability;
   note if traffic light symptom plan or written information has been provided
7. **Data gaps** — before reaching a verdict, explicitly check for the following. If any
   are missing, flag them in the DATA GAPS section of the output and reduce certainty %:

   | Value | Why it matters | Flag if missing for... |
   |---|---|---|
   | NYHA class | Determines HF eligibility threshold | All heart failure cases |
   | LVEF (quantified %) | Borderline 40–50% range affects classification | HF, valve disease, post-intervention |
   | Serial echo data | Rate of progression matters as much as current severity | AS, AR, MR, BAV |
   | Anticoagulation stability | Unstable INR excludes mechanical valve patients | AF, mechanical prosthesis |
   | eGFR trend | Post-ARNI drop may exclude even stable-looking HF | HFrEF/HFmrEF on ARNI |
   | Frailty assessment | Unscored frailty reduces certainty, not automatic exclusion | Any patient where frailty mentioned |
   | Patient age | Must be ≥18 for PIFU | Any letter where age not stated |
   | Remote monitoring status | ICD/pacemaker without remote = hard exclusion | All device patients |
   | Date of last hospital admission | <6 months = hard exclusion for HF | All heart failure cases |
   | Antiarrhythmic drug class | Class I/III = exclusion regardless of apparent stability | All arrhythmia cases on medication |

Then apply:
- NHS-pathway criteria (Steps 1 + 2d subtype rules) if condition is arrhythmia / valve disease / heart failure
- General SOP + POTS-specific criteria (Steps 2b and 2c) if condition is POTS
- General SOP criteria only (Step 2b) for all other cardiology conditions

**Watch for these common traps before reaching a verdict:**
- Patient feels well and is NYHA II, but biochemistry tells a different story
  (e.g. falling eGFR after ARNI initiation, rising LFTs on Amiodarone, hyperkalaemia)
- Echo looks stable but the *rate of change* between serial studies is the red flag
  (e.g. AS with Vmax increasing ≥0.3 m/s/year)
- Patient's primary condition is suitable but a co-medication requires secondary care
  monitoring (e.g. warfarin in a prosthetic valve patient with variable INR)
- Patient is functionally NYHA II but has documented non-compliance with self-monitoring
  or diuretic non-compliance causing recurrent fluid overload
- Medication is at a low/subtherapeutic dose — this is not "optimised", even if it's
  being tolerated well and no further titration is planned in this letter
- The follow-up plan is explicitly deferred ("will reassess after uptitration") —
  this is Not for PIFU until that reassessment occurs
- Clinician expresses explicit reservations about PIFU in the letter even if clinical
  criteria appear met — record this as a borderline factor and reduce certainty

---

### STEP 4 — Final Output

Produce a structured assessment:

```
PATIENT: [Name, DOB, NHS Number if available]
CONDITION: [Sub-specialty, subtype, and primary diagnosis]
DOCUMENT TYPE: [Clinic letter / Discharge summary / MDT note / Other]
PATHWAY TYPE: [NHS-defined pathway / General SOP criteria / POTS — no dedicated pathway]

DATA GAPS (if any):
  - [e.g. LVEF not quantified; formal frailty assessment not documented; NYHA class not stated]

PIFU ELIGIBILITY FACTORS:
  For PIFU:
    - [list supporting factors]
  Against PIFU:
    - [list excluding or cautionary factors]

APPLICABLE CRITERIA SOURCE:
  - [e.g. NHS Arrhythmia PIFU Guidelines + General SOP; or "General NHS PIFU SOP —
    no condition-specific pathway exists for [condition]"]

VERDICT: ✅ For PIFU / ❌ Not for PIFU / ⚠️ Uncertain [X]% / 🔄 Discharge (not PIFU)

REASONING:
  [2-4 sentences explaining the verdict with specific criteria cited. For non-pathway
  conditions, explicitly state that no dedicated NHS guideline exists. For borderline
  cases, name the specific factor(s) driving uncertainty.]

SUGGESTED PIFU TIMESCALE (if For PIFU):
  [e.g. 12 months — per NHS HF PIFU guidance / per general SOP criteria]
```

---

## Reasoning Transparency

This section explains *how and why* the skill makes decisions at each step. It is intended
to allow clinicians and supervisors to audit, challenge, and improve the workflow.

---

### What PIFU is (plain language)

Rather than booking patients into routine follow-up on a fixed schedule, PIFU lets the
*patient* decide when they need to be seen — they contact the service when something changes.
It frees up clinic slots for patients who genuinely need them and gives stable, well-informed
patients more autonomy. NHS England's target is for PIFU to be the default pathway for all
appropriate outpatients by March 2026, covering at least 5% of all outpatient appointments.

The key insight: **PIFU is not about discharging patients — it is about transferring the
initiation of follow-up from the clinician to the patient.** The clinical relationship
continues; the trigger mechanism changes.

---

### How eligibility decisions are made

The skill uses a two-layer decision process:

**Layer 1 — Condition-specific NHS criteria (Steps 1 & 2d)**
For arrhythmia, valve disease, and heart failure, NHS England has published explicit
eligibility criteria. The skill reads these and maps the patient's clinical status against
them using subtype-specific rules (Step 2d). The logic is:
- Does the patient meet the *inclusion* criteria for their specific subtype?
- Do any *exclusion* criteria apply?
- If both layers are clear → binary verdict, high confidence.

**Example (Heart Failure — HFrEF):**
- Inclusion: NYHA I–II, optimised GDMT (all four drug classes at or near target dose),
  stable renal function, no hospitalisation in past 6 months, good patient activation.
- Exclusion: Recent admission, NYHA III–IV, active medication titration, declining eGFR,
  electrolyte instability, end-of-life pathway, awaiting device therapy.
- The pattern is the same across all three NHS-pathway conditions: stable + optimised +
  informed + low-risk = For PIFU. Active + changing + complex + monitored = Not for PIFU.

**Layer 2 — Universal SOP criteria (Step 2a)**
The SOP acts as a cross-condition safety checklist applied to *every* patient regardless
of condition. Even if the clinical condition looks fine, the patient must also pass:
1. Clinical stability (no acute decompensation or pending intervention)
2. Established diagnosis (no outstanding investigations that would change management)
3. Optimised treatment (not in an active titration phase; medications at therapeutic doses)
4. No secondary care drug monitoring requirement
5. Demonstrated patient activation (understands condition, knows red flags, has a plan)
6. No device safety concern requiring timed follow-up

Failing any single criterion is sufficient to exclude PIFU — even if the patient's primary
condition would otherwise qualify. Frailty and multimorbidity are not automatic exclusions
but require careful consideration and should reduce certainty if not formally assessed.

---

### What to do when no guideline exists

For conditions without a dedicated NHS PIFU pathway (POTS, stable angina, post-MI,
cardiomyopathies), the skill:
1. Explicitly states that no condition-specific pathway exists — always disclosed in the
   output so the reader knows the verdict carries more uncertainty.
2. Falls back entirely to the six general SOP criteria above.
3. Applies a higher threshold — requires all six criteria to be clearly met, not just
   mostly met, because the absence of a guideline means there is no clinical validation
   of safety for that population.
4. Errs toward ❌ Not for PIFU in genuinely ambiguous cases.

The rationale: a false negative (failing to identify a PIFU candidate) means the patient
continues with timed follow-up — a safe default. A false positive (placing an unsuitable
patient on PIFU) could result in delayed recognition of deterioration — a patient safety risk.

---

### How the % certainty score is calculated

The certainty score is not a formula. It is a structured clinical judgement across four
dimensions, each of which shifts the score up or down:

| Dimension | Raises confidence | Lowers confidence |
|-----------|------------------|------------------|
| **Guideline fit** | Patient clearly meets published NHS inclusion criteria | Patient sits on the borderline of a criterion |
| **Exclusion flags** | Zero red flags identified | One or more amber flags present (not hard exclusions, but concerns) |
| **Information completeness** | All key data points present (EF, BNP, eGFR, valve gradient, HR increment etc.) | Key clinical values missing — cannot fully assess |
| **Pathway type** | NHS-defined condition-specific pathway used | General SOP reasoning only — more interpretive uncertainty |

**Calibration guide for supervisors:**
- **>95%** — criteria are unambiguously met or failed. No meaningful clinical disagreement expected.
- **85–95%** — strong case either way, but one minor uncertainty (e.g. a borderline value,
  or a single missing data point that would not change the overall picture).
- **70–85%** — genuine grey zone. Patient meets most criteria but one factor is uncertain
  or sits at a threshold. A senior clinician might reasonably reach a different verdict.
  The skill will always flag the specific factor driving the uncertainty.
- **<70%** — insufficient information to make a confident assessment. The output will
  explicitly list what additional clinical data would resolve the uncertainty.

**Common scenarios that push a case into borderline territory (⚠️):**
- Medication initiated but titration not yet complete — reassess after optimisation
- Recent hospital admission >6 months ago but restabilisation not explicitly confirmed
- LVEF in borderline range (40–50% for HF; 45–50% for valve disease) without clear
  stability trajectory documented in the letter
- Valve disease severity described qualitatively without quantitative echo data (Vmax,
  mean gradient, EROA, LVESD) — flag as a data gap
- Frailty mentioned but not formally scored — flag as a data gap
- Clinician explicitly expresses uncertainty or reservations about PIFU in the letter
- Multiple comorbidities (3+) whose interaction on self-management safety is not addressed
- Follow-up plan deferred ("will re-assess after uptitration") — PIFU is premature

---

### Guidance for supervisors wishing to edit this skill

**To add a new condition with dedicated NHS guidance:**
1. Add the NHS URL to Step 1 with a clear subheading.
2. Add condition-specific inclusion/exclusion criteria to `references/nhs-pifu-criteria-summary.md`.
3. Add subtype-specific rules to Step 2d under the relevant heading.
4. Add any condition-specific PIFU timescale to the output template in Step 4.

**To adjust the POTS or general SOP criteria:**
Edit Steps 2b and 2c directly. Each criterion is numbered — criteria can be added,
removed, or modified individually. If a criterion is changed from a hard exclusion to
a soft consideration (or vice versa), update the language accordingly ("must" vs "consider").

**To adjust subtype-specific decision rules:**
Edit Step 2d. Rules are organised by condition and subtype. Each rule has a "For PIFU",
"Not for PIFU", and "Borderline" section. Add, remove, or tighten criteria as clinical
experience accumulates.

**To adjust confidence thresholds:**
Edit the calibration guide in the Reasoning Transparency section above. The thresholds
are explicitly defined and can be tightened or relaxed based on clinical experience.

**To add new hard rules:**
Add them to the Hard Rules section below with a one-line rationale so future editors
understand why the rule exists.

---

## Hard Rules

- Never give a PIFU verdict for a non-cardiology patient. State the specialty mismatch.
- Always cite the criteria source. For non-pathway conditions, always state the absence
  of a dedicated guideline explicitly — never imply one exists.
- POTS must always include the "no dedicated NHS PIFU pathway" statement.
- If the document mentions the patient is already on a PIFU pathway, confirm the existing
  status rather than re-assessing from scratch.
- If key clinical information is missing (e.g. EF for heart failure, valve gradient,
  POTS HR increment, syncopal frequency, NYHA class, frailty score), flag this as a data
  gap and reduce certainty %. Do not fabricate values.
- End-of-life / palliative care pathway is an absolute hard exclusion — never recommend PIFU.
- Do not recommend PIFU for: active decompensation; recent hospitalisation <6 months
  (heart failure) or <3 months (arrhythmia post-cardioversion); planned procedures or
  pending results that would change management; newly initiated medications requiring
  monitoring; ICD with recent therapies without remote monitoring.
- Discharge to primary care is NOT the same as PIFU. If the document describes GP
  discharge (common in rate-controlled persistent AF with good LV), record this as
  🔄 Discharge — not a PIFU verdict.
- An exclusion flag alone does not mandate NOT_ELIGIBLE. If one or more exclusion criteria
  are present alongside meaningful mitigating factors or documented clinical ambiguity,
  classify as ⚠️ BORDERLINE with a certainty score and explicit reasoning. Reserve
  NOT_ELIGIBLE for cases where the exclusion is unambiguous and leaves no clinical doubt.
- If uncertain between NOT_ELIGIBLE and BORDERLINE, prefer BORDERLINE — it prompts
  clinician review rather than automatic exclusion. If uncertain between BORDERLINE and
  ELIGIBLE, prefer BORDERLINE.
- Discharge-to-GP cases output 🔄 Discharge (not PIFU), which maps to NOT_ELIGIBLE.
- If uncertain between BORDERLINE and NOT_ELIGIBLE, err toward NOT_ELIGIBLE — a false
  negative (missed PIFU candidate) is safer than a false positive (unsafe patient on PIFU).
- Never interpret low/subtherapeutic medication doses as "optimised". Optimisation means
  the patient is at or approaching guideline-directed target doses, or has a documented
  clinical reason for remaining at a lower dose (e.g. bradycardia limiting beta-blocker
  uptitration).
- If the clinician's own letter expresses doubt about PIFU suitability, do not override
  it with an ELIGIBLE verdict — flag as borderline and note the clinician's concern.
