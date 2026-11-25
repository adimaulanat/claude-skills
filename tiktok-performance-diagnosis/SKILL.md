---
name: tiktok-performance-diagnosis
description: Diagnose why a TikTok account's videos don't get views or retention: read TikTok Studio, verify fixes against viral videos in Creator Search Insights, propose hooks.
---

# TikTok performance diagnosis + CSI verification

Use when the user asks why their TikTok content doesn't reach views / doesn't hold viewers, wants hook ideas for their niche, or wants suggestions checked against viral content. Works for any account the user is signed into in Chrome.

Reply in the user's language (casual Indonesian "kamu" if they write Indonesian). Never invent numbers; every claim names where it came from (TikTok Studio, CSI topic name, project doc).

## Phase 0 — Context (silent)
- If a project or repo for this account exists, read its instructions and the latest evaluation/brief docs: niche, pillars, current hook rules, past A/B results. Note rules you may contradict later.
- If none exists, ask only for: account niche and target audience (one question).

## Phase 1 — Read TikTok Studio (browser, user's tab)
1. `tiktok.com/tiktokstudio/analytics` → Overview: views, profile views, likes, shares, followers, **traffic source** (% For You vs Search), search queries.
2. Content tab → list of posts with views.
3. Open 4–6 posts (top, middle, worst) via "View data". For each, zoom the metric row and record: duration, views, **average watch time**, **watched full video %**, new followers, and the retention note ("Most viewers stopped watching at 0:0X").
4. Compute avg watch time ÷ duration. Build a table: video | duration | views | avg watch (% of length) | full % | new followers.
5. Also read each caption for self-undermining lines ("aku nggak tes sendiri", AI voice disclosure as the first line, etc.).

Diagnostic rules of thumb:
- High For You % + low avg watch → TikTok is distributing; the first second fails (visual at frame 0).
- Drop at 0:01 → frame 0 is not a scroll-stopper; fix visuals before wording.
- Avg watch far below length → too long for the content type, or no re-hooks.
- Followers ≈ 0 per 1K views → niche too scattered or no reason to follow.
- Many topics/pillars in one week → the algorithm can't classify the audience.
- Decisions from tests with <100 views per variant → noise; say so.

## Phase 2 — First diagnosis (reply)
- Lead with the one main problem in one sentence.
- Data table, then numbered problems (each tied to a number from Phase 1).
- 3 hook patterns for the niche: pattern + one concrete example line. Label them as hypotheses until verified.
- Other quality fixes (footage, length, voice, niche focus, posting volume, search keywords, target metrics: ≥60% still watching at 3 s, avg watch ≥50% of length).
- Flag any suggestion that contradicts the project's current rules and ask before changing docs.

## Phase 3 — Verify against viral content in CSI
1. Open `tiktok.com/csi`. For each content pillar of the account, search 1 topic keyword (use the account's own search queries / product names; local-language terms). Pick a topic with real popularity (≥ ~5K) — skip ones at 0–100.
2. Open the topic detail, note popularity, growth %, location %, then scroll to **Related videos** and screenshot the row (use the next arrow if needed). Cover 3–5 topics, ~15–25 videos total.
3. For each video note: what is at frame 0 (face / hand + real product / real event footage / drawn graphics / gameplay), on-screen text, title wording, likes, date, first-person vs summary, format devices (comment-reply bubble, split screen, price overlay).
4. Also note topics the account covers but **can't film** (e.g. viral videos all use gameplay the creator doesn't have).

## Phase 4 — Verification reply
- State limits first: CSI shows covers, titles and likes only — no views, retention or duration; videos were not watched.
- Summary line: X confirmed, Y partly, Z replaced, N new findings.
- Table: suggestion | verdict (✅ confirmed / ⚠️ partly or needs correction / ❌ not supported) | evidence (pattern description, likes, topic).
- Correct suggestions the evidence contradicts (e.g. length is fine for storytelling).
- New findings not in the original suggestions.
- Revised 3 hooks, each tied to a winning pattern seen in CSI, examples written for the user's niche and only claims they can truly make.
- Run every revised hook (and the account's current default hook) through the hook critique below before sending.
- Don't name or copy other creators' videos in the user's content; describe patterns.

## Hook critique (run on every hook you propose or keep)
Adapted from the checklist and anti-patterns in vyralcontent/content-skills `viral-hooks` (MIT). Those are creator heuristics without data; when they conflict with the account's TikTok Studio numbers or CSI evidence, the numbers win and you say so.

Core pass/fail (rewrite if any fails):
- Spoken in ≤ 2 s (count words; Indonesian ≈ 3 words/s, so ≤ ~6–7 words).
- Leads with the payoff or the stake, not setup, brand or a yes/no question the viewer can answer in their head.
- Concrete noun, number or named stake in the first half.
- The promise is true and the body pays it off. A first-person claim ("pakai sebulan") only if the creator really did it; otherwise it's bait-and-switch.

Three layers, all pointing at the same idea:
- **Visual** works on mute: frame 0 readable at a glance, real and moving. If the creator can't film it, the hook is at most one-third strong; say so.
- **Verbal** works without the picture.
- **On-screen text** 3–7 words that sharpen the spoken line, not repeat it; upper-third/center, clear of TikTok's bottom and right UI.

Anti-patterns to name explicitly: welcome/logo/channel intro · vague tease · bait-and-switch · follow/subscribe ask before value · chronological story opener (fix: open on the most arresting moment, then walk back) · imperative command whose payoff doesn't earn it · cleverness that needs decoding · slow build-up (cut the first sentences) · hook that takes > 3 s to resolve · single-layer hook.

Fast upgrades: add an odd, specific number · authority signal in the first half-second · name the exact viewer (e.g. price class) · cut the first three words · state the consensus, then break it.

Also check and report:
- **Font:** creator heuristic says custom brand fonts can read as an ad and TikTok's native font as native. Unproven; if the account uses a heavy custom look, propose an A/B on the cover text rather than a rule.
- **Batch, not a line:** for a new idea, 6–10 hooks across ≥ 3 archetypes before the script. If no credible hook can be written, flag the idea (often: the creator can't film it), not the wording.
- **Pattern:** if the same failure repeats across hooks (often the visual layer), name it as one habit.

Output: table hook | verdict ✅/⚠️/❌ | which check failed or anti-pattern | rewrite (fixed version + one alternate).

## Phase 5 — Offer to persist
Offer (don't do unasked): save the verification as a project doc, update the hook rules in the project instructions, and draft 3 test briefs — noting which require the user to record real footage.

## Don'ts
- Don't change account settings, post, or comment.
- Don't treat likes as views, or one video as a proven rule.
- Don't recommend topics the user can't film or source honestly.
