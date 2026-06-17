# FastPIFU Skills Library

Skills for agentic outpatient follow-up optimisation.

See https://agentskills.io/ for information on Agent Skills specification.

```
├── skills
    ├── fastpifu-cardiology
    ├── fastpifu-dermatology
    ├── fastpifu-ent
    ├── fastpifu-gastroenterology
    ├── fastpifu-general-surgery
    ├── fastpifu-gynaecology
    ├── fastpifu-omfs
    ├── fastpifu-ophthalmology
    ├── fastpifu-orthopaedics
    ├── fastpifu-spinal
    ├── fastpifu-urology
    └── index.md
```

## How it composes

The universal reasoning (four dispositions, safety asymmetry, discharge-first, SOP checklist, output format, confidence calibration, universal hard rules) lives ONCE in `fastpifu-orchestrator-prompt.md`.
The orchestrator runs with that prompt plus one specialty skill loaded.
Each SKILL.md is now lean and holds only the specialty delta: its condition routing table, its data-gap cautions, and its specialty-specific hard rules.
The per-condition clinical criteria live in each skill's `references/` folder.

Skills carry no run-time logic about fetching or networking — offline operation is a property of the deployment environment (no egress), not an instruction in the files.
Provenance for each criterion is in that reference file's `Source:` line, for audit.

The ten guide-derived skills regenerate from `_authoring/generate_skills.py` + `_authoring/skills_data.py`.
The condition files are first-draft scaffolds at the guide's level of specificity, for the specialty leads to enrich via `_authoring/condition-template.md`.

Copyright (c) 2026 Lancashire Teaching Hospitals NHS Foundation Trust.
