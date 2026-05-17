"""
push_to_confluence.py
Uploads Intern-Projects.html to the PowerBI-AWS Architecture Design Confluence page
and attaches diagram PNGs from design-images/.

Target page: https://veradigm.atlassian.net/wiki/spaces/LSE/pages/6726353073/PowerBI-AWS+Architecture+Design

Usage:
    pip install requests python-dotenv
    python push_to_confluence.py

Credentials (.env — never commit this file):
    CONFLUENCE_EMAIL=your.email@veradigm.com
    CONFLUENCE_API_TOKEN=paste-your-token-here
"""

import os, re, sys, json, requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

# ── Shared config (not secret) ────────────────────────────────────────────────
CONFLUENCE_URL = "https://veradigm.atlassian.net"
PAGE_ID        = "6726353073"

# ── Per-contributor credentials (from .env) ───────────────────────────────────
EMAIL     = os.environ.get("CONFLUENCE_EMAIL", "")
API_TOKEN = os.environ.get("CONFLUENCE_API_TOKEN", "")

SCRIPT_DIR = Path(__file__).parent
HTML_FILE  = SCRIPT_DIR / "Intern-Projects.html"
IMAGES_DIR = SCRIPT_DIR / "design-images"

errors = []
if not EMAIL:     errors.append("CONFLUENCE_EMAIL")
if not API_TOKEN: errors.append("CONFLUENCE_API_TOKEN")
if errors:
    print(f"ERROR: set these variables in .env: {', '.join(errors)}")
    print("See CONTRIBUTING.md for setup instructions.")
    sys.exit(1)

AUTH = (EMAIL, API_TOKEN)
REST = f"{CONFLUENCE_URL}/wiki/rest/api/content"


def check(resp, label):
    if not resp.ok:
        print(f"ERROR [{label}] {resp.status_code}: {resp.text[:400]}")
        sys.exit(1)
    return resp


# Step 1: upload PNG attachments
print("Step 1 - uploading diagram PNGs...")
attachment_url_map = {}
for png in sorted(IMAGES_DIR.glob("*.drawio.png")):
    url = f"{REST}/{PAGE_ID}/child/attachment"
    with open(png, "rb") as fh:
        resp = requests.post(url, auth=AUTH,
                             headers={"X-Atlassian-Token": "no-check"},
                             files={"file": (png.name, fh, "image/png"),
                                    "minorEdit": (None, "true")})
    if resp.status_code not in (200, 201):
        list_resp = requests.get(url, auth=AUTH, params={"filename": png.name})
        existing = list_resp.json().get("results", [])
        if existing:
            att_id = existing[0]["id"]
            with open(png, "rb") as fh:
                resp = requests.post(
                    f"{REST}/{PAGE_ID}/child/attachment/{att_id}/data",
                    auth=AUTH, headers={"X-Atlassian-Token": "no-check"},
                    files={"file": (png.name, fh, "image/png"),
                           "minorEdit": (None, "true")})
            check(resp, f"update attachment {png.name}")
        else:
            check(resp, f"create attachment {png.name}")
    dl_path = f"/wiki/download/attachments/{PAGE_ID}/{png.name}"
    attachment_url_map[f"design-images/{png.name}"] = dl_path
    print(f"  uploaded: {png.name}")


# Step 2: prepare body — strip metadata header + TOC, start from Overview
print("Step 2 - preparing page body...")
raw_html = HTML_FILE.read_text(encoding="utf-8")
body_match = re.search(r"<body>(.*?)</body>", raw_html, re.DOTALL)
if not body_match:
    print("ERROR: no <body> found"); sys.exit(1)

body = body_match.group(1).strip()

# Strip everything before the first real content section (Overview)
overview = re.search(r'<h1\s+id="overview"', body)
if overview:
    body = body[overview.start():]

# Rewrite local image paths to attachment URLs
for local_path, conf_url in attachment_url_map.items():
    body = body.replace(f'src="{local_path}"', f'src="{CONFLUENCE_URL}{conf_url}"')

# Convert <img> tags for attached PNGs to ac:image macros
def img_to_ac_image(match):
    tag = match.group(0)
    src = re.search(r'src="([^"]+)"', tag)
    alt = re.search(r'alt="([^"]+)"', tag)
    if not src: return tag
    filename = src.group(1).split("/")[-1]
    if not filename.endswith(".drawio.png"): return tag
    alt_text = alt.group(1) if alt else filename
    return (f'<ac:image ac:alt="{alt_text}" ac:width="900">'
            f'<ri:attachment ri:filename="{filename}"/></ac:image>')

body = re.sub(r'<img[^>]+>', img_to_ac_image, body)


# Step 3: get current page version
print("Step 3 - fetching page version...")
resp = check(requests.get(f"{REST}/{PAGE_ID}", auth=AUTH,
                          params={"expand": "version,title"}), "get page")
page_data   = resp.json()
current_ver = page_data["version"]["number"]
page_title  = page_data["title"]
print(f"  version: {current_ver}, title: '{page_title}'")


# Step 4: update page
print("Step 4 - updating page...")
payload = {
    "version": {"number": current_ver + 1},
    "title": page_title,
    "type": "page",
    "body": {"storage": {"value": body, "representation": "storage"}},
}
resp = check(requests.put(f"{REST}/{PAGE_ID}", auth=AUTH,
                          headers={"Content-Type": "application/json"},
                          data=json.dumps(payload)), "update page")
print(f"  updated to version {resp.json()['version']['number']}")
print(f"\nDone: {CONFLUENCE_URL}/wiki/spaces/LSE/pages/{PAGE_ID}")
