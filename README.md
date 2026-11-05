# claude-skills

Personal [Claude Code](https://claude.com/claude-code) skills, shared so others can use them.

## Skills

| Skill | Use when |
|---|---|
| [mirroring-reference-video](mirroring-reference-video/SKILL.md) | Someone shares a reference video, ad, Reel, Short or TikTok and wants their own video to follow its structure, pacing or visual style |
| [writing-platform-copy](writing-platform-copy/SKILL.md) | A finished video or post needs titles, captions, descriptions, tags or pinned comments for YouTube, TikTok, Instagram, Facebook, X, Threads or LinkedIn, in everyday language |

## Install

Clone this repo, then link or copy a skill folder into your Claude Code skills directory:

```bash
git clone https://github.com/adimaulanat/claude-skills.git ~/claude-skills
ln -s ~/claude-skills/mirroring-reference-video ~/.claude/skills/mirroring-reference-video
ln -s ~/claude-skills/writing-platform-copy ~/.claude/skills/writing-platform-copy
```

Start a new Claude Code session; the skill then shows up in the skill list.

## How the skills work

Skills here are generic. They never assume your tools, look, language or format: each one reads your project's own instruction files first and asks you about anything those files do not answer. For `mirroring-reference-video`, a project can make this faster by documenting its design system, scaffold and render commands, voice tool, and where raw and private media go. For `writing-platform-copy`, document your language and voice, banned phrases, link and affiliate rules, and where the copy file lives.

## License

MIT, see [LICENSE](LICENSE).
