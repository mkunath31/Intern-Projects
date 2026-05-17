# AWS Migration Cutover Readiness — Intern Project Brief

12-week LS-UDP internship project covering the Azure → AWS Snowflake migration. The intern will build a Jira-backed migration dashboard, package the team's Confluence push script as a reusable GitHub Action, build a mapping-driven parity validator, and use that validator to sign off on the replication of one silver-layer database.

**Confluence page**: https://veradigm.atlassian.net/wiki/spaces/LSE/pages/6763118607

## Folder Structure

```
AWS-Migration-Cutover-Readiness/
├── README.md                                  ← this file
├── CLAUDE.md                                  ← project rules (Claude AI instructions)
├── CONTRIBUTING.md                            ← how to set up Confluence credentials
├── .gitignore
├── .env.example                               ← credential template (copy → .env, fill in)
├── AWS-Migration-Cutover-Readiness.html       ← the brief
├── push_to_confluence.py                      ← publishes the brief to Confluence
└── design-images/
    ├── 01-project-flow.drawio                 ← Draw.io source
    ├── 01-project-flow.drawio.png             ← exported PNG (committed)
    ├── 02-stakeholder-map.drawio
    ├── 02-stakeholder-map.drawio.png
    ├── 03-system-diagram.drawio
    └── 03-system-diagram.drawio.png
```

## Updating the Brief

1. Edit `AWS-Migration-Cutover-Readiness.html` — all sections are in this single file
2. To add or change a diagram, edit the `.drawio` source in `design-images/`, then re-export the PNG (see `CONTRIBUTING.md`)
3. Push to Confluence

## Publishing to Confluence

```bash
pip install requests python-dotenv
python push_to_confluence.py
```

See `CONTRIBUTING.md` for credential setup.
