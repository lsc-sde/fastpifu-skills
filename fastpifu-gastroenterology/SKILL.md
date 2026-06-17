---
name: fastpifu-gastroenterology
description: >
  Assess a gastroenterology patient for PIFU (Patient-Initiated Follow-Up) suitability from their
  clinical documents (clinic letters, discharge summaries, MDT notes, operation notes) and return
  one of four dispositions — PIFU, RETAIN_FOLLOW_UP, DISCHARGE, or INSUFFICIENT_DATA — with a
  confidence score and explicit reasoning. Use this whenever you need to screen a gastroenterology
  patient for PIFU, decide whether a patient can move to patient-initiated follow-up, be
  discharged, or must stay in timed follow-up, or process a gastroenterology clinic/operation letter
  for follow-up disposition. Covers stable cirrhosis, hyperferritinaemia/haemochromatosis, hepatitis B, auto-immune liver disease, MASLD, alcohol-related liver disease, inflammatory bowel disease and iron-deficiency anaemia. Reach for this skill even when the request
  doesn't say "PIFU" explicitly but asks what should happen next with a gastroenterology patient's
  follow-up.
---

# FastPIFU — Gastroenterology

This skill decides what should happen next with a gastroenterology patient who is **already in
outpatient or post-procedure follow-up**. It loads the relevant clinical criteria, screens the
patient's documents against them, applies a universal safety checklist, and returns a single
structured disposition with a confidence score.

The clinical detail for each condition lives in `references/` and is loaded only when needed — this
file holds the workflow, the routing, and the cross-condition logic that applies to every patient.

## The four dispositions

Every assessment resolves to exactly one of these:

- **PIFU** — the specialist relationship continues, but the patient self-initiates contact when
  something changes rather than being booked routinely. The clinician stays responsible; only the
  trigger shifts to the patient.
- **RETAIN_FOLLOW_UP** — the specialist relationship continues, but follow-up must be *timed and
  scheduled by the clinician* (e.g. a planned post-operative review, surveillance imaging, an
  unstable or high-risk patient not yet safe to self-initiate).
- **DISCHARGE** — no ongoing specialist follow-up is needed at all; the patient returns fully to GP
  / primary care and the specialist episode is complete.
- **INSUFFICIENT_DATA** — the documents do not contain enough to evaluate the criteria safely. A
  real outcome, not a failure: it flags the case for clinician review rather than forcing a guess.

**PIFU is not discharge.** If a letter hands the patient entirely back to GP with no ongoing
specialist role, that is DISCHARGE — however stable the patient looks.

## The safety asymmetry (the single most important rule)

The errors are not symmetric. Leaving a suitable patient in timed follow-up is safe. Placing an
unsuitable patient on PIFU, or discharging them, risks delayed recognition of deterioration.

> **Missing or ambiguous information can only ever push the disposition toward the safer option
> (RETAIN_FOLLOW_UP), never toward PIFU or DISCHARGE.**

A genuine borderline case resolves to RETAIN_FOLLOW_UP. When you cannot confirm a criterion, retain
rather than wave through. When key data is absent, return INSUFFICIENT_DATA.

## Discharge-first principle (GIRFT)

Identifying patients who can be safely **discharged** matters more than finding PIFU candidates — it
is what creates clinic capacity. The first question for every patient is: *can this patient be
discharged entirely?* Only if no does the PIFU-vs-timed question apply.

## Workflow

All clinical criteria this skill needs are bundled in its `references/` folder. The skill runs
**fully offline** and never fetches anything at run time. The reference files are the single source
of truth; the published guidance each is drawn from is named in that file's *Source* section for
provenance and audit, not retrieved live.

### Step 1 — Read the patient's document(s)

Read whatever is provided (PDF, Word, plain text). If several documents describe the same patient,
read all first. If none is provided, ask for the letter. Confirm this is a gastroenterology document;
if not, state the mismatch and stop. Identify the condition/procedure and subtype, the clinical
status, current management and post-operative course, features that exclude PIFU, features that
support it, and any documented concern about the patient's capacity to self-manage.

### Step 2 — Route to the condition reference and apply it

Match the condition to its reference file and read it. Each is organised under the same four
disposition headings.

| Condition | Reference file |
|---|---|
| Stable cirrhosis | `references/stable-cirrhosis.md` |
| Hyperferritinaemia / haemochromatosis (HH) | `references/hyperferritinaemia-haemochromatosis.md` |
| Hepatitis B | `references/hepatitis-b.md` |
| Auto-immune liver disease | `references/autoimmune-liver-disease.md` |
| MASLD (metabolic dysfunction-associated steatotic liver disease) | `references/masld.md` |
| Alcohol-related liver disease (ArLD) | `references/alcohol-related-liver-disease.md` |
| Inflammatory bowel disease (IBD) | `references/ibd.md` |
| Iron deficiency anaemia (IDA) | `references/iron-deficiency-anaemia.md` |

For conditions with no dedicated pathway, state that explicitly and require the universal SOP
checklist to be clearly met.

### Step 3 — Apply the universal SOP checklist (every patient)

Independent of condition, the patient must also pass this cross-condition safety checklist. Failing
any single item excludes PIFU even when the condition would otherwise qualify.

1. **Clinically stable** — no active decompensation, acute illness, or pending intervention.
2. **Diagnosis/procedure complete** — no outstanding investigations or staged treatment that would
   change management.
3. **Treatment optimised / recovery on track** — not in an active titration phase, and any expected
   post-operative milestones are being met.
4. **No secondary-care monitoring requirement** that mandates scheduled specialist review.
5. **Patient activation** — documented evidence they understand the condition, know their red-flag
   ("traffic-light") symptoms, can self-monitor, and can contact the service.
6. **No safety concern** (device, implant, high-risk histology, complication) requiring timed review.

Patient must be ≥ 18 for an adult PIFU pathway (note paediatric exceptions in the relevant file).
Frailty and multimorbidity are not automatic exclusions but reduce confidence; flag frailty as a
data gap if mentioned without a formal score.

### Step 4 — Check for data gaps before deciding

If any data point the condition file lists as required is absent, you cannot fully assess the
criterion that depends on it. Minor gaps lower confidence; gaps that block the central disposition
return **INSUFFICIENT_DATA** with a list of exactly what is needed. Never fabricate a value.

Common traps for gastroenterology:
- A chronic liver patient who 'feels well' but is due surveillance (6-monthly USS/AFP, fibrosis re-assessment) — surveillance is independent of clinic and must continue.
- Any patient found to be cirrhotic on assessment — moves to the stable-cirrhosis surveillance pathway regardless of how they present.
- A stable patient who lacks a safe/robust remote-monitoring or DNA-tracking system — without it, PIFU/remote monitoring is not safe.
- A clinician who voices reservations about PIFU even though the criteria appear met — do not
  override their concern.

## Output

```
PATIENT: [Name, DOB, NHS number if available]
CONDITION: [Condition/procedure, subtype, primary diagnosis]
DOCUMENT TYPE: [Clinic letter / Discharge summary / Operation note / MDT note / Other]
PATHWAY TYPE: [Guide pathway / General SOP — no dedicated pathway for this condition]

DISPOSITION: PIFU | RETAIN_FOLLOW_UP | DISCHARGE | INSUFFICIENT_DATA
CONFIDENCE: [0–100%]

SUPPORTING FACTORS:
  - [factors favouring the disposition, with specific findings cited]
AGAINST / CAUTIONARY FACTORS:
  - [exclusions or concerns, with specific findings cited]

DATA GAPS (if any):
  - [missing values and which criterion each blocks]

CRITERIA SOURCE:
  - [the pathway/guideline named in the condition file + universal SOP]

REASONING:
  [2–4 sentences citing the specific criteria. For low-confidence cases, name the driving factor and
  confirm the disposition resolved to the safer option.]

PIFU REVIEW INTERVAL (only if DISPOSITION = PIFU):
  [the review/surveillance interval from the condition file]
```

### Confidence calibration

Structured judgement across four dimensions: **guideline fit**, **exclusion flags**, **information
completeness**, **pathway type** (dedicated pathway ↑ / general SOP only ↓).
- **> 95%** unambiguous; **85–95%** strong with one minor uncertainty; **70–85%** genuine grey zone
  (name the factor; resolve to the safer option); **< 70%** usually INSUFFICIENT_DATA.

## Hard rules

- Never give a PIFU disposition for a patient outside this specialty; state the mismatch.
- Always cite the criteria source. For non-pathway conditions, state explicitly that no dedicated
  guideline exists — never imply one does.
- End-of-life / palliative care pathway is an absolute exclusion — never PIFU.
- Do not recommend PIFU where there is active decompensation, a planned procedure or pending result
  that would change management, incomplete recovery, or a newly initiated treatment requiring
  monitoring.
- If the patient is already on a PIFU pathway, confirm the existing status rather than re-assessing.
- If key clinical data is missing, flag it and lower confidence or return INSUFFICIENT_DATA; never
  fabricate values.
- Do not override a clinician's own documented reservation about PIFU with a PIFU disposition.
- Apply the safety asymmetry without exception: ambiguity resolves to RETAIN_FOLLOW_UP.

**Gastroenterology-specific hard rules:**
- PIFU/remote monitoring for chronic liver disease is only safe where a robust surveillance and DNA-tracking system exists — rationale: surveillance results, not clinic attendance, drive escalation.
- Any patient shown to be cirrhotic enters the stable-cirrhosis surveillance pathway — rationale: HCC and portal-hypertension risk require mandated surveillance.

---

## For clinicians maintaining this skill

You only ever edit files in `references/`. To add or update a condition, start from the shared
condition template in the project's `_authoring/` folder, fill in every section, and place your file
here. Each criterion keeps its "supported when" clause — that is what lets the system act on it
reliably. Tell the data-science team so they can add it to the routing table and map OMOP codes.
Every change is version-controlled and clinically signed off before deployment; keep the
`author` / `reviewed_by` / `last_updated` line current.
