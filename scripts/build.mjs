// Build: copy src/ to dist/ and apply site.config.json.
// Tokens in src: %%SITE_URL%%, %%DOWNLOAD_URL%%, %%REPO_URL%%, and the comment <!-- %%CANONICAL%% -->.
// canonical, og:url, sitemap and robots carry the real domain only once siteUrl is not localhost.
import { readFileSync, writeFileSync, rmSync, cpSync, readdirSync, statSync } from "node:fs";
import { join, dirname, extname, basename, relative, sep } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const cfg = JSON.parse(readFileSync(join(root, "site.config.json"), "utf8"));
const site = cfg.siteUrl.replace(/\/$/, "");
const isLocal = /localhost|127\.0\.0\.1/.test(site);
const src = join(root, "src"), dist = join(root, "dist");

rmSync(dist, { recursive: true, force: true });
// skip dot-folders such as .taste-skill (tool history, never shipped)
cpSync(src, dist, { recursive: true, filter: (p) => !basename(p).startsWith(".") });

const pages = [];
(function walk(dir) {
  for (const f of readdirSync(dir)) {
    const p = join(dir, f);
    if (statSync(p).isDirectory()) { if (f !== "assets") walk(p); continue; }
    if (extname(f) !== ".html") continue;
    let html = readFileSync(p, "utf8");
    const rel = relative(dist, p).split(sep).join("/");
    const url = `${site}/${rel === "index.html" ? "" : rel}`;
    html = html.replaceAll("%%SITE_URL%%", site).replaceAll("%%DOWNLOAD_URL%%", cfg.downloadUrl).replaceAll("%%REPO_URL%%", cfg.repoUrl);
    html = html.replace("<!-- %%CANONICAL%% -->", isLocal
      ? "<!-- canonical: set siteUrl in site.config.json to the real domain -->"
      : `<link rel="canonical" href="${url}">\n<meta property="og:url" content="${url}">`);
    writeFileSync(p, html);
    pages.push(url);
  }
})(dist);

writeFileSync(join(dist, "sitemap.xml"),
  `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${pages.map(u => `  <url><loc>${u}</loc></url>`).join("\n")}\n</urlset>\n`);
writeFileSync(join(dist, "robots.txt"), isLocal
  ? "User-agent: *\nDisallow: /\n"
  : `User-agent: *\nAllow: /\nSitemap: ${site}/sitemap.xml\n`);
console.log(`built ${pages.length} pages -> dist/ (${isLocal ? "local: no canonical, robots disallow" : site})`);
