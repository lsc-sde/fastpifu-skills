---
name: fastpifu-cardiology
description: >
  Assess a cardiology patient for PIFU (Patient-Initiated Follow-Up) suitability from their
  clinical documents (clinic letters, discharge summaries, MDT notes) and return one of four
  dispositions — PIFU, RETAIN_FOLLOW_UP, DISCHARGE, or INSUFFICIENT_DATA — with a confidence
  score and explicit reasoning. Use this whenever you need to screen a cardiology patient for
  PIFU, decide whether a patient can move to patient-initiated follow-up, be discharged, or
  must stay in timed follow-up, or process a cardiology clinic letter for follow-up disposition.
  Covers arrhythmia, heart valve disease, heart failure, POTS, and any other cardiology
  condition via general SOP reasoning. Reach for this skill even when the request doesn't say
  "PIFU" explicitly but asks what should happen next with a cardiology patient's follow-up.
---

# FastPIFU — Cardiology

This skill decides what should happen next with a cardiology patient who is **already in
outpatient follow-up**. It loads the relevant clinical criteria, screens the patient's
documents against them, applies a universal safety checklist, and returns a single structured
disposition with a confidence score.

The clinical detail for each condition lives in `references/` and is loaded only when needed —
this file holds the workflow, the routing, and the cross-condition logic that applies to
every patient regardless of diagnosis.

## The four dispositions

Every assessment resolves to exactly one of these:

- **PIFU** — the specialist relationship continues, but the patient self-initiates contact
  when something changes rather than being booked routinely. The clinician stays responsible;
  only the trigger shifts to the patient.
- **RETAIN_FOLLOW_UP** — the specialist relationship continues, but follow-up must be *timed
  and scheduled by the clinician*. The patient is not stable or informed enough to self-initiate
  safely (e.g. NYHA III, recent admission, medication being uptitrated, pending investigations).
- **DISCHARGE** — no ongoing specialist follow-up is needed at all; the patient returns fully to
  GP care and the specialist episode is complete.
- **INSUFFICIENT_DATA** — the documents do not contain enough to evaluate the criteria safely.
  This is a real outcome, not a failure: it flags the case for clinician review rather than
  forcing a guess.

**PIFU is not discharge.** If a letter hands the patient entirely back to GP with no ongoing
specialist role ("no further follow-up required", "discharged to your care", "no further
specialist input needed"), that is DISCHARGE — however stable the patient looks.

## The safety asymmetry (the single most important rule)

The errors are not symmetric. Leaving a suitable patient in timed follow-up is safe — they keep
their appointments. Placing an unsuitable patient on PIFU, or discharging them, risks delayed
recognition of deterioration. Therefore:

> **Missing or ambiguous information can only ever push the disposition toward the safer
> option (RETAIN_FOLLOW_UP), never toward PIFU or DISCHARGE.**

Concretely: a genuine borderline case resolves to RETAIN_FOLLOW_UP, not PIFU. When you cannot
confirm a criterion, that is a reason to retain, not to wave through. When key data is absent,
return INSUFFICIENT_DATA rather than assuming the favourable reading.

## Discharge-first principle (GIRFT)

Identifying patients who can be safely **discharged** matters more than finding PIFU candidates —
it is what creates clinic capacity. So the first question for every patient is always: *can this
patient be discharged entirely?* Only if no does the PIFU-vs-timed question apply. A clean-looking
letter (no flags, no borderline reasons) that describes handing the patient back to GP is a
DISCHARGE, never a PIFU.

## Workflow

All clinical criteria this skill needs are bundled in its `references/` folder. The skill runs
**fully offline** and never fetches anything at run time. The reference files are the single
source of truth; the published guidance each is drawn from is named in that file's *Source*
section for provenance and audit, not retrieved live.

### Step 1 — Read the patient's document(s)

Accepted formats: PDF, Word (.docx), plain text, or pasted text — read whatever is provided.
If several documents describe the same patient (e.g. clinic letter + discharge summary), read
all of them first. If none is provided, ask for the letter before proceeding.

Confirm this is a cardiology document. If it is not, state the specialty mismatch and stop.

Then identify: the sub-specialty and **subtype**; diagnosis and clinical status; current
management (drugs with doses and how recently started; devices and remote-monitoring status;
planned procedures); features that exclude PIFU; features that support it; and any documented
concern about the patient's capacity to self-manage.

### Step 2 — Route to the condition reference and apply it

Match the condition to its reference file and read it. Each file is organised under the same
four-disposition headings, with concrete "supported when" thresholds.

| Condition | Reference file | Pathway type |
|---|---|---|
| Arrhythmia — AF, flutter, SVT, VT, ectopy, pre-excitation, devices | `references/arrhythmia.md` | NHS pathway |
| Heart valve disease — AS, AR, MR, MS, MVP, BAV, prosthetic | `references/valve-disease.md` | NHS pathway |
| Heart failure — HFrEF, HFmrEF, HFpEF | `references/heart-failure.md` | NHS pathway |
| Chest pain (suspected cardiac, new presentation) | `references/chest-pain.md` | GIRFT pathway |
| Left bundle branch block (LBBB) | `references/lbbb.md` | GIRFT pathway |
| POTS | `references/pots.md` | No dedicated pathway |
| Stable angina, post-MI, cardiomyopathy, syncope, other | `references/non-pathway.md` | No dedicated pathway |

For non-pathway conditions (POTS, the general fallback), the output must explicitly state that
no dedicated NHS PIFU pathway exists, and the bar is higher — all six universal SOP criteria
must be *clearly* met.

### Step 3 — Apply the universal SOP checklist (every patient)

Independent of condition, the patient must also pass this cross-condition safety checklist. It
is drawn from the cardiology PIFU SOP. Failing any single item excludes PIFU even when the
primary condition would otherwise qualify.

1. **Clinically stable** — no active decompensation, acute symptoms, or pending intervention.
2. **Diagnosis established** — no outstanding investigations that would change management.
3. **Treatment optimised** — not in an active titration/initiation phase. Low/sub-therapeutic
   doses are *not* "optimised" unless there is a documented clinical ceiling reason.
4. **No secondary-care drug-monitoring requirement** (e.g. warfarin INR, antiarrhythmic
   monitoring, frequent U&Es after a nephrotoxic change).
5. **Patient activation** — documented evidence they understand the condition, know their
   red-flag ("traffic-light") symptoms, can self-monitor, and can contact the service.
6. **No device safety concern** requiring timed follow-up.

Patient must be ≥ 18. Frailty and multimorbidity are *not* automatic exclusions, but reduce
confidence and require careful consideration; flag frailty as a data gap if mentioned without a
formal score.

### Step 4 — Check for data gaps before deciding

If any data point the condition file lists as required is absent, you cannot fully assess the
criterion that depends on it. Minor gaps lower confidence; gaps that block the central
disposition return **INSUFFICIENT_DATA** with a list of exactly what is needed. Never fabricate
a value to fill a gap.

Common traps where the letter reads reassuringly but the data says otherwise: a patient who
feels well but has a falling eGFR after ARNI, rising LFTs on amiodarone, or hyperkalaemia; an
echo that looks stable but whose *rate of change* between studies is the red flag; a suitable
primary condition with a co-medication that needs secondary-care monitoring (e.g. variable INR
on a mechanical valve); a deferred plan ("will reassess after uptitration") — PIFU is premature;
a clinician who voices reservations about PIFU even though the criteria appear met — do not
override their concern.

## Output

```
PATIENT: [Name, DOB, NHS number if available]
CONDITION: [Sub-specialty, subtype, primary diagnosis]
DOCUMENT TYPE: [Clinic letter / Discharge summary / MDT note / Other]
PATHWAY TYPE: [NHS-defined pathway / General SOP — no dedicated pathway for this condition]

DISPOSITION: PIFU | RETAIN_FOLLOW_UP | DISCHARGE | INSUFFICIENT_DATA
CONFIDENCE: [0–100%]

SUPPORTING FACTORS:
  - [factors favouring the disposition, with the specific findings cited]
AGAINST / CAUTIONARY FACTORS:
  - [exclusions or concerns, with the specific findings cited]

DATA GAPS (if any):
  - [missing values and which criterion each blocks]

CRITERIA SOURCE:
  - [e.g. NHS Arrhythmia PIFU guidance + universal SOP; or "General SOP — no condition-specific
    NHS pathway exists for <condition>"]

REASONING:
  [2–4 sentences. Cite the specific criteria. For non-pathway conditions, state explicitly that
  no dedicated NHS guideline exists. For low-confidence cases, name the factor driving the
  uncertainty and confirm the disposition resolved to the safer option.]

PIFU REVIEW INTERVAL (only if DISPOSITION = PIFU):
  [e.g. 12 months per NHS HF PIFU guidance; or the surveillance interval from the condition file]
```

### Confidence calibration

Confidence is a structured judgement, not a formula, across four dimensions: **guideline fit**
(clearly meets published criteria ↑ / sits on a threshold ↓), **exclusion flags** (none ↑ / amber
flags present ↓), **information completeness** (all key values present ↑ / missing ↓), and
**pathway type** (NHS-defined pathway ↑ / general SOP only ↓).

- **> 95%** — unambiguous; no reasonable clinical disagreement.
- **85–95%** — strong case with one minor uncertainty.
- **70–85%** — genuine grey zone; a senior clinician might reasonably differ. Always name the
  driving factor. Per the safety asymmetry, the disposition itself resolves to the safer option.
- **< 70%** — usually return INSUFFICIENT_DATA and list what would resolve it.

## Hard rules

- Never give a PIFU disposition for a non-cardiology patient; state the specialty mismatch.
- Always cite the criteria source. For non-pathway conditions, always state explicitly that no
  dedicated guideline exists — never imply one does.
- End-of-life / palliative care pathway is an absolute exclusion — never PIFU.
- Do not recommend PIFU for: active decompensation; recent hospitalisation < 6 months (HF) or
  cardioversion < 3 months (arrhythmia); planned procedures or pending results that would change
  management; newly initiated medication requiring monitoring; ICD with recent therapies or
  without remote monitoring.
- Never read low/sub-therapeutic doses as "optimised" absent a documented ceiling reason.
- If the patient is already on a PIFU pathway, confirm the existing status rather than
  re-assessing from scratch.
- If key clinical data is missing, flag it and lower confidence or return INSUFFICIENT_DATA; do
  not fabricate values.
- Do not override a clinician's own documented reservation about PIFU with a PIFU disposition.
- Apply the safety asymmetry without exception: ambiguity resolves to RETAIN_FOLLOW_UP, never to
  PIFU or DISCHARGE.

---

## For clinicians maintaining this skill

You only ever edit files in `references/`. You never need to touch this file, and you do not
need to understand how the AI system loads them.

**To add or update a condition:** start from the shared condition template (in the project's
`_authoring/` folder, not inside this skill), rename your copy to the condition (e.g.
`pericarditis.md`), fill in every section, and place it in this skill's `references/` folder.
The template explains the three rules that matter (write checkable criteria; ambiguity means
RETAIN_FOLLOW_UP; state your sources). Then tell the data-science team the file exists so they
can add it to the routing table above and map the OMOP codes — that part is theirs, not yours.

**To change criteria for an existing condition:** edit that condition's file directly. Each
criterion is a standalone bullet you can tighten, add, or remove as clinical experience
accumulates. Keep the "supported when" clause on every criterion — it is what lets the system
act on it reliably.

**Every change is version-controlled and sign-off is recorded** before it reaches a patient
assessment, so leave the `author` / `reviewed_by` / `last_updated` line at the top of each file
current.
