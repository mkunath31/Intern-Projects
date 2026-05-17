# PowerBI-AWS Architecture Design

Architecture documentation for migrating PowerBI data connectivity from Azure to AWS.

**Confluence page**: https://veradigm.atlassian.net/wiki/spaces/LSE/pages/6726353073/PowerBI-AWS+Architecture+Design

## Repository Structure

```
PowerBi-AWS/
├── CLAUDE.md                              ← project rules (Claude AI instructions)
├── README.md                              ← this file
├── CONTRIBUTING.md                        ← how to set up Confluence credentials
├── .gitignore
└── Intern-Projects/
    ├── Intern-Projects.html      ← the document (all use cases inside)
    ├── push_to_confluence.py              ← publishes the document to Confluence
    ├── .env.example                       ← credential template (copy → .env, fill in)
    ├── .gitignore                         ← excludes .env
    └── design-images/
        ├── 01-uc1-current-azure.drawio        ← Draw.io source
        ├── 01-uc1-current-azure.drawio.png    ← exported PNG (committed)
        ├── 02-uc1-future-aws.drawio
        └── 02-uc1-future-aws.drawio.png
```

## Adding a Use Case

1. Add a new `<h1 id="uc-N">` section in `Intern-Projects.html`
2. Create diagrams in `design-images/` following the naming convention
3. Export and upscale PNGs (see `CONTRIBUTING.md`)
4. Push to Confluence

## Publishing to Confluence

```bash
cd Intern-Projects
pip install requests python-dotenv
python push_to_confluence.py
```

See `CONTRIBUTING.md` for credential setup.
