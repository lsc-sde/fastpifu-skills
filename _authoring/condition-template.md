# <CONDITION NAME>

<!--
================================================================================
HOW TO USE THIS TEMPLATE  (read once, then delete this comment block in your copy)
================================================================================
You are writing ONE file describing ONE condition. Copy this file, rename it to
the condition (lower-case, hyphens, e.g. `atrial-fibrillation.md`), and fill in
every section below. You do not need to know anything about how the AI system
works — just write the clinical criteria as clearly as you would explain them to
a new registrar.

Three rules that matter more than anything else:

1. WRITE CRITERIA AS CHECKABLE STATEMENTS, NOT IMPRESSIONS.
   The system can only act on something it can verify in a clinic letter. So for
   every criterion, state the specific finding, value, or wording that makes it
   true. "Stable" is not checkable. "Asymptomatic AND Vmax < 4.0 m/s on the most
   recent echo" is checkable. Each bullet should answer: *what would I have to
   read in the letter to know this is satisfied?*

2. WHEN IN DOUBT, THE SAFE ANSWER IS RETAIN_FOLLOW_UP.
   Missing or ambiguous information must never push a patient toward PIFU or
   DISCHARGE. If a criterion cannot be confirmed, that is a reason to keep the
   patient in timed follow-up, not to wave them through. Write your criteria with
   that asymmetry in mind.

3. ONLY WRITE WHAT YOU OWN.
   Do not edit SKILL.md or any other condition file. The data-science team maps
   your condition to OMOP codes and wires it in — leave the `concept_ids` line
   blank if you don't know it.
================================================================================
-->

<!-- concept_ids: (left blank for clinicians — completed by the data team) -->
<!-- author: <your name>  |  reviewed_by: <clinical lead>  |  last_updated: <YYYY-MM-DD> -->

## Scope

One or two sentences: which patients this file covers, and any subtypes it
handles (e.g. "Covers atrial fibrillation: paroxysmal, persistent, and
permanent."). If a presentation looks like this condition but belongs elsewhere,
say so here.

## PIFU — when the patient is suitable for patient-initiated follow-up

The specialist relationship continues, but the patient self-initiates contact.
List the criteria that must ALL hold. For each, state what confirms it.

- Criterion: <plain statement>
  Supported when: <the specific finding / value / wording that must be present>
- Criterion: ...
  Supported when: ...

## RETAIN_FOLLOW_UP — when timed specialist follow-up is still needed

The patient is not stable or informed enough to self-initiate safely, but still
needs the specialist. List the features that require timed follow-up. Any one of
these is enough to exclude PIFU.

- Feature: <plain statement>
  Identified when: <the specific finding / value / wording>
- Feature: ...
  Identified when: ...

## DISCHARGE — when no ongoing specialist follow-up is needed at all

The episode of specialist care is complete and the patient returns fully to GP
care. This is NOT the same as PIFU. List the scenarios where discharge is the
correct outcome.

- Scenario: <plain statement>
  Identified when: <the specific finding / wording, e.g. "letter states no
  further specialist input required">

## Borderline / uncertain cases

Situations where the criteria are genuinely on a threshold or partially met.
These do not get their own verdict — under the safety rule they resolve to
RETAIN_FOLLOW_UP — but naming them tells the system to lower its confidence and
flag the specific reason. List the recurring grey-zone patterns for this
condition.

- <e.g. "Value sits at the boundary (X to Y) without a documented trajectory">
- ...

## Data that must be present to assess this condition

The specific values or facts a letter MUST contain before a confident PIFU or
DISCHARGE decision is possible. If any are absent, the system flags
INSUFFICIENT_DATA rather than guessing. List them, with why each matters.

| Required data point | Why it matters |
|---|---|
| <e.g. LVEF (quantified %)> | <e.g. distinguishes borderline severity> |
| ... | ... |

## Surveillance / review interval (if applicable)

If patients on this pathway need imaging or review at set intervals (e.g.
echo every 1–2 years), state the interval and what the review checks. Omit if
not applicable.

## Source

The published guidance these criteria come from, with version/date — e.g.
"NHS England, Setting up PIFU services for people with arrhythmia"; "GIRFT
Outpatient Operational Guide module 2, v1.2 March 2026". This is part of the
clinical-safety audit trail, so be specific.
