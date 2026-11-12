---
name: drafting-threads-overview
description: Use when a finished video or project should get a Threads thread that walks through how it was made, where every post can be quoted later as its own spoke thread. Covers asking the right questions, a plan with every hook shown, drafting and checking posts, optional images, and filling the drafts into the Threads composer in a browser. The person presses Post, never Claude.
---

# Drafting a Threads overview thread

One hub thread tells the whole story. Each post is one stage and stands alone, so the author can quote it later and explain that stage in a separate spoke thread. Claude drafts and fills the composer; the author posts.

Read the project's own files first (CLAUDE.md, the style or copy doc, COPY/sources files, QA scores) and ask only what they do not answer. Never assume the author's tools, language or look.

## 1. Ask (one AskUserQuestion round)

- Link to the published video, and which platform it is on.
- Which links go in the thread (tools, skills, repos) and what the author's relationship to each is: user, affiliate, sponsor. This decides any disclosure label. No affiliate link unless given.
- Which Threads account, because it sets the voice (personal "aku" or brand).
- Post time. Default: 30 minutes after the video goes live.
- Images: yes or no, and on which posts. Default: 1 image on each of the 2 most visual stages.
- Which browser, **asked before any browser step**: Claude in Chrome (real Chrome, existing Threads login) for filling the composer, headless Chrome for rendering images.

## 2. Plan, and show every hook

Plan mode output, concise:

- Context: facts to use, each with its source file or URL.
- A table `# | stage | hook (verbatim) | attachment`. The author reviews the actual sentences; a plan without them gets rejected.
- Images, schedule, unresolved questions. Then ask for confirmation.

Typical stages: opening (the author's own sentence plus the video link), script source, visual concept and palette, fact check, voice, render, QA loop, copy, closing list of tools.

Rules learned from the author's feedback:

- The author's own sentences are used as written. Their inline additions go into the post they commented on.
- Match the author's hook and the project style doc: short sentences, everyday language, familiar English terms kept (prompt, scene, render, skill), no em dash, at most one emoji.
- 500 characters per post at most, one link per post at most. The closing post may list links.
- Every number comes from a repo file or a named source with a check date. If the author's wording overstates a result ("above 90" when the score is exactly 90), propose the accurate wording and ask.
- Leave out what the author says to leave out (for example a paid tool they do not want mentioned), and do not add costs they say do not count.
- Open every link before using it. Never invent a link. A skill with no public source is called "local skill".
- No engagement bait. The closing post says the list is here and the next thread explains why each tool was used.

## 3. Draft and check

1. Write the posts into `THREADS.md` using `threads-template.md` (header with account, schedule, style, disclosure, dated sources; one code block per post; spoke table).
2. Run `no-ai-slop` on the posts if it is installed. Look for contrast framing, colon reveals, em dashes, kicker lines.
3. Run `node count.mjs <THREADS.md>`. It must exit 0.
4. Show the final posts in chat.

## 4. Images (optional)

- One HTML page, 1080x1350, one `<section id="post-NN">` per image, shown with `:target`. Use the project's colors and fonts.
- Read facts from the source files in the build script and throw when the chart or quote disagrees with the file.
- Charts are honest: axis from 0, the pass line drawn, rounds that were re-scored partially say so in the source line.
- Render: `bash render-images.sh page.html <out-dir> post-02:post-02-name.png ...`. View every PNG before moving on.

## 5. Fill the composer (Claude in Chrome)

Load the `anthropic-skills:chrome-browser` skill first.

1. Open a new tab at threads.com. Check the logged-in account is the one the author named. If not, stop and say so.
2. Click the composer's "What's new?" field, then type post 1. Wait until a pasted link's preview has finished loading and the dialog has stopped moving, then take a screenshot. The preview shifts the layout, so never click "Add to thread" from remembered coordinates: use `find` for its ref (or a fresh screenshot), click, and screenshot again to confirm a second empty slot exists before typing post 2. Repeat for every post. If the dialog closed and the page changed, stop: typed text may have gone to another page's reply box. Check nothing was posted and tell the author.
3. Attach images to the posts that have them: never click the image icon (it opens a native file picker). `find` the post's hidden file-input ref (one per post slot, in order) and call `file_upload` with the PNG's absolute path; confirm in a screenshot that the image sits in the right post. An image replaces that post's link preview card. If upload is rejected, say which PNG goes on which post and leave it to the author.
   Check how each link was linkified: Threads cut `https://tokogame.ai.id` after `.ai` (preview pointed to `tokogame.ai`, a different site). Compare each preview card's domain with the intended URL. A trailing slash does not fix it. What works: put the cursor at the end of the link line, `shift+Home` to select it, `cmd+x`, `cmd+v`; the pasted text is linkified whole (`https://tokogame.ai.id/` all blue). Do this for every link on an unusual TLD (`.ai.id`, `.co.id`) and re-check in a zoomed screenshot.
4. Set the schedule only if the author asked for it.
5. Take a screenshot of the full composer and show it.
6. The tab group is deleted when its last tab is closed, and tabs the author opened themselves are outside it and cannot be driven. Open the composer in your own tab (`find` the "New thread" button ref) unless the author moves their tab into the group.
7. **Stop.** Never press Post or Schedule. The author checks and presses it.

## 6. After posting: spokes

For each spoke, quote the matching post, write a new hook, and give 3 to 5 points from the material listed in the spoke table. Suggested pace: first spoke two days after the hub, then every 2 to 3 days.

## Worked example (summary)

A 93-second football explainer Short. Nine posts: opening with video link; script from an AI script site (manual free mode) then copied to Claude, planning in Opus and executing in Sonnet; palette from Brandfetch and a visual concept skill; a US$ figure the author computed from the official regulation PDF, plus a fact-check rule added to CLAUDE.md; ElevenLabs voice with numbers spelled as spoken; HyperFrames render with cue-word timing; visual QA loop with scores 80, 86, 89, 90 (pass at 90) shown in a bar chart image; copy written with a copy skill and no-ai-slop; closing list of tool links. Images on posts 2 and 7. It took ten plan rounds by hand; the rules above are what those rounds corrected.
