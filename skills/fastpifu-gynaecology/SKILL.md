---
name: fastpifu-gynaecology
description: >
  Use when deciding what should happen next
  with a gynaecology patient's follow-up — whether they can move to patient-initiated follow-up,
  be discharged, or stay in timed follow-up. Covers pelvic organ prolapse (conservative, pessary
  and surgical pathways), endometriosis, secondary amenorrhoea, PCOS, heavy or irregular menstrual
  bleeding, chronic pelvic pain, fibroids, recurrent miscarriage, menopause, urethral bulking
  agents and urinary incontinence.
---

<!-- Universal FastPIFU logic (dispositions, safety asymmetry, SOP checklist, output format) lives
in the orchestrator system prompt. This file is gynaecology-specific only. -->

# FastPIFU — Gynaecology

Gynaecology PIFU assessment.
Routing, cautions, and hard rules specific to gynaecology; apply under the FastPIFU orchestrator's universal operating instructions.

## Condition routing

| Condition | Reference file |
|---|---|
| General principles (remote consultation, discharge pathways, top tips) | `references/general-principles.md` |
| Pelvic organ prolapse (POP) | `references/pelvic-organ-prolapse.md` |
| Endometriosis (mild/moderate and severe) | `references/endometriosis.md` |
| Secondary amenorrhoea | `references/secondary-amenorrhoea.md` |
| PCOS | `references/pcos.md` |
| Heavy or irregular menstrual bleeding | `references/heavy-or-irregular-menstrual-bleeding.md` |
| Chronic pelvic pain | `references/chronic-pelvic-pain.md` |
| Fibroids (medically managed) | `references/fibroids.md` |
| Recurrent miscarriage | `references/recurrent-miscarriage.md` |
| Menopause | `references/menopause.md` |
| Bulking agents (urethral, for stress incontinence) | `references/bulking-agents.md` |
| Urinary incontinence (uncomplicated) | `references/urinary-incontinence.md` |

## Specialty-specific cautions (data-gap traps)

- A patient close to the BMI surgical cut-off — may be listed conditionally to allow time for weight loss; not a straightforward PIFU.
- A post-operative patient where early recurrence or complication is the concern — direct access back to the surgical team is needed.
- A letter that reports symptom "improvement" without confirming the bleeding/pain pattern is acceptable to the patient — improvement is not the same as controlled.
- A deferred fertility, imaging or biopsy result that would change the disposition if positive — treat as pending, not as PIFU-suitable.

## Specialty-specific hard rules

- BMI > 35 may make a patient ineligible for surgery — ensure this is communicated and conservative options (physio, pessary) are offered.
- Vulval conditions, post-menopausal bleeding, abnormal vaginal bleeding and post-coital bleeding are never a remote/PIFU disposition — rationale: these require physical examination and/or exclusion of sinister pathology.
- Heavy/irregular menstrual bleeding requiring an endometrial biopsy is never a remote appointment — rationale: NICE requires face-to-face assessment.
- 2-week-wait cancer referrals are excluded from the remote-first/PIFU approach entirely.
