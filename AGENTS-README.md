# AGENTS-README.md — 3 Specialized Agents

**Version:** 2.0.0  
**Updated:** 2026-05-14

---

## 🎬 Overview

Marketing Content Workspace v2 uses **3 specialized agents**, each with a distinct role in the content strategy → execution pipeline.

```
Communication Strategist (CMO)
    ↓ Input: Brand + Market context
    ↓ Output: Strategy docs + GPT analysis
    ↓
Content Planner (Strategy orchestrator)
    ↓ Input: Communication plan
    ↓ Output: 3-month calendar + Excel templates
    ↓
Content Execution (Production operator)
    ↓ Input: Content plan
    ↓ Output: Copy + visuals + reports
    ↓
[Measure & Optimize]
```

---

## 1️⃣ AGENT 1: Communication Strategist

**Role:** CMO — Nghiên cứu + định vị + đúc kết insights  
**Defines:** Strategy, positioning, messaging, tone of voice  
**Cadence:** Quarterly (once every 3 months)  
**Automation:** 95% (chỉ cần user approve insights)  
**Time commitment:** 3-4 hours per quarter

### Input Requirements

Before starting, gather:
- **Brand document** (mission, values, positioning) — if available
- **Audience research** (personas, pain points) — if available  
- **Product/service brief** (what you do, how you're different)
- **Market context** (industry trends, timing)
- **Competitor data** (from `/competitor research` or user input)

### Workflow — 6 Phases + Bias Check

```
PHASE 0: Input Gathering (MANUAL)
  └─ User provides documents OR Agent runs /competitor research + /market-intelligence
  └─ Confirmation: "Ready to proceed?"

PHASE 0.5: Stakeholder Alignment (AUTO)
  └─ /stakeholder-alignment [brand]
  └─ Output: Risk check (Stakeholder map, Compliance, PR risks)
  └─ Verdict: GO / HOLD / BLOCKED
  └─ [If HOLD → STOP until resolved]

PHASE 1: Research Gaps (AUTO)
  ├─ If missing competitor data: /competitor research [brand]
  │  ├─ WebSearch + WebFetch
  │  ├─ Calls GPT o1 for deep analysis (if OPENAI_API_KEY set)
  │  └─ Output: competitor-audit.md + gpt-competitor-analysis.json
  │
  └─ If missing market data: /market-intelligence [brand] [month]
     ├─ SEO keywords + algorithm updates + competitor pulse
     ├─ Calls GPT o1 for synthesis (if OPENAI_API_KEY set)
     └─ Output: market-intelligence.md + gpt-market-synthesis.json

PHASE 2: Distill Insights (AUTO)
  └─ /distill-insights [all data]
  └─ Output: 5 strategic insights + 1 meta-pattern (all with evidence)
  └─ [USER REVIEW: Any surprises?]
  └─ [Bias check: Confirmation bias, Anchoring, Halo effect, Optimism, Groupthink]

PHASE 3: Build Message House (AUTO)
  └─ /message-house [insights + brand context]
  └─ Output: Brand Promise + 3-5 Message Pillars + Funnel map + Persona map

PHASE 3.5: Tone & Voice Calibration (AUTO)
  └─ /tone-voice [message house + personas]
  └─ Output: Voice archetype, attributes, tone per channel, red lines

PHASE 3.7: Competitive Positioning Validation (AUTO)
  └─ /competitive-positioning [brand + competitors + message house]
  └─ Output: Positioning map + Message overlap analysis + Risks
  └─ Verdict: STRONG / ADEQUATE / NEEDS WORK
  └─ [If NEEDS WORK → Adjust Phase 3, retry]

PHASE 4: Channel Strategy (AUTO)
  └─ Build OPE matrix (Owned/Paid/Earned)
  └─ Assign frequency per channel (default: FB 3x/week, TikTok 2x/week)

PHASE 4.5: Campaign Themes (AUTO)
  └─ /campaign-themes [brand + year/quarter]
  └─ Output: Quarterly themes + hero campaigns + seasonal hooks

PHASE 5: High-Level Calendar (AUTO)
  └─ 3-month outline (no week-by-week detail yet)

PHASE 6: Handoff Brief (AUTO)
  └─ Generate comm-to-content-handoff.md
  └─ Ready for Content Planner to consume
```

### Outputs (8 files)

**Strategic Documents (.md):**
1. `communication-plan.md` — Executive summary of all 6 phases
2. `message-house.md` — Brand Promise + pillars + funnel map
3. `tone-voice-guide.md` — Voice archetype, tone per channel, red lines
4. `positioning-map.md` — Competitive positioning matrix
5. `campaign-themes-[year].md` — Quarterly themes + hero campaigns
6. `stakeholder-risk-check.md` — Risk assessment + verdict
7. `handoff-to-content-planner.md` — Brief for Content Planner (uses template)

**Data Files (.json):**
8. `gpt-competitor-analysis.json` (if OpenAI available)
9. `gpt-market-synthesis.json` (if OpenAI available)

### Hard Rules

- ❌ Never deliver without Phase 3.7 validation (if verdict NEEDS WORK, adjust & retry)
- ❌ Never deliver without tone & voice guide (even if basic)
- ❌ Never skip Phase 0.5 (stakeholder check) even if user says "quick"
- ❌ Never assume messaging without evidence — mark as "gap" if data missing
- ❌ Never continue after HOLD verdict without user approval

---

## 2️⃣ AGENT 2: Content Planner

**Role:** Strategy execution orchestrator — Biến strategy thành 3-month calendar + production SOP  
**Defines:** Content calendar, KPI targets, production allocation  
**Cadence:** Quarterly planning + weekly KPI review  
**Automation:** 85% (auto-generate calendar, manual approval of strategy)  
**Time commitment:** 2-3 hours per quarter + 30 min per week (KPI check)

### Input Requirements

**Must have:**
- `communication-plan.md` from Communication Strategist (non-negotiable)
- `tone-voice-guide.md` for writing style rules
- `message-house.md` for content pillars

**Nice to have:**
- `gpt-market-synthesis.json` for market opportunities
- `gpt-competitor-analysis.json` for competitor insights
- Any previous content performance data (Notion database)

### Workflow

```
PHASE 0: Input Validation (AUTO)
  ├─ Parse communication-plan.md
  ├─ Extract:
  │  ├─ Message Pillars → Content Pillars
  │  ├─ Channel strategy → Content frequency
  │  ├─ Campaign themes → Quarterly hooks
  │  └─ Tone & Voice → Writing style guide
  │
  └─ Read gpt-market-synthesis.json
     └─ Extract top 3 opportunities

PHASE 1: Build Strategic Calendar (AUTO)
  ├─ Create 12-week outline
  ├─ Assign content pillar per week
  ├─ Assign hero channel per month
  ├─ Set posting frequency (default: FB 3x/week, TikTok 2x/week)
  ├─ Add gpt-market opportunities
  └─ Map KPI targets per channel

PHASE 2: Generate Excel Templates (AUTO)
  ├─ Sheet 1: Strategic Calendar
  │  ├─ Columns: Week | Month | Pillar | Hero Channel | Format | Angle | Persona | CTA | Status
  │  └─ 12 rows (1 per week)
  │
  ├─ Sheet 2: KPI Benchmark
  │  ├─ Columns: Channel | Reach Target | ER% Target | Bài/Tháng | Format
  │  └─ 5 rows (Facebook, TikTok, Instagram, LinkedIn, Email)
  │
  └─ Sheet 3: Production Allocation
     ├─ Columns: Week | Pillar | Format | Hero? | AI Tool | Time Est. | Owner | Notes
     └─ Maps all 36-48 content pieces

PHASE 3: Notion Sync (AUTO if connected)
  ├─ Create database: [Brand] Content Calendar Q[X] [YYYY]
  ├─ Properties:
  │  ├─ Title (content idea)
  │  ├─ Week (1-12)
  │  ├─ Pillar (select)
  │  ├─ Channel (select)
  │  ├─ Format (select)
  │  ├─ Status (Planned → In Prod → Approved → Published → Measured)
  │  ├─ Reach (number)
  │  ├─ Engagement % (number)
  │  └─ Link to assets (URL)
  │
  └─ Auto-populate 36-48 rows

WEEKLY KPI REVIEW (Every Monday)
  ├─ Read previous week's /weekly-report
  ├─ Compare actual KPI vs benchmark:
  │  ├─ Reach (flag if < 50% target)
  │  ├─ ER% (flag if < 70% target)
  │  └─ Frequency (flag if missed schedule)
  │
  └─ Decide: Continue as-is OR adjust next week's strategy
```

### Outputs (4 files)

**Planning Documents:**
1. `content-plan.md` — Executive summary of strategy + calendar overview
2. `strategic-calendar-[brand].xlsx` — Weekly breakdown for 12 weeks
3. `kpi-benchmark-[brand].xlsx` — Channel targets + format recommendations
4. `production-allocation-[brand].xlsx` — Content piece assignments + tool mapping

**Plus:**
5. Notion database (if connected) with 36-48 content entries

### Quality Gates

- ✅ Calendar must have 12 weeks mapped (no gaps)
- ✅ Each week must have pillar + channel + format assigned
- ✅ Frequency must match Communication Strategist targets (FB 3x/week, etc.)
- ✅ KPI benchmarks must be realistic (based on industry data)
- ✅ Notion database fully synced (if using)

---

## 3️⃣ AGENT 3: Content Execution

**Role:** Production operator — Viết bài + thiết kế + đăng bài + đo lường  
**Defines:** Copy variations, visual concepts, posting schedule, weekly metrics  
**Cadence:** Weekly (Monday-Sunday each week)  
**Automation:** 40% (copywrite + visual creative auto-generate), 60% (approvals + manual tasks)  
**Time commitment:** 4-5 hours per week (or 8-10 hours for pair work)

### Input Requirements

**Must have:**
- `content-plan.md` from Content Planner
- `strategic-calendar-[brand].xlsx` (weekly direction)
- `tone-voice-guide.md` (writing rules)

**Use for reference:**
- `platform-algorithm-[platform].md` (generated fresh each week from WebSearch)
- Notion database (for status tracking)

### Weekly Workflow

```
MONDAY (Thứ 2) — Planning & Research
├─ 🤖 /platform algorithm [facebook]
│  └─ Search latest Facebook algorithm updates
│  └─ Output: algorithm-cheat-sheet.md (temp reference)
│
├─ 🤖 /platform algorithm [tiktok]
│  └─ Search latest TikTok algorithm
│  └─ Output: algorithm-cheat-sheet.md (temp reference)
│
└─ Read: strategic calendar for week [X]
   ├─ Hero channel: [Facebook / TikTok]
   ├─ Content pillar: [Pillar name]
   ├─ Format: [video/carousel/text]
   ├─ Angle: [specific angle]
   └─ Target persona: [Persona name]

TUE-WED (Thứ 3-4) — Copywriting
├─ 🤖 /copywrite [platform] [brief]
│  ├─ Input brief:
│  │  ├─ Platform: facebook (or hero channel)
│  │  ├─ Pillar: [from calendar]
│  │  ├─ Angle: [from calendar]
│  │  ├─ Target persona: [from communication-plan]
│  │  ├─ CTA: [from message pillars]
│  │  └─ Tone: [from tone-voice-guide]
│  │
│  ├─ Generate: 3 variations
│  │  ├─ V1: Story-driven angle
│  │  ├─ V2: Data-driven angle
│  │  └─ V3: Community-engagement angle
│  │
│  └─ Output: copywrite-[platform]-W[X].md
│     └─ Contains: [Brief] + [V1] + [V2] + [V3]
│
└─ ⏸️ MANUAL: Review & choose best variation
   └─ Save chosen copy (V1/V2/V3) for asset approval

THU (Thứ 4-5) — Visual Creative
├─ ⏸️ MANUAL: Research visual inspiration
│  ├─ Open: Behance.com / Pinterest
│  ├─ Search: [angle] + [format]
│  ├─ Screenshot: 3-5 best references
│  └─ Save folder: visual-refs-W[X]/
│
├─ Create visual brief (MANUAL + AI support)
│  ├─ Concept: [1-2 sentences visual direction]
│  ├─ Composition: [layout description]
│  ├─ Color mood: [primary colors]
│  ├─ Typography: [headline style]
│  └─ References: [links to Behance/Pinterest]
│  └─ Output: visual-brief-W[X].md
│
├─ 🤖 /visual creative [brief]
│  ├─ Input:
│  │  ├─ Visual brief file
│  │  ├─ Copy (from chosen variation)
│  │  └─ Brand colors/fonts (from tone-voice-guide)
│  │
│  ├─ Generate:
│  │  ├─ Creative concept (text)
│  │  ├─ AI image prompt (Midjourney/DALL-E)
│  │  └─ Canva brief (description, not execution)
│  │
│  └─ Output: ai-prompts-W[X].md
│     └─ Contains: [Concept] + [AI Prompt] + [Canva brief]
│
└─ ⏸️ MANUAL: If using Canva
   ├─ Open Canva (or use competitor's design tool)
   ├─ Execute brief manually
   ├─ Export: PNG/MP4/PDF
   └─ Save: assets-W[X]/[format]/[final-asset]

FRI (Thứ 5-6) — Approval & Scheduling
├─ ⏸️ MANUAL: Final QA before posting
│  ├─ Verify: Copy matches tone-voice-guide?
│  ├─ Verify: Visual matches brief?
│  ├─ Verify: CTA clear + clickable?
│  ├─ Check: Compliance (if healthcare/finance)?
│  └─ Status: Mark Notion as "Approved"
│
└─ ⏸️ MANUAL: Set posting date/time
   ├─ Best time per platform: [from algorithm notes]
   ├─ Facebook: Morning (7-9 AM) or evening (6-8 PM)
   ├─ TikTok: Evening (6-10 PM) or early morning (8-10 AM)
   ├─ Schedule tool: Buffer / native platform scheduler / manual post
   └─ Status: Mark Notion as "Published"

SAT-SUN (Thứ 6-7) — Monitoring & Weekly Report
├─ Monitor posts (optional)
│  ├─ Respond to comments (if team resource available)
│  └─ Note patterns (what works, what doesn't)
│
├─ 🤖 /weekly-report [brand] [week]
│  ├─ Input required (MANUAL):
│  │  ├─ Posts published count per channel
│  │  ├─ Reach numbers from Buffer/Meta Business Suite
│  │  ├─ Engagement rate per post
│  │  ├─ Comments + shares
│  │  └─ Copy to Excel Execution Log
│  │
│  ├─ Process:
│  │  ├─ Read Excel inputs
│  │  ├─ Calculate vs KPI benchmark
│  │  ├─ Flag underperformers (Reach < X, ER < Y%)
│  │  ├─ Update Notion: Status → "Measured"
│  │  └─ Generate weekly-summary-W[X].md
│  │
│  └─ Output: weekly-summary-W[X].md
│     └─ Contains:
│        ├─ Posts published summary (4-6 per week)
│        ├─ Reach totals per channel
│        ├─ ER% per post vs KPI
│        ├─ Top 3 performing content
│        ├─ Underperformers (if any)
│        └─ Recommendations for next week
│
└─ 📤 Send report to Content Planner
   └─ If KPI gap > 20% → Planner may adjust strategy
```

### Outputs (Weekly)

**Writing Documents (.md):**
1. `copywrite-[platform]-W[X].md` — Brief + 3 variations
2. `visual-brief-W[X].md` — Research + concept + references
3. `ai-prompts-W[X].md` — AI image prompts + Canva brief
4. `weekly-summary-W[X].md` — Metrics + narrative report

**Tracking (.xlsx):**
5. `execution-log-[brand].xlsx` — Ongoing metrics tracker (updated weekly)

**Notion updates:**
6. Status updates per content piece (Planned → In Prod → Approved → Published → Measured)
7. Reach + ER% filled in after publishing

---

## 🔄 Agent Handoff Process

### **Communication Strategist → Content Planner**

**When:** After Phase 6 complete (all 8 .md files + 2 .json files ready)

**What to hand off:**
```
Folder: outputs/[brand]-[YYYY-MM]/
├─ communication-plan.md ← Content Planner reads this
├─ message-house.md ← Extract pillars
├─ tone-voice-guide.md ← Extract writing rules
├─ positioning-map.md ← Reference
├─ campaign-themes-[year].md ← Extract quarterly hooks
├─ gpt-competitor-analysis.json ← Nice to have
└─ gpt-market-synthesis.json ← Extract opportunities
```

**Communication:** "Communication plan [Brand] complete. Ready for Content Planner to build calendar."

---

### **Content Planner → Content Execution**

**When:** After 3 Excel templates created + Notion synced

**What to hand off:**
```
Files:
├─ content-plan.md ← Execution reads for overview
├─ strategic-calendar-[brand].xlsx ← Weekly reference (THE KEY FILE)
├─ kpi-benchmark-[brand].xlsx ← KPI targets
└─ production-allocation-[brand].xlsx ← Tool mapping

Notion database:
└─ [Brand] Content Calendar Q[X] [YYYY] with 36-48 entries
```

**Communication:** "Content plan [Brand] ready. Execution starts Monday of Week 1. See strategic-calendar for weekly direction."

---

### **Content Execution → Content Planner (Weekly)**

**When:** End of week (Saturday or Sunday)

**What to hand off:**
```
Files:
├─ weekly-summary-W[X].md ← Narrative report
└─ execution-log-[brand].xlsx ← Updated metrics

Data:
├─ Reach per post
├─ ER% per post
├─ Frequency achieved (4-6 posts per week? Y/N)
└─ Any compliance issues
```

**Communication:** "Week [X] report attached. KPI on track / KPI gap detected [metric] — recommend [action]."

---

## ⚙️ Technical Setup

Each agent defined in `.claude/agents/`:
- `communication-strategist.md` — Agent 1 definition + phases + tools
- `content-planner.md` — Agent 2 definition + workflow
- `content-execution.md` — Agent 3 definition + weekly schedule

Registration: `.claude/agents/agents-manifest.json`

---

## 🎓 Example Prompts

### For Communication Strategist
```
/stakeholder-alignment "Phòng khám sản phụ khoa tư nhân TPHCM"
/competitor research "phòng khám sản phụ khoa"
/market-intelligence "bacsi-sanphukhoa" "2026-05"
/content plan "Thương hiệu cá nhân bác sĩ sản phụ khoa"
```

### For Content Planner
```
# Make sure communication-plan.md exists in outputs folder first
/content plan "Sản phụ khoa"
```

### For Content Execution
```
/platform algorithm facebook
/copywrite facebook "Bài giáo dục thai kỳ tuần 28 — angle khoa học"
/visual creative "Infographic thai kỳ tuần 28 — pastel colors + infographic style"
/weekly-report "bacsi-sanphukhoa" "W1"
```

---

**Related:** [README.md](./README.md), [CLAUDE.md](./CLAUDE.md), [3-AGENTS-WORKFLOW-DIAGRAM.md](./3-AGENTS-WORKFLOW-DIAGRAM.md), [plan.md](./plan.md)
