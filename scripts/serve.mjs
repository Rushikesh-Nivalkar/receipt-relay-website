// Serve dist/ on localhost (port from site.config.json). No dependencies.
import { createServer } from "node:http";
import { readFileSync, statSync, existsSync } from "node:fs";
import { join, dirname, extname, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const cfg = JSON.parse(readFileSync(join(root, "site.config.json"), "utf8"));
const dist = resolve(root, "dist");
const types = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript", ".mjs": "text/javascript",
  ".json": "application/json", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
  ".webp": "image/webp", ".avif": "image/avif", ".woff2": "font/woff2", ".xml": "application/xml", ".txt": "text/plain", ".ico": "image/x-icon" };

createServer((req, res) => {
  let rel;
  try { rel = decodeURIComponent(req.url.split("?")[0]); } catch { res.writeHead(400); return res.end("Bad request"); }
  let f = resolve(dist, "." + rel);
  // never serve outside dist/
  if (f !== dist && !f.startsWith(dist + sep)) { res.writeHead(403); return res.end("Forbidden"); }
  if (existsSync(f) && statSync(f).isDirectory()) f = join(f, "index.html");
  if (!existsSync(f)) { res.writeHead(404); return res.end("Not found"); }
  res.writeHead(200, { "Content-Type": types[extname(f)] || "application/octet-stream" });
  res.end(readFileSync(f));
}).listen(cfg.port, "127.0.0.1", () => console.log(`ReceiptRelay site on http://localhost:${cfg.port}`));
