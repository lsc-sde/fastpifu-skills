---
name: fastpifu-<<SPECIALTY>>          # e.g. fastpifu-neurology, fastpifu-urology
description: >
  Assess a <<SPECIALTY>> patient for PIFU (Patient-Initiated Follow-Up) suitability from their
  clinical documents (clinic letters, discharge summaries, MDT notes) and return one of four
  dispositions — PIFU, RETAIN_FOLLOW_UP, DISCHARGE, or INSUFFICIENT_DATA — with a confidence
  score and explicit reasoning. Use this whenever you need to screen a <<SPECIALTY>> patient for
  PIFU, decide whether a patient can move to patient-initiated follow-up, be discharged, or must
  stay in timed follow-up, or process a <<SPECIALTY>> clinic letter for follow-up disposition.
  Covers <<LIST THE CONDITIONS THIS SKILL HANDLES>>. Reach for this skill even when the request
  doesn't say "PIFU" explicitly but asks what should happen next with a <<SPECIALTY>> patient's
  follow-up.
---

<!--
================================================================================
HOW TO USE THIS TEMPLATE (data-science team — delete this block in the real skill)
================================================================================
This shell holds the universal PIFU logic that every FastPIFU specialty skill shares:
the four dispositions, the safety asymmetry, the discharge-first principle, the SOP
checklist, the output format, confidence calibration, and the universal hard rules.
DO NOT change those — they are the safety contract and must be identical across all
specialties. Only fill in the slots marked  <<LIKE THIS>>  and the two clearly-labelled
specialty-specific subsections (Step 4 traps, and specialty-specific hard rules).

If the universal logic ever changes, change it HERE and regenerate every specialty's
SKILL.md from this shell — that keeps a single source of truth for the safety logic
while each deployed skill stays fully self-contained and offline.

The per-condition clinical detail does NOT go in this file. It goes in separate
references/<condition>.md files authored by the specialty lead from the condition
template (also in _authoring/).
================================================================================
-->

# FastPIFU — <<Specialty>>

This skill decides what should happen next with a <<specialty>> patient who is **already in
outpatient follow-up**. It loads the relevant clinical criteria, screens the patient's documents
against them, applies a universal safety checklist, and returns a single structured disposition
with a confidence score.

The clinical detail for each condition lives in `references/` and is loaded only when needed —
this file holds the workflow, the routing, and the cross-condition logic that applies to every
patient regardless of diagnosis.

## The four dispositions

Every assessment resolves to exactly one of these:

- **PIFU** — the specialist relationship continues, but the patient self-initiates contact when
  something changes rather than being booked routinely. The clinician stays responsible; only the
  trigger shifts to the patient.
- **RETAIN_FOLLOW_UP** — the specialist relationship continues, but follow-up must be *timed and
  scheduled by the clinician*. The patient is not stable or informed enough to self-initiate safely.
- **DISCHARGE** — no ongoing specialist follow-up is needed at all; the patient returns fully to GP
  care and the specialist episode is complete.
- **INSUFFICIENT_DATA** — the documents do not contain enough to evaluate the criteria safely. This
  is a real outcome, not a failure: it flags the case for clinician review rather than forcing a guess.

**PIFU is not discharge.** If a letter hands the patient entirely back to GP with no ongoing
specialist role ("no further follow-up required", "discharged to your care", "no further specialist
input needed"), that is DISCHARGE — however stable the patient looks.

## The safety asymmetry (the single most important rule)

The errors are not symmetric. Leaving a suitable patient in timed follow-up is safe — they keep
their appointments. Placing an unsuitable patient on PIFU, or discharging them, risks delayed
recognition of deterioration. Therefore:

> **Missing or ambiguous information can only ever push the disposition toward the safer option
> (RETAIN_FOLLOW_UP), never toward PIFU or DISCHARGE.**

A genuine borderline case resolves to RETAIN_FOLLOW_UP, not PIFU. When you cannot confirm a
criterion, that is a reason to retain, not to wave through. When key data is absent, return
INSUFFICIENT_DATA rather than assuming the favourable reading.

## Discharge-first principle (GIRFT)

Identifying patients who can be safely **discharged** matters more than finding PIFU candidates —
it is what creates clinic capacity. So the first question for every patient is always: *can this
patient be discharged entirely?* Only if no does the PIFU-vs-timed question apply. A clean-looking
letter that describes handing the patient back to GP is a DISCHARGE, never a PIFU.

## Workflow

All clinical criteria this skill needs are bundled in its `references/` folder. The skill runs
**fully offline** and never fetches anything at run time. The reference files are the single source
of truth; the published guidance each is drawn from is named in that file's *Source* section for
provenance and audit, not retrieved live.

### Step 1 — Read the patient's document(s)

Accepted formats: PDF, Word (.docx), plain text, or pasted text — read whatever is provided. If
several documents describe the same patient, read all of them first. If none is provided, ask for
the letter before proceeding.

Confirm this is a <<specialty>> document. If it is not, state the specialty mismatch and stop.

Then identify: the condition and **subtype**; diagnosis and clinical status; current management
(drugs with doses and how recently started; relevant devices/procedures and their status; planned
investigations); features that exclude PIFU; features that support it; and any documented concern
about the patient's capacity to self-manage.

### Step 2 — Route to the condition reference and apply it

Match the condition to its reference file and read it. Each file is organised under the same four
disposition headings, with concrete "supported when" thresholds.

<!-- SPECIALTY-SPECIFIC: list every condition reference file this skill ships, and flag which have
     a dedicated published pathway vs. which fall back to general SOP reasoning. -->

| Condition | Reference file | Pathway type |
|---|---|---|
| <<condition>> | `references/<<condition>>.md` | <<Published pathway / No dedicated pathway>> |
| <<condition>> | `references/<<condition>>.md` | <<...>> |
| <<other / not separately listed>> | `references/non-pathway.md` | No dedicated pathway |

For conditions with no dedicated published pathway, the output must explicitly state that fact, and
the bar is higher — all six universal SOP criteria must be *clearly* met.

### Step 3 — Apply the universal SOP checklist (every patient)

Independent of condition, the patient must also pass this cross-condition safety checklist. Failing
any single item excludes PIFU even when the primary condition would otherwise qualify.

1. **Clinically stable** — no active decompensation, acute symptoms, or pending intervention.
2. **Diagnosis established** — no outstanding investigations that would change management.
3. **Treatment optimised** — not in an active titration/initiation phase. Low/sub-therapeutic doses
   are *not* "optimised" unless there is a documented clinical ceiling reason.
4. **No secondary-care monitoring requirement** (e.g. a drug needing regular specialist bloods, or a
   device/parameter needing scheduled specialist checks).
5. **Patient activation** — documented evidence they understand the condition, know their red-flag
   ("traffic-light") symptoms, can self-monitor, and can contact the service.
6. **No safety concern** requiring timed follow-up (e.g. a device, an implant, or a monitored
   parameter specific to this specialty).

Patient must be ≥ 18. Frailty and multimorbidity are *not* automatic exclusions, but reduce
confidence and require careful consideration; flag frailty as a data gap if mentioned without a
formal score.

### Step 4 — Check for data gaps before deciding

If any data point the condition file lists as required is absent, you cannot fully assess the
criterion that depends on it. Minor gaps lower confidence; gaps that block the central disposition
return **INSUFFICIENT_DATA** with a list of exactly what is needed. Never fabricate a value.

<!-- SPECIALTY-SPECIFIC: list the "reads-well-but-the-data-says-otherwise" traps for this specialty
     — the situations where a letter sounds reassuring but a specific value, trend, or omission
     should change the disposition. Keep them concrete. -->

Common traps for <<specialty>>:
- <<e.g. a result that looks stable in isolation but whose trend across studies is the red flag>>
- <<e.g. a co-medication or comorbidity that imposes a secondary-care monitoring requirement>>
- <<e.g. a deferred plan ("will reassess after X") which makes PIFU premature>>
- A clinician who voices reservations about PIFU even though the criteria appear met — do not
  override their concern.

## Output

```
PATIENT: [Name, DOB, NHS number if available]
CONDITION: [Condition, subtype, primary diagnosis]
DOCUMENT TYPE: [Clinic letter / Discharge summary / MDT note / Other]
PATHWAY TYPE: [Published pathway / General SOP — no dedicated pathway for this condition]

DISPOSITION: PIFU | RETAIN_FOLLOW_UP | DISCHARGE | INSUFFICIENT_DATA
CONFIDENCE: [0–100%]

SUPPORTING FACTORS:
  - [factors favouring the disposition, with the specific findings cited]
AGAINST / CAUTIONARY FACTORS:
  - [exclusions or concerns, with the specific findings cited]

DATA GAPS (if any):
  - [missing values and which criterion each blocks]

CRITERIA SOURCE:
  - [e.g. <published pathway name> + universal SOP; or "General SOP — no condition-specific
    pathway exists for <condition>"]

REASONING:
  [2–4 sentences. Cite the specific criteria. For non-pathway conditions, state explicitly that no
  dedicated guideline exists. For low-confidence cases, name the factor driving the uncertainty and
  confirm the disposition resolved to the safer option.]

PIFU REVIEW INTERVAL (only if DISPOSITION = PIFU):
  [the review/surveillance interval from the condition file]
```

### Confidence calibration

Confidence is a structured judgement, not a formula, across four dimensions: **guideline fit**
(clearly meets published criteria ↑ / sits on a threshold ↓), **exclusion flags** (none ↑ / amber
flags present ↓), **information completeness** (all key values present ↑ / missing ↓), and **pathway
type** (published pathway ↑ / general SOP only ↓).

- **> 95%** — unambiguous; no reasonable clinical disagreement.
- **85–95%** — strong case with one minor uncertainty.
- **70–85%** — genuine grey zone; a senior clinician might reasonably differ. Always name the driving
  factor. Per the safety asymmetry, the disposition itself resolves to the safer option.
- **< 70%** — usually return INSUFFICIENT_DATA and list what would resolve it.

## Hard rules

<!-- The rules below are UNIVERSAL — keep them verbatim. Add specialty-specific rules in the second
     list only. -->

- Never give a PIFU disposition for a patient outside this specialty; state the specialty mismatch.
- Always cite the criteria source. For non-pathway conditions, always state explicitly that no
  dedicated guideline exists — never imply one does.
- End-of-life / palliative care pathway is an absolute exclusion — never PIFU.
- Do not recommend PIFU where there is active decompensation, a planned procedure or pending result
  that would change management, or a newly initiated treatment requiring monitoring.
- Never read low/sub-therapeutic doses as "optimised" absent a documented ceiling reason.
- If the patient is already on a PIFU pathway, confirm the existing status rather than re-assessing
  from scratch.
- If key clinical data is missing, flag it and lower confidence or return INSUFFICIENT_DATA; do not
  fabricate values.
- Do not override a clinician's own documented reservation about PIFU with a PIFU disposition.
- Apply the safety asymmetry without exception: ambiguity resolves to RETAIN_FOLLOW_UP, never to
  PIFU or DISCHARGE.

**<<Specialty>>-specific hard rules:**
<!-- SPECIALTY-SPECIFIC: the small number of hard exclusions unique to this specialty, each with a
     one-line rationale so future editors understand why it exists. Examples of the *kind* of thing:
     a time-since-event exclusion, a device/monitoring exclusion, a high-risk-subtype exclusion. -->
- <<rule — rationale>>

---

## For clinicians maintaining this skill

You only ever edit files in `references/`. You never need to touch this file, and you do not need to
understand how the AI system loads them.

**To add or update a condition:** start from the shared condition template (in the project's
`_authoring/` folder), rename your copy to the condition (e.g. `migraine.md`), fill in every section,
and place it in this skill's `references/` folder. The template explains the three rules that matter
(write checkable criteria; ambiguity means RETAIN_FOLLOW_UP; state your sources). Then tell the
data-science team the file exists so they can add it to the routing table above and map the OMOP
codes — that part is theirs, not yours.

**To change criteria for an existing condition:** edit that condition's file directly. Each criterion
is a standalone bullet you can tighten, add, or remove. Keep the "supported when" clause on every
criterion — it is what lets the system act on it reliably.

**Every change is version-controlled and sign-off is recorded** before it reaches a patient
assessment, so keep the `author` / `reviewed_by` / `last_updated` line at the top of each file current.
