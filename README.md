# ReceiptRelay — Website

Marketing site for the ReceiptRelay Android app: a receipt rewards app for Australian shoppers. It is a static site, built with taste-skill under the studio design stack (`.claude/rules/design-stack.md` in master-root).

## Run it locally

Needs Node 22 or later. There are no dependencies to install.

```bash
npm run start      # build src/ -> dist/ and serve on http://localhost:4173
npm run build      # build only
npm run serve      # serve an existing dist/
```

## Configuration

Settings live in `site.config.json`:

| Key | Use |
|---|---|
| `siteUrl` | The site's address. While it is localhost, the build leaves out the canonical link and og:url, and `robots.txt` blocks crawling. Set the real domain and rebuild when one exists. |
| `downloadUrl` | The page the download button opens (GitHub Releases on this repo). |
| `repoUrl` | The footer's "Source and releases" link. |
| `port` | The local server port. |

## Layout

- `src/`: the pages (`index.html`, `download.html`, `privacy.html`, `terms.html`), brand files and the taste-skill kit (`src/assets`).
- `scripts/build.mjs`: copies `src/` to `dist/` and applies the config.
- `scripts/serve.mjs`: a zero-dependency local server.
- `brand/`: the logo system and brand guide.
- `docs/`: `WEBSITE-PLAN.md` and `BUILD-REPORT.md` (gate result, waivers, what is still to do).

## Releases

The APK is published as GitHub Releases on this repository. The site's download button points to the latest release.
