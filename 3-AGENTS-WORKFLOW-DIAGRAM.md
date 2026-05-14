# 3 Agents Workflow — Diagrams & Automation Points

## 📊 High-Level Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                      MARKETING CONTENT WORKSPACE v2                  │
│                    3 Agents + OpenAI Deep Research                   │
└─────────────────────────────────────────────────────────────────────┘

                            INPUT
                              ↓
           [Brand Info + Business Goals + Market Context]
                              ↓
        ┌─────────────────────────────────────────────┐
        │   AGENT 1: Communication Strategist         │
        │   Role: CMO — Strategy & Positioning        │
        │   Cadence: Hàng quý (3 tháng)               │
        │                                             │
        │   Phases: 0→0.5→1→2→3→3.5→3.7→4→4.5→5→6   │
        │                                             │
        │   🤖 Automation:                            │
        │   • /stakeholder-alignment (auto)           │
        │   • /competitor research (auto → GPT)       │
        │   • /market-intelligence (auto → GPT)       │
        │   • /distill-insights (auto)                │
        │   • /message-house (auto)                   │
        │   • /tone-voice (auto)                      │
        │   • /competitive-positioning (auto)         │
        │   • /campaign-themes (auto)                 │
        │                                             │
        │   📤 Output:                                │
        │   ├── communication-plan.md                 │
        │   ├── message-house.md                      │
        │   ├── tone-voice-guide.md                   │
        │   ├── positioning-map.md                    │
        │   ├── campaign-themes.md                    │
        │   ├── gpt-competitor-analysis.json          │
        │   └── gpt-market-synthesis.json             │
        └─────────────────────────────────────────────┘
                    [⏸️ MANUAL: User review]
                              ↓
        ┌─────────────────────────────────────────────┐
        │   AGENT 2: Content Planner                  │
        │   Role: Strategy execution plan             │
        │   Cadence: Đầu mỗi quý                      │
        │                                             │
        │   Input: communication-plan.md + market data│
        │                                             │
        │   🤖 Automation:                            │
        │   • /content plan (reads communication data)│
        │   • Parse comm plan + GPT insights          │
        │   • Check KPI benchmarks vs market          │
        │   • Generate 3-month calendar               │
        │   • Sync to Notion (if available)          │
        │                                             │
        │   📤 Output:                                │
        │   ├── content-plan.md                       │
        │   ├── content-calendar.xlsx                 │
        │   ├── kpi-benchmark.xlsx                    │
        │   ├── production-allocation.xlsx            │
        │   └── Notion database entries               │
        └─────────────────────────────────────────────┘
                    [⏸️ MANUAL: User review]
                              ↓
        ┌─────────────────────────────────────────────┐
        │   AGENT 3: Content Execution                │
        │   Role: Produce + post + measure            │
        │   Cadence: Hàng tuần (Thứ 2-7)              │
        │                                             │
        │   Input: content-plan.md                    │
        │                                             │
        │   🤖 Automation:                            │
        │   • /platform algorithm (auto search)       │
        │   • /copywrite (semi-auto → manual approve) │
        │   • /visual creative (semi-auto → Canva)    │
        │                                             │
        │   ⏸️ MANUAL STEPS:                          │
        │   • Approve copy variations                 │
        │   • Research Behance/Pinterest (visual)     │
        │   • Create concept brief (AI prompts)       │
        │   • Review final assets                     │
        │   • Set posting date + schedule manually    │
        │                                             │
        │   📤 Output:                                │
        │   ├── copywrite-[platform]-[week].md        │
        │   ├── visual-brief-[week].md                │
        │   ├── ai-prompts-[week].md                  │
        │   ├── Notion: Status updates                │
        │   ├── Excel: Execution log                  │
        │   └── weekly-report.md                      │
        └─────────────────────────────────────────────┘
                              ↓
                    [📊 MEASURE & REPORT]
                              ↓
              [Buffer Analytics + Manual Input]
                              ↓
                    [⏸️ MANUAL: Content Planner]
                   [Điều chỉnh plan nếu cần]
```

---

## 🔄 Detailed Workflow — Each Agent

### **AGENT 1: Communication Strategist**

```
PHASE 0: Input Gathering (MANUAL)
│
├─ You provide: Brand doc, audience research, product brief, competitor data
├─ OR: Agent runs /competitor research + /market-intelligence
├─ Confirmation: "Đúng, bắt đầu đi"
│
PHASE 0.5: Stakeholder Alignment (AUTOMATED)
│
├─ /stakeholder-alignment [brand + context]
│  └─ Output: stakeholder-risk-check.md
│     ├─ Stakeholder map
│     ├─ Compliance risks
│     ├─ PR/timing risks
│     └─ Verdict: GO / HOLD / BLOCKED
│
├─ [If HOLD/BLOCKED] ⏸️ STOP — User must resolve
│
PHASE 1: Research Gaps (AUTOMATED)
│
├─ If missing competitor data:
│  └─ /competitor research [brand]
│     ├─ WebSearch + WebFetch
│     ├─ Calls GPT o1 (Phase 5.5)
│     └─ Output: competitor-audit.md + gpt-competitor-analysis.json
│
├─ If missing market/audience data:
│  └─ /market-intelligence [brand] [month]
│     ├─ SEO + algorithm + competitor pulse
│     ├─ Calls GPT o1 (Section 5)
│     └─ Output: market-intelligence.md + gpt-market-synthesis.json
│
PHASE 2: Distill Insights (AUTOMATED)
│
├─ /distill-insights [all data from Phase 0 + 1]
│  ├─ Extract 5 strategic insights + meta-pattern
│  └─ Output: distilled-insights.md
│
├─ [User confirms insights] ⏸️ REVIEW
│
PHASE 3: Build Message House (AUTOMATED)
│
├─ /message-house [insights + brand context]
│  ├─ Brand Promise + 3-5 Message Pillars
│  ├─ Funnel Message Map
│  └─ Output: message-house.md
│
PHASE 3.5: Tone & Voice (AUTOMATED)
│
├─ /tone-voice [message house + personas]
│  ├─ Voice Archetype + Attributes
│  ├─ Tone per Channel/Persona
│  └─ Output: tone-voice-guide.md
│
PHASE 3.7: Competitive Positioning (AUTOMATED)
│
├─ /competitive-positioning [brand + competitors + message house]
│  ├─ Positioning Map
│  ├─ Message Overlap Analysis
│  └─ Output: positioning-map.md
│
├─ [If NEEDS WORK] ⏸️ Adjust Phase 3 + retry
│
PHASE 4: Channel Strategy (AUTOMATED)
│
├─ Build OPE matrix
│  ├─ Owns: Facebook 3x/week, TikTok 2x/week, Blog 1x/week
│  ├─ Paid: Instagram ads nếu có budget
│  └─ Earned: Community, PR, partnerships
│
PHASE 4.5: Campaign Themes (AUTOMATED)
│
├─ /campaign-themes [brand + context + year/quarter]
│  ├─ Quarterly themes + hero campaigns
│  └─ Output: campaign-themes-[year].md
│
PHASE 5: Communication Calendar (HIGH-LEVEL)
│
├─ Tổng hợp 3-month outline
│  ├─ Quarterly milestones
│  ├─ Key campaign moments
│  └─ No week-by-week detail (→ Content Planner job)
│
PHASE 6: Handoff Brief (AUTOMATED)
│
├─ Generate comm-to-content-handoff.md
│  ├─ Content Planner Brief
│  ├─ Stakeholder Brief (optional)
│  └─ Sales Enablement Brief (optional)
│
└─ 📤 DELIVER to Content Planner
   └─ Files: 8 .md files + 2 .json files
```

### **AGENT 2: Content Planner**

```
INPUT: communication-plan.md + market data
│
PHASE 0: Read & Parse Communication Plan (AUTOMATED)
│
├─ Read: communication-plan.md từ Communication Strategist
├─ Extract:
│  ├─ Message Pillars → Content Pillars
│  ├─ Channel Strategy → Content frequency (FB 3x/week, TikTok 2x/week)
│  ├─ Campaign Themes → Quarterly hooks
│  ├─ Tone & Voice → Writing style guide
│  └─ KPI targets → Benchmarks
│
PHASE 1: Market Intelligence Review (AUTOMATED)
│
├─ Read: gpt-market-synthesis.json
├─ Extract:
│  ├─ Top 3 opportunities
│  ├─ Content adjustments
│  └─ Risk signals
│
PHASE 2: Build Content Calendar (AUTOMATED)
│
├─ /content plan [topic]
│  ├─ Input:
│  │  ├─ communication-plan.md
│  │  ├─ gpt-market-synthesis.json
│  │  └─ Any existing content audit
│  │
│  ├─ Process:
│  │  ├─ Map 12 weeks (3 months)
│  │  ├─ Assign pillars per week
│  │  ├─ Select hero channel per month
│  │  ├─ Set posting frequency (FB 3x, TikTok 2x)
│  │  ├─ Add gpt-market opportunities
│  │  └─ Check KPI benchmarks
│  │
│  └─ Output 3 Excel sheets (⬇️ see below)
│
PHASE 3: Create Excel Templates (AUTOMATED)
│
├─ Sheet 1: Strategic Calendar
│  ├─ Columns: Week | Month | Pillar | Hero Channel | Format | Angle | Persona | CTA | Status
│  ├─ 12 rows (1 per week)
│  └─ Format: .xlsx (dùng để manual update)
│
├─ Sheet 2: KPI Benchmark
│  ├─ Columns: Channel | Reach TB | ER% Target | Bài/Tháng | Format | Notes
│  ├─ 5 rows (1 per channel: FB, TikTok, Instagram, LinkedIn, Email)
│  └─ Format: .xlsx
│
├─ Sheet 3: Production Allocation
│  ├─ Columns: Week | Pillar | Format | Hero? | AI Tool | Time Est. | Owner | Notes
│  ├─ Map từng content piece
│  └─ Format: .xlsx
│
PHASE 4: Notion Sync (AUTOMATED nếu có access)
│
├─ Create Notion database:
│  ├─ Database name: [Brand] Content Calendar Q[X] [YYYY]
│  ├─ Properties:
│  │  ├─ Title (content idea)
│  │  ├─ Week (number 1-12)
│  │  ├─ Pillar (select)
│  │  ├─ Channel (select)
│  │  ├─ Format (select)
│  │  ├─ Status (select: Planned, In Prod, Approved, Published, Measured)
│  │  ├─ Reach (number)
│  │  ├─ Engagement % (number)
│  │  └─ Link to assets (URL)
│  │
│  └─ Auto-populate 36-48 rows
│
└─ 📤 DELIVER to Content Execution
   └─ Files:
      ├─ content-plan.md (summary)
      ├─ strategic-calendar-[brand].xlsx
      ├─ kpi-benchmark-[brand].xlsx
      ├─ production-allocation-[brand].xlsx
      └─ Notion database (if connected)
```

### **AGENT 3: Content Execution**

```
INPUT: content-plan.md + Excel templates
│
WEEKLY WORKFLOW (Thứ 2-7)
│
MON (Thứ 2) — Planning
│
├─ 🤖 /platform algorithm [facebook]
│  └─ Search latest Facebook algorithm updates
│     └─ Output: algorithm-cheat-sheet.md (temp, for reference)
│
├─ 🤖 /platform algorithm [tiktok]
│  └─ Search latest TikTok algorithm
│     └─ Output: algorithm-cheat-sheet.md (temp)
│
├─ Read: strategic calendar for week X
│  ├─ Hero channel: [Facebook / TikTok]
│  ├─ Content pillar: [Pillar name]
│  ├─ Format: [video/carousel/text]
│  └─ Angle: [specific angle]
│
TUE (Thứ 3-4) — Copywriting
│
├─ 🤖 /copywrite [platform] [brief]
│  ├─ Input brief:
│  │  ├─ Platform: facebook (hero channel for month)
│  │  ├─ Pillar: [from calendar]
│  │  ├─ Angle: [from calendar]
│  │  ├─ Target persona: [from communication-plan.md]
│  │  ├─ CTA: [from message pillars]
│  │  └─ Tone: [from tone-voice-guide.md]
│  │
│  ├─ Generate: 3 variations
│  │  ├─ V1: Story-driven angle
│  │  ├─ V2: Data-driven angle
│  │  └─ V3: Community-engagement angle
│  │
│  └─ Output: copywrite-facebook-W[X].md
│     └─ Chứa: [Brief] + [V1] + [V2] + [V3]
│
├─ ⏸️ MANUAL: Review & choose best variation
│     └─ Save chosen copy (V1/V2/V3)
│
WED (Thứ 4) — Visual Creative
│
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
│     └─ Output: visual-brief-W[X].md
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
│  │  └─ Canva brief (no execution yet)
│  │
│  └─ Output: ai-prompts-W[X].md
│     └─ Chứa: [Concept] + [AI Prompt] + [Canva brief]
│
├─ ⏸️ MANUAL: If using Canva
│  ├─ Open Canva
│  ├─ Execute brief manually (or import from AI prompt)
│  ├─ Export: PNG/MP4/PDF
│  └─ Save: assets-W[X]/[format]/[final-asset]
│
THU (Thứ 5) — Approval
│
├─ ⏸️ MANUAL: Final QA before posting
│  ├─ Verify: Copy matches tone-voice-guide?
│  ├─ Verify: Visual matches brief?
│  ├─ Verify: CTA clear + clickable?
│  ├─ Check: Compliance (if needed)?
│  └─ Status: Mark Notion as "Approved"
│
FRI (Thứ 6) — Posting Schedule
│
├─ ⏸️ MANUAL: Set posting date/time
│  ├─ Best time per platform: [from algorithm notes]
│  ├─ Facebook: Morning (7-9 AM) or evening (6-8 PM)
│  ├─ TikTok: Evening (6-10 PM) or early morning (8-10 AM)
│  └─ Schedule tool: Buffer / native platform scheduler / manual post
│     └─ Status: Mark Notion as "Published"
│
SAT-SUN (Thứ 6-7) — Monitoring + Reporting
│
├─ 🤖 Weekly Report (AUTOMATED input required)
│  ├─ User provides:
│  │  ├─ Reach numbers from Buffer/Meta Business Suite
│  │  ├─ Engagement rate per post
│  │  ├─ Comments + shares
│  │  └─ Copy to Excel Execution Log
│  │
│  ├─ /weekly-report [brand] [week]
│  │  ├─ Process:
│  │  │  ├─ Read Excel inputs
│  │  │  ├─ Calculate vs KPI benchmark
│  │  │  ├─ Flag underperformers (Reach < X, ER < Y%)
│  │  │  ├─ Update Notion: Status → "Measured"
│  │  │  └─ Generate weekly-summary-W[X].md
│  │  │
│  │  └─ Output: weekly-summary-W[X].md
│  │     └─ Chứa:
│  │        ├─ Posts published (4-6 per week)
│  │        ├─ Reach totals per channel
│  │        ├─ ER% per post vs KPI
│  │        ├─ Top 3 performing content
│  │        ├─ Underperformers (if any)
│  │        └─ Recommendations for next week
│  │
│  └─ Sync to:
│     ├─ Excel: Execution Log (ongoing tracker)
│     ├─ Notion: Status updates
│     └─ GitHub: weekly-summary-W[X].md (for history)
│
└─ ⏸️ MANUAL: Send report to Content Planner
   └─ If KPI gap > 20% → Planner may adjust strategy
```

---

## 📁 File Format Guide

### **When to Use Each Format:**

```
┌──────────────────────────────────────────────────────────────────────┐
│                        FILE FORMAT DECISION TREE                      │
└──────────────────────────────────────────────────────────────────────┘

1. .md (MARKDOWN) — Primary Format for Strategy & Content
   ─────────────────────────────────────────────────────────────────
   Use when:
   ✅ Human-readable documentation needed
   ✅ Narrative + formatted text (headers, lists, tables)
   ✅ Longer-form strategy, briefs, guidelines
   ✅ Version control + Git history (readable diffs)
   ✅ Can be displayed in GitHub/Notion directly

   Files using .md:
   ├─ communication-plan.md (Communication Strategist)
   ├─ message-house.md (Communication Strategist)
   ├─ tone-voice-guide.md (Communication Strategist)
   ├─ positioning-map.md (Communication Strategist)
   ├─ campaign-themes-[year].md (Communication Strategist)
   ├─ content-plan.md (Content Planner)
   ├─ copywrite-[platform]-W[X].md (Content Execution)
   ├─ visual-brief-W[X].md (Content Execution)
   ├─ ai-prompts-W[X].md (Content Execution)
   ├─ weekly-summary-W[X].md (Content Execution)
   └─ algorithm-cheat-sheet.md (temp reference)

   Example:
   ```markdown
   # Content Plan — Q2 2026

   ## Week 1: Awareness Phase
   | Pillar | Channel | Format | CTA |
   |--------|---------|--------|-----|
   | Education | Facebook | Video | Learn more |
   ```


2. .json (JSON) — Machine-Readable Data
   ─────────────────────────────────────────────────────────────────
   Use when:
   ✅ Structured data that needs parsing (by code/Python)
   ✅ GPT analysis output (standardized format)
   ✅ Multi-language or metadata-heavy content
   ✅ Integration with external tools/APIs
   ✅ Configuration files

   Files using .json:
   ├─ gpt-competitor-analysis.json (from openai-research-helper)
   ├─ gpt-market-synthesis.json (from openai-research-helper)
   ├─ agents-manifest.json (registry)
   └─ config.json (future: brand settings)

   Example:
   ```json
   {
     "hidden_patterns": ["Pattern 1", "Pattern 2"],
     "quick_wins": [
       {
         "action": "Create weekly Q&A series",
         "timeframe": "1-2 weeks",
         "impact": "Engagement +40%"
       }
     ]
   }
   ```


3. .xlsx (EXCEL) — Data Entry + Live Tracking
   ─────────────────────────────────────────────────────────────────
   Use when:
   ✅ Numerical data that changes (KPIs, metrics)
   ✅ Multi-column comparisons (benchmarking)
   ✅ Non-technical users need to edit (Content Planner, stakeholders)
   ✅ Formulas + calculations needed
   ✅ Manual input expected (reach, engagement, dates)
   ✅ Pivot tables, charts for reporting

   Files using .xlsx:
   ├─ strategic-calendar-[brand].xlsx (Content Planner)
   │  └─ Columns: Week | Pillar | Channel | Format | Angle | Status
   │
   ├─ kpi-benchmark-[brand].xlsx (Content Planner)
   │  └─ Columns: Channel | Reach Target | ER% Target | Bài/Tháng | Format
   │
   ├─ production-allocation-[brand].xlsx (Content Planner)
   │  └─ Columns: Week | Pillar | Format | AI Tool | Time | Owner
   │
   └─ execution-log-[brand].xlsx (Content Execution — Weekly updates)
      └─ Columns: Week | Content | Channel | Published Date | Reach | ER% | Status

   Example (Sheet: Strategic Calendar):
   | Week | Month | Pillar | Hero Channel | Format | Status |
   |------|-------|--------|--------------|--------|--------|
   | W1   | May   | Edu    | Facebook     | Video  | Planned |
   | W2   | May   | Promo  | TikTok       | Reel   | In Prod |


4. .py (PYTHON) — Automation Helper Scripts
   ─────────────────────────────────────────────────────────────────
   Use when:
   ✅ Automation logic (API calls, data processing)
   ✅ Code that needs to be reused
   ✅ Integration between tools
   ✅ Custom calculations or transformations

   Files using .py:
   ├─ openai-research-helper.py (OpenAI API wrapper)
   └─ (future) google-sheets-updater.py (Sheets API)
   └─ (future) notion-sync.py (Notion API)

   Usage:
   ```python
   from openai_research_helper import gpt_competitor_deep_analysis
   analysis = gpt_competitor_deep_analysis(audit_data, "Brand")
   ```


5. .txt (TEXT) — Temporary Notes Only
   ─────────────────────────────────────────────────────────────────
   Use when:
   ✅ Rough draft / scratch notes
   ✅ Raw output before formatting
   ✅ Chat history export

   NOT recommended for:
   ❌ Final deliverables
   ❌ Version-controlled documents

   Example:
   └─ chat-history-export-[date].txt


6. Others (Less Common)
   ─────────────────────────────────────────────────────────────────

   .docx (Word):
   ❌ Avoid — Markdown (.md) is better for version control
   
   .pdf:
   ✅ Only for exports (e.g., brand guide distribution)
   
   .csv:
   ✅ Alternative to .xlsx if Excel formulas not needed
   
   .jpg/.png/.mp4:
   ✅ Asset files (design output, video exports)

```

---

## 🔄 Data Flow Between Agents

```
COMMUNICATION STRATEGIST
    ↓ Output: 8 .md files + 2 .json files
    ├─ communication-plan.md
    ├─ message-house.md
    ├─ tone-voice-guide.md
    ├─ positioning-map.md
    ├─ campaign-themes-[year].md
    ├─ gpt-competitor-analysis.json
    └─ gpt-market-synthesis.json
    │
    ↓ [Manual: User reviews]
    │
CONTENT PLANNER
    ↓ Input: communication-plan.md + gpt-market-synthesis.json
    ├─ Parse message pillars → content pillars
    ├─ Parse tone-voice-guide → writing style
    ├─ Parse gpt-market-synthesis → top opportunities
    ↓ Output: 1 .md + 3 .xlsx files + Notion database
    ├─ content-plan.md
    ├─ strategic-calendar-[brand].xlsx
    ├─ kpi-benchmark-[brand].xlsx
    ├─ production-allocation-[brand].xlsx
    └─ Notion: [Brand] Content Calendar
    │
    ↓ [Manual: User reviews]
    │
CONTENT EXECUTION
    ↓ Input: content-plan.md + strategic-calendar.xlsx
    ├─ Read: Week X details (pillar, channel, angle)
    ├─ Read: tone-voice-guide.md (writing rules)
    ├─ Generate: copywrite-[platform]-W[X].md (3 variations)
    │            visual-brief-W[X].md (research + concept)
    │            ai-prompts-W[X].md (AI image prompts)
    │
    ├─ [Manual: Approve copy, create visual]
    │
    ├─ Manual: Set posting date + schedule
    │
    ├─ Manual: Input metrics from Buffer/Meta
    │
    ↓ Output: Weekly
    ├─ weekly-summary-W[X].md (narrative report)
    ├─ execution-log-[brand].xlsx (metrics tracker)
    └─ Notion: Status updates (Measured)
    │
    ↓ [Send to Content Planner for KPI review]
    │
CONTENT PLANNER (Weekly Check-In)
    ├─ Review: KPI actual vs benchmark
    ├─ Flag: Underperformers (Reach < X, ER < Y%)
    ├─ Decide: Continue as-is OR adjust next week
    └─ Optional: Request Communication Strategist adjust if major gap

```

---

## ⏸️ Manual Intervention Points (5 Key Checkpoints)

```
┌──────────────────────────┐
│ 1. AFTER Phase 0 Gather  │ Communication Strategist
│    ⏸️ MANUAL: User review data completeness
│       "Ready to start?"
└──────────────────────────┘
           ↓
┌──────────────────────────┐
│ 2. AFTER Phase 2 Insights│ Communication Strategist
│    ⏸️ MANUAL: User approves 5 insights
│       "Any surprises or clarifications?"
└──────────────────────────┘
           ↓
┌──────────────────────────┐
│ 3. AFTER Content Plan    │ Content Planner
│    ⏸️ MANUAL: User reviews calendar
│       "Correct frequencies? Any changes?"
│       ✓ Confirm → goes to Execution
└──────────────────────────┘
           ↓
┌──────────────────────────┐
│ 4. WEEKLY: Copywriting   │ Content Execution
│    ⏸️ MANUAL: Choose best variation (V1/V2/V3)
│    ⏸️ MANUAL: Research visual inspiration (Behance)
│    ⏸️ MANUAL: Create visual concept brief
│    ⏸️ MANUAL: Approve final assets
│    ⏸️ MANUAL: Schedule posts (set date/time)
└──────────────────────────┘
           ↓
┌──────────────────────────┐
│ 5. WEEKLY: KPI Report    │ Content Planner
│    ⏸️ MANUAL: Input metrics (Reach, ER%)
│    ✓ Review vs KPI benchmark
│    ✓ Decide: Continue OR adjust
└──────────────────────────┘
```

---

## 🤖 Fully Automated Steps (No Manual Input)

```
COMMUNICATION STRATEGIST:
✅ /stakeholder-alignment      [auto check]
✅ /competitor research        [auto WebSearch + GPT]
✅ /market-intelligence       [auto WebSearch + GPT]
✅ /distill-insights          [auto analysis]
✅ /message-house             [auto generation]
✅ /tone-voice                [auto generation]
✅ /competitive-positioning   [auto validation]
✅ /campaign-themes           [auto generation]

CONTENT PLANNER:
✅ Parse communication plan    [auto extract fields]
✅ Build content calendar      [auto assign weeks]
✅ Generate Excel templates    [auto create sheets]
✅ Sync to Notion             [auto upload if API available]

CONTENT EXECUTION:
✅ /platform algorithm        [auto WebSearch]
✅ /copywrite [brief]         [auto generate 3 variations]
✅ /visual creative [brief]   [auto generate concept + prompts]
❌ Final copy approval        [MANUAL]
❌ Visual reference research  [MANUAL]
❌ Post scheduling            [MANUAL]
❌ Metrics input              [MANUAL]
✅ /weekly-report             [auto compile from Excel input]
```

---

## 📊 Recommended Workflow By Week

### **Week 1-2: Strategy Phase (Monthly)**
```
Agent 1: Communication Strategist
   └─ Runs phases 0-6 (parallel research allowed)
   └─ Output: comm-plan.md + supporting docs

User: Review & approve
```

### **Week 3: Planning Phase (Monthly)**
```
Agent 2: Content Planner
   └─ Reads comm-plan.md
   └─ Generates 3-month calendar + Excel templates
   └─ Syncs to Notion

User: Review & approve
```

### **Week 4-15: Execution Phase (Weekly, 12 Weeks)**
```
Agent 3: Content Execution
   Mon:    Platform algorithm check
   Tue-4:  Copywrite (3 variations) → Manual approve
   Thu:    Visual brief + AI prompts
   Fri:    Final approval + schedule posts
   Sat-Sun: Weekly report + metrics input

Weekly: Send report to Planner
Monthly: Planner reviews KPI trend, decides adjustments
Quarterly: Cycle back to Communication Strategist
```

---

## 🎯 Summary: Automation vs Manual

| Phase | Automation | Manual | Tool Used |
|-------|-----------|--------|-----------|
| Strategy | 95% auto | 5% review | Agent 1 |
| Planning | 85% auto | 15% review | Agent 2 |
| Execution | 40% auto | 60% manual | Agent 3 |
| Reporting | 70% auto | 30% input | Agent 3 |

**Key Insight:** The higher you go in the funnel (Strategy), the more automated. The lower (Execution), the more creative human input needed.
