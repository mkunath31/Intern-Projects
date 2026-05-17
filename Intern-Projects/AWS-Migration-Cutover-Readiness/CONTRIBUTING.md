# Contributing to AWS Migration Cutover Readiness

## Setting Up Confluence Credentials

This folder publishes to:
**https://veradigm.atlassian.net/wiki/spaces/LSE/pages/6763118607**

Each contributor uses their own Atlassian API token. Tokens are never committed to git.

### Step 1 — Create your .env file

```bash
cp .env.example .env
```

### Step 2 — Fill in your credentials

Edit `.env`:

```
CONFLUENCE_EMAIL=your.name@veradigm.com
CONFLUENCE_API_TOKEN=paste-your-token-here
```

### Step 3 — Generate your API token

1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click **Create API token**
3. Label it `intern-cutover-readiness` (or anything meaningful)
4. Copy the token and paste it into `.env`

### Step 4 — Install dependencies (one-time)

```bash
pip install requests python-dotenv
```

### Step 5 — Publish

```bash
python push_to_confluence.py
```

The script is idempotent — re-running updates the page in place and increments the version.

---

## Adding or Updating Diagrams

Diagrams live in `design-images/`.

### Naming convention

```
NN-short-description.drawio       ← Draw.io source (commit this)
NN-short-description.drawio.png   ← exported PNG (commit this)
```

### Export workflow

**Step 1 — Export at scale 1:**
```bash
"/c/Program Files/draw.io/draw.io.exe" --export --format png --scale 1 --border 10 \
  --output "design-images/<name>_src1x.png" \
  "design-images/<name>.drawio"
```

**Step 2 — Upscale 4× via PowerShell:**
```powershell
$diagDir = "<absolute-path-to-design-images>"
$base = "<name>"
Add-Type -AssemblyName System.Drawing
$src = [System.Drawing.Image]::FromFile("$diagDir\${base}_src1x.png")
$w = $src.Width * 4; $h = $src.Height * 4
$dst = New-Object System.Drawing.Bitmap($w, $h)
$g = [System.Drawing.Graphics]::FromImage($dst)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.DrawImage($src, 0, 0, $w, $h)
$g.Dispose(); $src.Dispose()
$dst.Save("$diagDir\${base}.drawio.png", [System.Drawing.Imaging.ImageFormat]::Png)
$dst.Dispose()
Remove-Item "$diagDir\${base}_src1x.png"
```

The push script handles uploading PNGs to Confluence and converting `<img>` tags to native `<ac:image>` macros automatically.
