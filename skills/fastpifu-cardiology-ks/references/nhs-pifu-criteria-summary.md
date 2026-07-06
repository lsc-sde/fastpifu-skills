# NHS PIFU Eligibility Criteria — Cardiology Summary

<!-- concept_ids: (completed by data team) -->
<!-- author: Karthik | reviewed_by: (pending clinical review) | last_updated: 2026-07-02 -->

This file is a pre-compiled reference for use when NHS web pages are unavailable.
Always prefer live web-fetched content over this summary, as guidelines may be updated.

---

## What is PIFU?

Patient-Initiated Follow-Up (PIFU) allows patients to self-initiate follow-up appointments
when their symptoms or circumstances change, rather than attending routine scheduled
outpatient appointments. It is appropriate for patients who are clinically stable, understand
their condition, and can reliably self-monitor and contact the service when needed.

NHS England asks all trusts to ensure PIFU is offered as standard in all appropriate pathways
by March 2026, targeting at least 5% of all outpatient appointments.

**PIFU is not discharge.** The specialist relationship continues — only the trigger mechanism
changes from clinician-initiated to patient-initiated. If a letter describes handing the
patient entirely back to GP with no ongoing specialist role, that is a discharge, not PIFU.

---

## Arrhythmia PIFU — Eligibility Criteria

**Source:** NHS England — Setting up PIFU services for people with arrhythmia

### Likely SUITABLE for PIFU:

**Paroxysmal AF (PAF):**
- Asymptomatic or minimally symptomatic, rate/rhythm controlled
- No class I/III antiarrhythmic drug requirement
- No recent cardioversion (<3 months)
- Stable anticoagulation (well-controlled warfarin or DOAC)
- No structural heart disease

**SVT (AVNRT, AVRT):**
- Post-successful ablation, symptom-free ≥3 months, no antiarrhythmic needed
- Or medically managed with stable, well-tolerated medication and infrequent episodes

**Ventricular Ectopy** (NHS-sourced, three distinct scenarios — not a flat rule):
- Asymptomatic, high burden, normal LV function: repeat echo at 1 year, then discharge if
  no clinical concerns (timed re-check, not PIFU)
- Previously impaired LV, successfully ablated: 2-year timed follow-up, then discharge if
  LV function has fully recovered
- Symptomatic, treated with ablation, beta-blocker, OR calcium channel blocker: PIFU,
  time-limited, at physician's discretion (CCB is explicitly NHS-sourced alongside
  beta-blocker — not beta-blocker alone)

**Other Arrhythmias** (inappropriate sinus tachycardia, low-burden supraventricular
ectopy) — NHS-sourced, verbatim: "Discharge where appropriate but may be suitable for
PIFU at clinician's discretion." Do not apply the elevated non-pathway six-criteria bar
to this category.

**VT in structurally normal heart:**
- Successful ablation, asymptomatic, preserved LV function, no ICD, medications stable

**Atrial Flutter (typical and atypical):**
- Post-successful ablation, symptom-free, no recurrence, anticoagulation stable

**Pre-excitation (WPW pattern):**
- Pre-excitation managed without EPS — NHS source: "Consider LONG-TERM PIFU with the
  option of periodic outpatient review." When MDT/electrophysiologist has explicitly
  assessed and determined no EP study is required, PIFU is appropriate.
- Or post-ablation, symptom-free ≥3 months

**Device patients:**
- Stable pacemaker patients with remote monitoring in place
- ILR patients being monitored remotely

### NOT suitable for PIFU (require timed follow-up):

**Universal arrhythmia exclusions — CORRECTED (2 July 2026):** the NHS arrhythmia document
DOES have a verbatim universal "General Inclusion and Exclusion Criteria" section (an
earlier pass on this same date wrongly said it didn't). Verbatim exclusion: "Patients with
outstanding investigations or decisions still to be made regarding further options for
care." "Cannot easily contact the service." "Low level of knowledge, skills and confidence
to manage their follow-up care and/or no carer support." Verbatim inclusion: age 18+,
patient/carer understands and feels confident, patient stable with medicines optimised.
Per the same disclosed policy as valve/HF, Step 2a treats the "contact the service" and
"knowledge/skills/confidence/carer support" items as BORDERLINE-capable, not hard
exclusions — intentional, not an oversight. The bullets below are a DIFFERENT list —
mostly per-subtype synthesis, not the verbatim universal list above; "ICD without remote
monitoring" is NOT actually traceable to the source's CRM Devices section (corrected this
pass — that section only mentions remote monitoring as a review tool, not a PIFU
precondition); "reversible cause" and "high-risk arrhythmia without curative intervention/
complete heart block" remain supplementary, not NHS-sourced. See `condition-rules.md` for
full detail:
- Newly initiated class I or III antiarrhythmic drug (amiodarone, flecainide, sotalol) —
  genuinely subtype-verbatim (PAF/persistent AF sections)
- ICD patients without remote monitoring in place — supplementary, not NHS-sourced
- Recent cardioversion (<3 months)
- Symptomatic arrhythmia with functional limitation (NYHA III–IV equivalent)
- Complex device patients (CRT-D) with frequent therapies or recent shocks
- Reversible cause not yet addressed (thyroid disease, electrolyte abnormality) —
  supplementary, not NHS-sourced
- High-risk arrhythmias without curative intervention (VT in channelopathy, Brugada,
  complete heart block without pacemaker) — supplementary, not NHS-sourced (the
  channelopathy/Brugada long-term-follow-up requirement itself IS NHS-sourced elsewhere)

**Subtype-specific exclusions:**
- PAF or persistent AF on class I/III antiarrhythmic → long-term follow-up or GP shared care
- Persistent AF, rate-controlled, good LV function → Discharge to GP (not PIFU)
- Pre-excitation where formal specialist risk assessment has NOT been completed (EP study
  outstanding/undecided) → NOT_ELIGIBLE. Pre-excitation with AF where MDT has assessed
  and decided no EP study required → ELIGIBLE or BORDERLINE (not automatic NOT_ELIGIBLE)
- VT in non-ischaemic cardiomyopathy → inherited cardiomyopathy pathway, not PIFU
- VT in inherited channelopathy (LQT, Brugada) → specialist long-term follow-up required
- Ischaemic cardiomyopathy, once optimised (medically or with ablation), regardless of
  device status → NOT suitable for PIFU, shared care with HF team + device team + GP
- Non-ischaemic cardiomyopathy or inherited channelopathy AS A PRIMARY DIAGNOSIS (not only
  in the VT context) → long-term specialist follow-up required; never PIFU or general
  discharge, regardless of current stability
- Medically-managed VT in a structurally normal heart → consider TIMED PIFU for 3 years
  (this is ELIGIBLE, not an exclusion — listed here for completeness alongside the
  ablated-VT rule above)
- Pre-ablation SVT where ablation is already scheduled and imminent → NOT_ELIGIBLE;
  ablation only being discussed/considered → BORDERLINE (not NOT_ELIGIBLE)

### Discharge-to-GP scenarios (not PIFU):
- Asymptomatic PAF with no structural disease and no ongoing intervention needed
- Persistent AF rate-controlled with good LV function (EF ≥50%), asymptomatic
- PAF or persistent AF treated with AV node ablation + pacemaker: echocardiogram at
  3–6 months, then discharged to follow-up at pacing clinic (and HF clinic if appropriate)
  — NOT PIFU, and NOT ongoing general cardiology follow-up
- Typical atrial flutter, symptom-free and in sinus rhythm (or stable well-controlled
  flutter) with stable LV function, at 3–6 months
- Atypical atrial flutter / atrial tachycardia, successfully treated, after 6 months →
  discharge or referral back to originating team

> **⚠️ Scope note:** The PAF, persistent AF, and typical-flutter DISCHARGE rules above
> apply exclusively to those specific subtypes. Atypical atrial flutter and atrial
> tachycardia (AT) are distinct — clinician-stated discharge of atypical flutter/AT to GP
> without completed ablation/successful treatment documented = ❌ NOT_ELIGIBLE, not
> 🔄 Discharge.

---

## Valve Disease PIFU — Eligibility Criteria

**Source:** NHS England — Guide to implementing PIFU: imaging in mild-to-moderate heart valve disease

### Likely SUITABLE for PIFU:

**Aortic Stenosis (AS):**
- NHS-sourced cutoff (verbatim): "low to moderate aortic stenosis (Vmax <3.5 m/s with
  preserved left ventricular function)." This is the actual PIFU-suitability threshold —
  do NOT use the general cardiology "severe AS" threshold (Vmax ≥4.0 m/s) as the entry
  cutoff for this pathway; the NHS PIFU threshold is more conservative.
- Vmax <3.5 m/s, preserved LV function, normal flow, asymptomatic
- Stable on serial echo — leave-PIFU trigger is Vmax >3.5 m/s or AVA <1.2cm² (NHS-sourced).
  Rate-of-progression figures (e.g. "0.3 m/s/year") are a supplementary clinical heuristic,
  not NHS-stated.

**Aortic Regurgitation (AR)** — imaging surveillance interval: 1–2 years.
- Mild-to-moderate AR, preserved LV size and function, asymptomatic
- NHS-sourced leave-trigger: aortic root dimension ≥40mm (not LV chamber size), left
  ventricular dilatation (unquantified), progression to severe AR, PA pressure >50mmHg.
  No LVESD number is given in the source — any specific LVESD threshold is a supplementary
  clinical heuristic, not NHS-sourced.

**Mitral Regurgitation (MR)** — imaging surveillance interval: 18 months – 2 years.
- Mild-to-moderate MR, preserved LV function (LVEF ≥55%, PA pressure <50mmHg), asymptomatic
- Note: the NHS source entry criterion is "preserved LVEF, PA pressure <50mmHg" with no
  hard % cutoff. "Leave PIFU if LVEF <60%" is a surveillance EXIT trigger, not an entry
  exclusion. LVEF 55–59% = BORDERLINE (not NOT_ELIGIBLE). The NHS source gives no LVESD or
  EROA number for MR at all — LVESD/EROA bands are supplementary clinical heuristics, not
  NHS-sourced, and should be treated as softer signals than LVEF/PA pressure.

**Mitral Stenosis (MS)** — imaging surveillance interval: 2–3 years.
- Mild MS (MVA >1.5cm², NHS-sourced verbatim), no haemodynamic compromise, asymptomatic

**Mitral Valve Prolapse (MVP)** — imaging surveillance interval: 3–5 years (no/mild MR);
follow the MR interval (18mo–2yr) instead if moderate MR is present.
- Non-severe MVP (mild-moderate MR if present), asymptomatic, preserved LV
- No malignant arrhythmia pattern

**Bicuspid Aortic Valve (BAV)** — imaging surveillance interval: 2–5 years (12 months if
aortic dilatation >40mm).
- Mild-moderate non-severe valve disease, asymptomatic, preserved LV
- Stable on serial imaging, no significant aortic root dilatation requiring surveillance
- **NHS-sourced imaging-adequacy caveat (verbatim):** "If echocardiogram cannot assess
  aortopathy alone, patient is NOT suitable for PIFU." Distinct from the root-size
  triggers — this is about whether echo can adequately visualise the aortic root at all,
  not whether the root is dilated. Not a data gap/BORDERLINE trigger — the source states
  this as a firm exclusion. See `condition-rules.md` for full detail.

**Post-Valve Intervention — TAVI, Bioprosthetic Valve, Mitral Repair, TEER** — imaging
surveillance interval: 1–2 years.
- Fully recovered, normally functioning prosthesis confirmed on post-operative TTE
- Post-op TTE must be performed before PIFU begins (no timing restriction — if TTE done
  and normal, PIFU is appropriate regardless of time since procedure)
- Stable anticoagulation (therapeutic INR for warfarin; DOAC for bioprosthetic)
- Preserved LV function (EF ≥50%), no complications, no ongoing specialist need

**Post-Valve Intervention — Mechanical Valve Prosthesis (distinct NHS pathway, no
associated aortopathy):**
- NHS-sourced, verbatim: "No imaging follow-up required" at all — NOT the same 1–2 year
  interval as bioprosthetic/TAVI/TEER/repair above. Only precondition is the same
  post-operative TTE before entering PIFU.
- NHS-sourced caveat, verbatim: "Patients with bicuspid aortic valve or co-existent
  untreated valve lesions may not be suitable for PIFU." "Consider TTE at 5 years in
  isolated mechanical MVR to assess right heart and for tricuspid regurgitation."
- Suitable: isolated mechanical prosthesis, no associated aortopathy, no co-existent BAV
  or untreated lesion, post-op TTE performed and normal, stable anticoagulation.
- Not suitable: co-existent BAV or untreated valve lesion; no post-op TTE performed;
  unstable/subtherapeutic anticoagulation.

### NOT suitable for PIFU (require timed follow-up):
(Source fidelity: unlike arrhythmia, the NHS valve source DOES have a verbatim universal
"NOT Suitable for Heart Valve PIFU" list — severe disease, symptomatic disease, LV
impairment, outstanding investigations/decisions, complex HVD needing regular review, low
health literacy/confidence, difficulty contacting the service, unsuitable-for-intervention
patients who should be discharged. The specific "EF <50%" number and "rapid echo
progression" framing below are supplementary — the source itself only says "LEFT
VENTRICULAR IMPAIRMENT" unquantified and has no universal echo-progression criterion. See
`condition-rules.md` for the full verbatim quote.)
- Severe valve disease of any type
- Moderate valve disease with symptoms (dyspnoea, syncope, chest pain)
- AS: Vmax >3.5 m/s or AVA <1.2cm² (NHS-sourced leave-trigger — this is the operative
  cutoff, not the general "severe AS" 4.0 m/s definition)
- AR: aortic root ≥40mm (NHS-sourced); LV dysfunction EF <50%
- MR: EF <55%; PA pressure >50mmHg; new/worsening LV or RV dysfunction
- MS: mitral valve area <1.5cm² (NHS-sourced, verbatim)
- LV dysfunction: EF <50% for AR/MR; EF <50% post-intervention
- Awaiting valve intervention (surgical or TAVI)
- Unstable or subtherapeutic anticoagulation (especially mechanical valve + warfarin)
- Prosthetic valve concerns (stenosis, regurgitation, thrombosis); post-intervention
  gradient increase ≥10mmHg vs previous echo (NHS-sourced leave-trigger)
- BAV: "significant" aortic root dilatation — the NHS source gives no exact number for the
  leave-trigger itself (only that 12-month surveillance starts >40mm); ~45mm is a
  supplementary clinical reference point for "significant," not an NHS-stated cutoff

**Borderline — flag with uncertainty %:**
- AS: Vmax approaching 3.5 m/s with genuine reading ambiguity; AVA close to 1.2cm²
- BAV: aortic root 40–45mm where "significant" is not clearly established
- MR: LVEF 55–59%; LVESD/EROA bands if reported are supplementary heuristics only
- EF 45–50% without clear stability trajectory
- Recent decompensation >6 months ago, restabilisation not confirmed

### Discharge-to-GP scenarios (not PIFU):
- Mild stable valve disease explicitly handed to GP with no further imaging surveillance planned
- Bicuspid AV with no significant haemodynamic lesion, no aortic root concern, explicitly discharged
- Post-valve intervention fully recovered with no ongoing specialist need documented
- Clinician has deemed the patient unsuitable for valvular intervention due to frailty or
  multiple co-morbidities, with no valve-specific surveillance plan documented — NHS-sourced
  verbatim: "these should be discharged back to their GP." Distinct from ordinary severe/
  symptomatic valve disease (otherwise NOT_ELIGIBLE) — this is specifically a documented
  clinician decision against intervention on frailty/comorbidity grounds.

---

## Heart Failure PIFU — Eligibility Criteria

**Source:** NHS England — Setting up PIFU services for people with heart failure

**Source fidelity note:** the NHS document only states patients must be "stable" with
"medicines optimised," and excludes outstanding investigations/decisions, device-therapy
candidates awaiting diagnostics, "uncontrolled symptoms," and end-of-life pathway — no
numeric eGFR/K+/titration-window/drug-class detail is given. The specific numbers below are
supplementary clinical judgement (general HF management guidance), not literally NHS-sourced.

**Disclosed policy choice:** the source also lists "unable to contact the service" and "low
knowledge/skills/confidence and/or no carer support" under its own "NOT Suitable" list (same
pattern as the valve disease source). Step 2a deliberately treats these as BORDERLINE-capable
"careful consideration" factors rather than hard exclusions, for the same reason given under
Valve Disease below — this is intentional, not a missed source detail.

### Likely SUITABLE for PIFU (HFpEF / HFrEF / HFmrEF):
- Clinically stable, NYHA Class I–II. The NHS source requires "stable" — this does not
  mandate a specific admission-free window; a single past admission that has resolved
  does not automatically disqualify if stability is established.
- Optimised GDMT:
  - HFrEF: all four drug classes (ACEI/ARB/ARNI, beta-blocker, MRA, SGLT2i) at or
    approaching target doses
  - HFmrEF: ACEi/ARB/ARNI, beta-blocker, MRA at or approaching target doses; SGLT2i
    if prescribed but absence ALONE does NOT constitute "not optimised" — flag as data
    gap, do NOT downgrade ELIGIBLE to BORDERLINE solely on SGLT2i absence in HFmrEF
  - HFpEF: diuretic optimised, SGLT2i if clinically indicated
  - Medications at low/sub-therapeutic doses that haven't been uptitrated = NOT optimised
- No active medication titration or recently initiated agent (<8–12 weeks)
- Stable renal function (eGFR trend not declining)
- No electrolyte instability
- Evidence of patient self-monitoring (weight diary, fluid balance, traffic light plan)

### NOT suitable for PIFU (require timed follow-up):
- NYHA Class III–IV (even if partially treated)
- Active decompensation, or multiple admissions indicating pattern of instability.
  Single recent admission with positive trajectory = BORDERLINE, not hard NOT_ELIGIBLE.
- End-of-life / palliative care pathway (absolute hard exclusion)
- Awaiting device therapy (CRT, ICD) or cardiac resynchronisation
- Key medication wholly unoptimised or major drug class just initiated (<8 weeks) with
  no established response. Minor gaps (e.g. SGLT2i not started in HFmrEF) = BORDERLINE.
- eGFR <30 or actively declining after recent medication change
- Significant electrolyte abnormality (K+ >5.5 or actively rising)
- Outstanding investigation or decision regarding device therapy, surgery, or major
  management intervention

### Borderline — flag with uncertainty %:
- Single recent unplanned admission but patient now clearly restabilising and improving
- Recent medication change (<12 weeks) but otherwise stable
- LVEF in borderline range (40–50%) without clear documented stability trajectory
- Recent admission >6 months ago but restabilisation not explicitly confirmed
- Diuretic use unclear (PRN vs regular) — not optimised if not on a fixed regimen
- NYHA class not formally documented — flag as data gap
- Multiple comorbidities (3+) with uncertain interactions
- Medication partially optimised (one drug class missing) but patient otherwise stable

---

## Chest Pain / Stable Angina / Post-MI — GIRFT Pathway (not a true non-pathway condition)

**Source:** GIRFT Outpatient Operational Guide, Module 2 — Cardiology, Chest Pain

This condition has explicit GIRFT operational guidance and should NOT be treated with the
elevated "all six general SOP criteria must be clearly met" bar reserved for POTS/
cardiomyopathy. GIRFT: "PIFU should be used where appropriate, particularly where symptoms
require reassessment — nurse-led PIFU/SPoA, ideally limited to 6-12 months." Post-PCI
outcomes "can be assessed virtually." Medication review "should not require face-to-face
discussion."

- **Suitable for PIFU:** stable angina with optimised secondary prevention and no further
  invasive workup planned; post-PCI with stable/resolved symptoms; post-MI fully
  investigated with secondary prevention established.
- **Not suitable:** ACS/unstable angina or any presentation still being actively worked up
  (troponin/imaging/angiogram decision pending); high-risk features awaiting MDT or
  invasive investigation; anti-anginal medication just initiated, response not yet known.
- **Timescale:** 6–12 months per GIRFT.

See `references/condition-rules.md` for full detail.

---

## General SOP Eligibility Conditions (applicable to all specialties)

### Factors SUPPORTING PIFU:
- Patient is clinically stable with no pending interventions
- Patient understands their condition and can recognise warning symptoms
- Patient has the confidence, ability, and tools to self-monitor
- Patient can contact the service easily (phone, digital)
- Patient has agreed to and understands the PIFU pathway
- Written information on red flag symptoms provided

### Factors requiring CAREFUL CONSIDERATION (not automatic exclusion):
- Complex or multiple comorbidities (3+) with uncertain interactions
- Medicines requiring regular secondary care monitoring
- Low health literacy or low patient activation
- Difficulty contacting the service
- Safeguarding concerns
- Mild/unformalised cognitive concerns or significant frailty (flag if not formally assessed)

### Absolute EXCLUSIONS from PIFU:
(Source fidelity: "end-of-life or palliative care pathway" is explicitly NHS-sourced only
in the heart failure document ("managed on an END-OF-LIFE care pathway") — it does not
appear in the arrhythmia document, the valve document, or the generic SOP template's own
"careful consideration"/inclusion lists. Extending it as a universal hard exclusion across
all conditions is a reasonable, clinically uncontroversial extension, but it should not be
presented as if explicitly NHS-sourced for arrhythmia/valve/general-SOP patients.)
- Active decompensation or acute illness
- End-of-life or palliative care pathway
- Pending investigations or procedures that will directly determine whether to intervene
  or initiate device therapy (routine surveillance imaging = BORDERLINE, not exclusion)
- Recently initiated medication requiring active secondary care monitoring
- Patient unable or unwilling to take responsibility for self-initiated care — NHS-sourced
  examples: rapidly progressing dementia, severe memory loss, severe learning disability.
  A documented willing/capable carer (or administrative booking support from a care home/GP
  surgery) mitigates this; if no such support is documented, this is NOT_ELIGIBLE, not
  BORDERLINE.

### Key data gaps that reduce certainty (flag these explicitly):
- NYHA class not formally documented
- LVEF not quantified (qualitative description only)
- Formal frailty assessment not performed or not documented
- Patient age not stated
- Anticoagulation stability not documented (for valve/AF patients)
- Serial echo data not available (cannot assess rate of progression)

> **Critical decision rule:** Data gaps produce **BORDERLINE**, not NOT_ELIGIBLE. A missing piece of information means uncertainty — it is NOT evidence of an exclusion criterion being met. NOT_ELIGIBLE requires a clearly and positively met exclusion. Patient age not stated → BORDERLINE (assume adult). Medication optimisation unclear → BORDERLINE. Follow-up plan undetermined → BORDERLINE. Clinical stability not documented → BORDERLINE. Absent information ≠ information of absence.
