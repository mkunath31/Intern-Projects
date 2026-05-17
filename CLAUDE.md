# PowerBI-AWS Architecture Design — Project Rules

## Confluence Target

This project publishes to exactly one Confluence page:

- **URL**: https://veradigm.atlassian.net/wiki/spaces/LSE/pages/6726353073/PowerBI-AWS+Architecture+Design
- **Page ID**: `6726353073`
- **Space**: LSE
- **Page title**: PowerBI-AWS Architecture Design

The `push_to_confluence.py` script in `Intern-Projects/` is pre-configured with this page ID.
Never change the target page without team consensus.

## Credentials (per contributor — never committed)

Each contributor creates their own `Intern-Projects/.env` file:

```
CONFLUENCE_EMAIL=your.email@veradigm.com
CONFLUENCE_API_TOKEN=paste-your-token-here
```

Get a token at: https://id.atlassian.com/manage-profile/security/api-tokens

## Document Format

- One HTML file: `Intern-Projects/Intern-Projects.html`
- All use cases are `<h1>` sections **inside** that HTML file — not separate files or folders
- Diagrams are Draw.io PNG exports in `Intern-Projects/design-images/`
- Naming: `NN-uc<N>-<short-description>.drawio` (e.g. `01-uc1-current-azure.drawio`)
- Push to Confluence: `cd Intern-Projects && python push_to_confluence.py`

## Diagram Workflow

1. Author the `.drawio` file in `design-images/`
2. Export PNG at scale 1 via draw.io CLI
3. Upscale 4× via the PowerShell snippet in the document skill
4. Reference as `<img src="design-images/<name>.drawio.png" />`
5. The push script converts `<img>` tags to `<ac:image>` macros automatically

## No Push Gate

This project does not use push gate validation.
