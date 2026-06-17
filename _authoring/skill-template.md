---
name: fastpifu-<<SPECIALTY>>          # e.g. fastpifu-neurology, fastpifu-urology
description: >
  Use when deciding what should happen next
  with a <<SPECIALTY>> patient's follow-up — whether they can move to patient-initiated follow-up,
  be discharged, or stay in timed follow-up. Covers <<LIST THE CONDITIONS THIS SKILL HANDLES>>.
---

<!--
The universal FastPIFU logic — the four dispositions, the safety asymmetry, the discharge-first
principle, the SOP checklist, the output format, confidence calibration, and the universal hard
rules — lives ONCE in the orchestrator system prompt (fastpifu-orchestrator-prompt.md), not here.
Do not restate it. This file carries only the <<SPECIALTY>> delta. Fill in the slots marked
<<LIKE THIS>>. The per-condition clinical detail goes in separate references/<condition>.md files
authored from condition-template.md.
-->

# FastPIFU — <<Specialty>>

<<Specialty>> PIFU assessment. Routing, cautions, and hard rules specific to <<specialty>>; apply
under the FastPIFU orchestrator's universal operating instructions.

## Condition routing

<!-- One row per condition reference file this skill ships. -->

| Condition | Reference file |
|---|---|
| <<condition>> | `references/<<condition>>.md` |
| <<condition>> | `references/<<condition>>.md` |

## Specialty-specific cautions (data-gap traps)

<!-- The "reads-well-but-the-data-says-otherwise" situations unique to this specialty: a value or
trend that should change the disposition, a co-morbidity/co-medication imposing monitoring, or a
deferred plan that makes PIFU premature. Keep them concrete. -->

- <<caution>>

## Specialty-specific hard rules

<!-- The small number of hard exclusions unique to this specialty, each with a one-line rationale.
If there are none, write: "- None beyond the universal rules." -->

- <<rule — rationale>>
