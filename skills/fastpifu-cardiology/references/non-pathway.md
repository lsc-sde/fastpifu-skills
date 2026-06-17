# Non-Pathway Conditions (general SOP fallback)

<!-- concept_ids: (completed by data team) -->
<!-- author: PIFU SOP general criteria + GIRFT module 2 | last_updated: 2026-06 -->

## Scope

Cardiology conditions for which **no dedicated NHS England PIFU pathway exists**: stable angina / chronic stable IHD / post-MI, the cardiomyopathies (DCM, HCM — low-risk non-obstructive only), single-episode syncope with normal investigations, and any other cardiology presentation not covered by a dedicated reference file.
POTS is also non-pathway but has enough specific content to warrant its own file (`pots.md`).

For every condition handled here, the output MUST state that no condition-specific NHS pathway exists and that the verdict rests on general SOP criteria alone — the reader needs to know the assessment carries more uncertainty.

## The decision rule

There are no published condition-specific criteria, so fall back entirely to the six general SOP criteria (also in SKILL.md).
ALL six must be **clearly** met — a higher bar than for pathway conditions, because there is no validated guideline confirming PIFU is safe for this population:

1. Clinically stable — no active decompensation, acute symptoms, or pending intervention.
2. Diagnosis established — no outstanding investigations that would change management.
3. Treatment optimised — not in an active titration/initiation phase needing monitoring.
4. No secondary-care drug-monitoring requirement (e.g. warfarin INR, frequent U&Es after a nephrotoxic drug change, antiarrhythmic monitoring).
5. Patient activation confirmed — documented evidence they understand the condition, know their red-flag symptoms, and feel confident to self-manage.
6. No device safety concern requiring timed follow-up.

- If ALL six are clearly met → PIFU under general SOP criteria.
- If ANY is not met, or any is ambiguous → RETAIN_FOLLOW_UP.
  State which criterion failed.
- In genuinely ambiguous cases, err toward RETAIN_FOLLOW_UP.

## Condition-specific notes

These are not separate criteria — they are the typical activation triggers and the common shape of each presentation, to help locate the six SOP criteria in a letter.

- **Stable angina / post-PCI / post-CABG**: PIFU appropriate when symptoms are controlled and the revascularisation episode is complete; activation trigger is new persistent chest pain or breathlessness on exertion.
  Recent procedure or unresolved symptoms → RETAIN.
- **Post-MI**: PIFU only once secondary prevention is optimised and the patient is stable; ongoing titration or recent event → RETAIN.
- **Cardiomyopathy (DCM / HCM)**: only low-risk, non-obstructive, stable disease may be considered, and only if all six SOP criteria are clearly met.
  Any high-risk feature (arrhythmia, outflow obstruction, ICD considerations, family screening in progress) → RETAIN.
- **Single-episode syncope, normal investigations**: PIFU appropriate where recurrence would trigger advanced investigation; activation trigger is new syncope.
  Outstanding workup → RETAIN.

## Borderline / uncertain (resolve to RETAIN_FOLLOW_UP, lower confidence)

Because the bar is "all six clearly met", treat any partial or ambiguous criterion as a borderline case that resolves to RETAIN_FOLLOW_UP, and name the criterion in question.

## Data that must be present to assess

The six SOP criteria each require positive evidence in the letter.
If the letter does not contain enough to confirm them, flag INSUFFICIENT_DATA rather than defaulting to PIFU.

## Source

NHS England PIFU SOP (general eligibility criteria, Appendix 1 cardiology scenarios).
GIRFT Outpatient Operational Guide module 2, v1.2 (March 2026).
No condition-specific NHS PIFU pathway exists for these conditions — always disclosed.
