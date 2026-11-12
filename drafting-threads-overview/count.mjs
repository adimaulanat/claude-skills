// node count.mjs <THREADS.md>
// Checks each post (a code block under a "### N" heading): <=500 chars, no em dash, <=1 link (the last post may list links).
import fs from "node:fs";
const file = process.argv[2];
if (!file) { console.error("usage: node count.mjs <THREADS.md>"); process.exit(2); }
const md = fs.readFileSync(file, "utf8");
const posts = [...md.matchAll(/^### (\d+)[^\n]*\n```\n([\s\S]*?)\n```/gm)].map((m) => ({ n: +m[1], t: m[2] }));
if (!posts.length) { console.error("no posts found"); process.exit(2); }
const LINK = /https?:\/\/\S+|\b(?:[a-z0-9-]+\.)+(?:com|io|ai|id|dev|app|co|net|org)(?:\/\S*)?/gi;
let bad = 0;
for (const [i, { n, t }] of posts.entries()) {
  const chars = [...t].length, dash = (t.match(/—/g) || []).length, links = (t.match(LINK) || []).length;
  const last = i === posts.length - 1;
  const errs = [chars > 500 && "over 500", dash && "em dash", !last && links > 1 && "more than 1 link"].filter(Boolean);
  if (errs.length) bad++;
  console.log(`${String(n).padStart(2)}  ${String(chars).padStart(3)} chars  ${dash} em dash  ${links} links  ${errs.length ? "FAIL: " + errs.join(", ") : "ok"}`);
}
console.log(`${posts.length} posts, ${bad} failing`);
process.exit(bad ? 1 : 0);
