# AWS Migration Cutover Readiness — Project Rules

## Confluence Target

This project publishes to exactly one Confluence page:

- **URL**: https://veradigm.atlassian.net/wiki/spaces/LSE/pages/6763118607
- **Page ID**: `6763118607`
- **Space**: LSE
- **Page title**: Intern Project — AWS Migration Cutover Readiness (DRAFT)
- **Parent page**: Interns (page ID `6762692662`)

The `push_to_confluence.py` script in this folder is pre-configured with this page ID. Never change the target page without team consensus.

## Credentials (per contributor — never committed)

Each contributor creates their own `.env` file in this folder:

```
CONFLUENCE_EMAIL=your.email@veradigm.com
CONFLUENCE_API_TOKEN=paste-your-token-here
```

Get a token at: https://id.atlassian.com/manage-profile/security/api-tokens

## Document Format

- One HTML file: `AWS-Migration-Cutover-Readiness.html`
- The HTML body starts at `<h1 id="overview">` — everything before that is stripped by the push script
- Diagrams are Draw.io PNG exports in `design-images/`
- Naming: `NN-<short-description>.drawio` and `NN-<short-description>.drawio.png`
- Push to Confluence: `python push_to_confluence.py`

## Diagram Workflow

1. Author the `.drawio` file in `design-images/`
2. Export PNG at scale 1 via draw.io CLI
3. Upscale 4× via the PowerShell snippet in `CONTRIBUTING.md`
4. Reference as `<img src="design-images/<name>.drawio.png" />` in the HTML
5. The push script converts `<img>` tags to native `<ac:image>` macros automatically

## No Push Gate

This project does not use push gate validation.
