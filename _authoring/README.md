# FastPIFU skill authoring

This folder holds the shared scaffolding for building FastPIFU skills. It is **not** a skill and
is never shipped to an agent — it lives one level above the individual specialty skills, which
each get their own self-contained, offline bundle.

## Repository layout

```
<repo root>/
├── _authoring/                      ← this folder (humans only, never deployed)
│   ├── README.md                    ← you are here
│   ├── skill-template.md            ← shell for a new specialty's SKILL.md
│   └── condition-template.md        ← one-per-condition template the clinical leads fill in
│
├── fastpifu-cardiology/             ← a deployed skill (self-contained, offline)
│   ├── SKILL.md
│   └── references/
│       ├── arrhythmia.md
│       ├── valve-disease.md
│       ├── heart-failure.md
│       ├── pots.md
│       └── non-pathway.md
│
├── fastpifu-neurology/              ← same shape, different specialty
│   ├── SKILL.md
│   └── references/
│       └── …
└── …                                ← urology, gastroenterology, etc.
```

Each specialty is an independent skill with its own SKILL.md and references. Nothing is shared at
run time — every skill carries all the clinical criteria it needs and works with no internet access.

## Who does what

**Specialty clinical lead (one per specialty).** Authors condition reference files only, one per
condition, from `condition-template.md`. Writes clinical criteria as checkable statements. Never
touches SKILL.md, never needs to know how the agent works. Owns the `author` / `reviewed_by` /
`last_updated` line at the top of each file.

**Data-science team.** Instantiates each new specialty's SKILL.md from `skill-template.md` (filling
only the marked slots), keeps the universal safety logic identical across all skills, wires new
condition files into the routing table, and maps OMOP concept IDs. Runs the validation gate and
packages the skill.

## The two templates

- **`skill-template.md`** — the SKILL.md shell. Carries the universal PIFU logic (four dispositions,
  safety asymmetry, discharge-first, SOP checklist, output format, confidence calibration, universal
  hard rules) as fixed text, with specialty-specific slots marked `<<LIKE THIS>>`. The universal
  logic is the safety contract: it must stay identical across all ten specialties. If it has to
  change, change it here and regenerate every SKILL.md, so there is a single source of truth for the
  safety logic even though each deployed skill is self-contained.

- **`condition-template.md`** — the per-condition file. Four disposition headings, every criterion
  forced into a checkable "supported when" clause, a required-data table, a source line for audit.
  This is the only thing a clinical lead has to learn.

## Three rules that hold everywhere

1. **Criteria must be checkable.** Every criterion states the specific finding, value, or wording
   that makes it true. The agent can only act on what it can verify in a letter.
2. **Ambiguity is safe only in one direction.** Missing or unclear information resolves to
   RETAIN_FOLLOW_UP, never to PIFU or DISCHARGE. Severe gaps return INSUFFICIENT_DATA.
3. **Everything is offline and self-contained.** A deployed skill carries all its criteria in
   `references/`. Published guidance is cited for provenance, never fetched.

## Version control and sign-off

Each skill folder is version-controlled. Condition files carry their author, reviewer, and date.
Changes are reviewed and clinically signed off before deployment, and releases are tagged — the
git history is the audit trail for which criteria version produced a given disposition.
