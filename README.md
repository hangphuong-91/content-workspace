# Marketing Content Workspace — 6-Skill Claude Code System

**Version:** 1.0.0  
**Created:** 2026-05-10  
**Repository:** https://github.com/hangphuong-91/content-workspace

A complete, production-ready Claude Code workspace for content marketing teams. 6 interconnected skills + external integrations (Notion, Google Drive, Canva, GitHub) = end-to-end content machine.

---

## 🎯 What This Workspace Does

Transform a content brief into a **3-month executed content strategy**:

```
Research Competitors → Analyze Platform Algorithms → Create Content Plan 
→ Build SOP for Production → Write Copy (Copywrite) → Design Visuals (Visual Creative)
```

Perfect for:
- Solo content creators / solopreneurs
- Small marketing teams needing automation
- Agencies wanting a repeatable playbook
- Content handoff & knowledge sharing

---

## 📦 6 Core Skills

| Skill | Command | What it does | When to use |
|---|---|---|---|
| **Content Plan** | `/content plan [topic]` | 3-month strategy: analysis, personas, calendar, tracking | Start here — orchestrator |
| **Competitor Research** | `/competitor research [brand]` | Audit competitors, find gaps, SWOT | Before content plan |
| **Platform Algorithm** | `/platform algorithm [platform]` | Real-time algorithm intel from official sources | Before content plan |
| **Copywrite** | `/copywrite [platform] [brief]` | Platform-specific copy × 3 A/B variations | Produce content weekly |
| **Visual Creative** | `/visual creative [brief]` | Design briefs, AI prompts, Canva design | Produce visuals weekly |
| **AI Execution** | `/ai execution [plan-file]` | Turn plan into SOP + weekly queue + repurposing tree | Operations & handoff |

---

## 🚀 Quick Start (5 minutes)

### Step 1: Setup Skills

Follow: **[.claude/SKILLS-SETUP.md](./.claude/SKILLS-SETUP.md)**

TL;DR:
```bash
# Copy skills folder
cp -r .claude/skills ~/.claude/skills
cp .claude/skills-manifest.json ~/.claude/

# Restart Claude Code
# Type / to see all 6 skills
```

### Step 2: Connect External Tools

Required MCPs:
- Notion (content tracking)
- Google Drive (file storage)
- Canva (design generation)
- GitHub CLI (version control)

### Step 3: Run Workflow

```bash
/competitor research "your brand"
/platform algorithm facebook
/content plan "your topic"
/ai execution
/copywrite facebook "brief"
/visual creative "visual brief"
```

---

## 📚 What's Included

### Skills (6 files)
- `content-plan.md` — Orchestrator, 5 phases, 3-month calendar
- `competitor-research.md` — Audit, gap analysis, SWOT
- `platform-algorithm.md` — Fresh algorithm intel per platform
- `copywrite.md` — Platform-specific frameworks + 24 cognitive biases
- `visual-creative.md` — 3-step process: brief → AI prompts → Canva
- `ai-execution.md` — SOP, tool matrix, repurposing tree

### Supporting Files (19 templates & guides)
- Templates: brief, plan, tracking, audit, SOP
- Frameworks: social media, email, blog, ads copywriting
- Guides: brand voice, platform specs, AI prompts, Canva, compliance

### Test Outputs
- Case: Personal brand for private OB/GYN doctor (Vietnam)
- Sequence: competitor audit → content plan → SOP → sample copy & visuals

---

## 💡 How It Works

### For Solo Creators
1. Week 1: `/content plan` → get 3-month strategy
2. Week 2: `/ai execution` → get weekly SOP
3. Each week: `/copywrite` + `/visual creative`

**Result:** 5-7 pieces/week, 80% faster planning

### For Small Teams
1. Manager: quarterly `/content plan` + `/ai execution`
2. Writers: use `/copywrite` daily
3. Designers: use `/visual creative` daily
4. Hand-off: SOP detailed for non-Claude-Code users

### For Agencies
1. Onboarding: `/competitor research` → landscape analysis
2. Proposal: `/content plan` → 3-month roadmap
3. Execution: `/ai execution` → repeatable SOP
4. Quarterly: `/platform algorithm` → stay current

---

## 🔧 Key Features

✅ **5-Phase Content Planning:** Situation Analysis → Strategic Foundation → Messaging → Calendar → Tracking

✅ **OPE Framework:** Owned/Paid/Earned channel strategy matrix

✅ **Psychology-Based Copy:** 24 cognitive biases mapped to copy approaches

✅ **Bias × Funnel Stage Matrix:** Which biases work best at each stage

✅ **Quick Mode:** Get output instantly for time-sensitive content

✅ **Full Mode:** Deep analysis for strategic decisions

✅ **SOP Generator:** Hand-off ready for delegation

✅ **Canva Integration:** Auto-generate visuals with brand kit

✅ **Notion Tracking:** Content status dashboard

✅ **Compliance Built-In:** Notes for regulated industries (healthcare, finance)

---

## 📋 Folder Structure

```
content-workspace/
├── README.md ← You are here
├── skills/
│   ├── content-plan.md
│   ├── competitor-research.md
│   ├── platform-algorithm.md
│   ├── copywrite.md
│   ├── visual-creative.md
│   ├── ai-execution.md
│   └── [supporting templates & frameworks]
├── .claude/
│   ├── skills-manifest.json
│   ├── SKILLS-SETUP.md ← Installation guide
│   └── skills/ ← Copy to ~/.claude/skills
├── outputs/
│   └── [brand-YYYY-MM]/
│       ├── content-plan.md
│       ├── competitor-audit.md
│       ├── ai-execution-sop.md
│       └── tracking.md
└── exports/
    └── chat-history.txt
```

---

## ⚡ Quick Commands

```bash
# Workflow sequence (in order)
/competitor research "your brand"
/platform algorithm facebook
/platform algorithm tiktok
/content plan "your topic"

# From plan
/ai execution

# Weekly production
/copywrite facebook "brief"
/copywrite email "newsletter"
/visual creative "graphic brief"

# Quick mode (instant, no questions)
/copywrite facebook "brief" --quick
/content plan "topic" --quick
```

---

## 🧪 Test Case: OB/GYN Doctor

Workspace tested with: **Personal brand for private OB/GYN physician (HCMC)**

Run this sequence to verify setup:
```bash
/competitor research "phòng khám sản phụ khoa tư nhân TPHCM"
/platform algorithm facebook
/platform algorithm tiktok
/content plan "Personal brand bác sĩ sản phụ khoa tư nhân"
/ai execution content-outputs/bacsi-sanphukhoa-2026-05/content-plan.md
/copywrite facebook "Bài giáo dục sức khỏe thai kỳ tuần 28"
/visual creative "Infographic thai kỳ tuần 28 cho Facebook"
```

---

## 📖 Full Documentation

- **[SKILLS-SETUP.md](./.claude/SKILLS-SETUP.md)** — Install & register skills
- **[skills/content-plan.md](./skills/content-plan.md)** — Full 5-phase workflow
- **[skills/copywrite.md](./skills/copywrite.md)** — Cognitive bias mapping
- **[skills/visual-creative.md](./skills/visual-creative.md)** — AI prompt templates

---

## 🎓 Frameworks Included

- **OPE Matrix:** Owned/Paid/Earned channels with % split
- **Funnel Alignment:** Awareness → Consideration → Conversion → Retention
- **Cognitive Biases:** 24 biases × platform-specific copy techniques
- **SUME-Kit Patterns:** Strategic insight filtering, leverage discovery, stress-testing
- **Think-Kit Patterns:** Hard stop rules, transparency, cognitive awareness
- **Repurposing:** 1 pillar → 5-7 derivative pieces (80/20 optimization)

---

## ✅ Checklist to Get Started

- [ ] Clone repo: `git clone https://github.com/hangphuong-91/content-workspace`
- [ ] Read [SKILLS-SETUP.md](./.claude/SKILLS-SETUP.md)
- [ ] Copy skills to Claude Code
- [ ] Setup Notion MCP
- [ ] Setup Google Drive MCP
- [ ] Setup Canva MCP
- [ ] Install GitHub CLI
- [ ] Run test case with `/competitor research`
- [ ] Check outputs folder

---

## 🤝 Contributing

Found a bug? Improvement idea?

1. Fork repo
2. Create branch: `git checkout -b feature/improve-copywrite`
3. Edit skill files
4. Test with sample brief
5. Submit PR

Or open issue: [GitHub Issues](https://github.com/hangphuong-91/content-workspace/issues)

---

## 📄 License

MIT — use freely, modify, share

---

**Built with Claude Code × Think-Kit + SUME-Kit Patterns**  
**v1.0.0 | 2026-05-10**
