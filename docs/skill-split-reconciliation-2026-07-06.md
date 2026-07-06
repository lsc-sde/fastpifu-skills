# SKILL.md split reconciliation — 2026-07-06

Records the line-by-line check that nothing was lost when the self-contained v5 SKILL.md
(backed up at `docs/SKILL-v5-self-contained-backup.md`) was split into a lean cardiology-only
`SKILL.md` plus a new shared `alternate-orchestrator-prompt.md`.

## Where everything went

| v5 section | Destination |
|---|---|
| Four-disposition framing, discharge-first principle | `alternate-orchestrator-prompt.md` — "The Four Dispositions" |
| ELIGIBLE/BORDERLINE/NOT_ELIGIBLE distinction, six always-BORDERLINE scenarios, "prefer BORDERLINE when uncertain" | `alternate-orchestrator-prompt.md` — "The Core Safety Rule" (genericized wording; cardiology's concrete examples of each scenario live in SKILL.md's data-gap table) |
| NHS-pathway / GIRFT-informed / non-pathway condition definitions | `SKILL.md` — "Cardiology's three-tier pathway classification" (kept in full — this is cardiology-specific) |
| Step 1 file list + "extract and note" instruction + re-verification date note | `SKILL.md` — "Condition routing" table |
| Step 2 SOP read instruction + 2a criteria (suitable-if / careful-consideration-if / absolute exclusions) | `alternate-orchestrator-prompt.md` — "Universal SOP Checklist" (verbatim; SKILL.md's routing table still points to the local SOP file) |
| Step 2b six-criteria non-pathway test | `alternate-orchestrator-prompt.md` — "Non-Pathway Fallback" (criteria 1-5 generic; criterion 6 genericized with cardiology's concrete device-safety meaning kept in SKILL.md's three-tier section) |
| Step 2c POTS guidance | `SKILL.md` — "POTS disclosure requirement" (kept in full) |
| Step 2d condition-rules.md pointer | `SKILL.md` — "Condition routing" table |
| Step 3 accepted formats + 7-point identify list | `alternate-orchestrator-prompt.md` — "Document Screening Framework" (genericized; item 7's concrete cardiology data-gap list stays in SKILL.md) |
| Step 3 data-gap table (11 rows) | `SKILL.md` — "Specialty-specific cautions (data-gap traps)" (kept in full, terminology updated to RETAIN_FOLLOW_UP) |
| Step 3 "Common traps" (7 bullets) | `SKILL.md` — same section (kept in full) |
| Step 3b verdict-vocabulary mapping | `alternate-orchestrator-prompt.md` — "External Verdict Vocabulary" (the mapping table itself is generic; cardiology's specific internal-classification names are still named in SKILL.md's frontmatter) |
| Step 4 structured output template | `alternate-orchestrator-prompt.md` — "Structured Output" (genericized field labels; cardiology's concrete PIFU-timescale examples were already fully covered in `condition-rules.md`, not duplicated here) |
| Reasoning Transparency Layer 1 (HF worked example) | `SKILL.md` — "Specialty-specific hard rules" (HFrEF/HFmrEF worked example, kept verbatim) |
| Reasoning Transparency Layer 2 (universal SOP six-point recap) | Not duplicated — this was a near-verbatim repeat of the Step 2b six-criteria list already captured once in `alternate-orchestrator-prompt.md`'s Non-Pathway Fallback section |
| "What to do when no guideline exists" 4-point list | `alternate-orchestrator-prompt.md` — "Non-Pathway Fallback" (paraphrased into prose, same four points: disclose, fall back to six criteria, higher threshold, err toward RETAIN_FOLLOW_UP) |
| Note on chest pain/cardiomyopathy not being non-pathway | `SKILL.md` — three-tier section + hard rules |
| Confidence calibration table + thresholds | `alternate-orchestrator-prompt.md` — "Confidence Calibration" (verbatim) |
| "Common borderline scenarios" (8 items) | Split: generic paraphrase in `alternate-orchestrator-prompt.md`; the exact cardiology figures (recent admission >6 months, LVEF 40-50%, etc.) restated precisely in `SKILL.md` so no concrete number was lost |
| Guidance for supervisors | Split: cardiology items (new condition, POTS, subtype rules) → `SKILL.md`; universal items (adjust SOP criteria, adjust confidence thresholds) → `alternate-orchestrator-prompt.md` |
| Hard Rules (16 rules) | Split rule-by-rule: universal framing → `alternate-orchestrator-prompt.md`; cardiology's concrete flag examples (recent hospitalisation/cardioversion windows, ICD remote monitoring, antiarrhythmic initiation, GDMT dosing, bradycardia example) → `SKILL.md` |

## Gaps found and fixed during the check

- The "Discharge-to-GP maps to NOT_ELIGIBLE in structured output" line in v5's Hard Rules was
  cryptic out of context — on inspection this refers specifically to how DISCHARGE cases are
  scored against the current 150-case eval dataset, which only has three ground-truth classes
  (ELIGIBLE/NOT_ELIGIBLE/BORDERLINE, no DISCHARGE class). Restated explicitly as an "Eval-scoring
  note" in `SKILL.md` so this isn't lost or mistaken for a change to the actual clinical output.
- The concrete cardiology figures in "Common borderline scenarios" (>6 months, LVEF 40-50%, etc.)
  needed to be restated verbatim in `SKILL.md`, since the orchestrator's version of this list is
  necessarily genericized for use across all specialties.
- The generic "extract and internally note: eligible / not eligible / monitoring" instruction from
  Step 1 had been dropped in the first draft of the split — added back to `SKILL.md`'s routing
  section.

## Content NOT carried over (intentionally)

Two items were drafted into the lean `SKILL.md` during the split that do **not** come from v5 —
they were pulled in from the "areas identified for next iteration" section of
`docs/fastpifu-version-history.md` (the EPS/WPW rationale hard rule, and a discharge-summary-title
disambiguation trap). These were removed again before finalizing, since the task was a structural
split of the validated v5 content, not an implementation of unreleased v6 ideas. Both remain
documented in the version history as candidate future fixes, to be addressed as a deliberate
decision later, not folded in silently.

## Not fixed (pre-existing, flagged for awareness only)

- v5's Hard Rules mentions "valve gradient" as an example of clinical information that, if
  missing, should be flagged as a data gap — but the Step 3 data-gap table itself has no dedicated
  row for valve gradient (it's implicitly covered by the "Serial echo data" row). This inconsistency
  existed in v5 already and was carried through unchanged, not introduced by the split.
