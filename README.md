# Marketing Content Workspace v2 — 3 Agents + 10 Skills + OpenAI

**Phiên bản:** 2.0.0  
**Ngày tạo:** 2026-05-10  
**Cập nhật:** 2026-05-14  
**Repository:** https://github.com/hangphuong-91/content-workspace

Workspace Claude Code hoàn chỉnh cho marketer một người hoặc nhóm nhỏ. **3 agents chuyên biệt** + 10 skills + OpenAI deep research = máy tạo & quản lý nội dung tự động từ chiến lược đến công bố.

---

## 🎯 Workspace Này Làm Gì?

Biến một brief nội dung thành **chiến lược nội dung thực thi 3 tháng + quy trình sản xuất**:

```
Nghiên cứu thị trường (GPT) → Định vị & thông điệp → Kế hoạch nội dung 3 tháng
→ Quy trình sản xuất → Viết bài hàng tuần → Thiết kế hình ảnh → Đo lường & điều chỉnh
```

Phù hợp cho:
- Marketer một người / solopreneur
- Nhóm marketing nhỏ cần tự động hóa
- Agency muốn quy trình có thể lặp lại
- Bàn giao kiến thức cho team khác

---

## 🤖 3 Agents Chuyên Biệt

### **Agent 1: Communication Strategist**
**Role:** CMO — Nghiên cứu, định vị, đúc kết insights  
**Cadence:** Hàng quý (3 tháng)  
**Automation:** 95% tự động  
**Output:** 8 .md files + 2 .json files (strategy, positioning, tone & voice guide)

```
Quy trình: Phases 0→6
├─ Phase 0: Thu thập input (brand, audience, product)
├─ Phase 0.5: Kiểm tra stakeholder & compliance risk
├─ Phase 1: Nghiên cứu (competitor research + market intelligence + GPT analysis)
├─ Phase 2: Distill insights (5 insights + 1 meta-pattern)
├─ Phase 3: Message house (Brand Promise + 3-5 pillars)
├─ Phase 3.5: Tone & Voice guide
├─ Phase 3.7: Competitive positioning validation
├─ Phase 4: Channel strategy (OPE matrix)
├─ Phase 4.5: Campaign themes (quarterly hooks)
├─ Phase 5: High-level calendar
└─ Phase 6: Handoff brief to Content Planner
```

**Skills:** `/stakeholder-alignment`, `/competitor-research`, `/market-intelligence`, `/distill-insights`, `/message-house`, `/tone-voice`, `/competitive-positioning`, `/campaign-themes` + GPT o1

---

### **Agent 2: Content Planner**
**Role:** Strategy execution orchestrator — Lên kế hoạch 3 tháng, giám sát chất lượng  
**Cadence:** Đầu mỗi quý + hàng tuần (quick check KPI)  
**Automation:** 85% tự động  
**Output:** 1 .md file + 3 .xlsx files + Notion database

```
Quy trình:
├─ Phase 1: Parse communication-plan.md
├─ Phase 2: Extract opportunities từ gpt-market-synthesis.json
├─ Phase 3: Build 12-week content calendar
│  ├─ Strategic Calendar (Excel): Week | Pillar | Channel | Format | Angle | Status
│  ├─ KPI Benchmark (Excel): Channel | Reach Target | ER% Target | Frequency
│  └─ Production Allocation (Excel): Week | Content | Tool | Time | Owner
├─ Phase 4: Sync to Notion database (if available)
└─ Weekly: Monitor KPI vs benchmark, flag underperformers
```

**Skills:** `/content plan` (reads communication data) + manual orchestration

---

### **Agent 3: Content Execution**
**Role:** Operator — Sản xuất nội dung, thiết kế, đăng bài, báo cáo  
**Cadence:** Hàng tuần (Thứ 2-7)  
**Automation:** 40% tự động, 60% cần hướng dẫn & phê duyệt  
**Output:** Copywriting + visuals + weekly report + metrics tracking

```
Quy trình hàng tuần:
├─ MON (Thứ 2): /platform algorithm [facebook] + /platform algorithm [tiktok]
├─ TUE-4 (Thứ 3-4): /copywrite [platform] [brief] → 3 variations → Manual approve
├─ WED (Thứ 4): Research Behance/Pinterest → Create visual brief → /visual creative [brief]
├─ THU (Thứ 5): Final QA (copy + visual approved)
├─ FRI (Thứ 6): Manual schedule posts
└─ SAT-7 (Thứ 6-7): /weekly-report [brand] [week] → Update metrics
```

**Skills:** `/platform algorithm`, `/copywrite`, `/visual creative`, `/weekly-report` + manual approvals

---

## 📊 10 Skills (3 mới + 7 legacy)

### **New Skills (v2.0)**

| Skill | Command | Chức năng | Tích hợp |
|-------|---------|----------|---------|
| **Market Intelligence** | `/market-intelligence [brand] [month]` | SEO keywords + algorithm updates + competitor pulse (monthly pulse check) | WebSearch + GPT o1 synthesis |
| **Performance Tracking** | `/performance-tracking [brand] [period]` | Compare actual KPI vs planned, identify gaps, recommendations | Notion + Google Sheets |
| **Weekly Report** | `/weekly-report [brand] [week]` | Compile weekly metrics, update Notion, generate summary | Notion + Excel |

### **Legacy Skills (v1.0) — Still Used**

| Skill | Command | Chức năng | Cadence |
|-------|---------|----------|---------|
| **Competitor Research** | `/competitor research [brand]` | Phân tích đối thủ, gap analysis, SWOT + GPT deep analysis | Hàng quý (hoặc khi cần) |
| **Platform Algorithm** | `/platform algorithm [platform]` | Thuật toán mới nhất (Facebook, TikTok, Instagram, LinkedIn, YouTube, X) | Trước khi viết bài |
| **Content Plan** | `/content plan [topic]` | 5-giai đoạn chiến lược, lịch 3 tháng, theo dõi | Hàng quý |
| **Copywrite** | `/copywrite [platform] [brief]` | Viết bài × 3 biến thể, ánh xạ thiên kiến nhận thức | Hàng tuần |
| **Visual Creative** | `/visual creative [brief]` | Brief + AI prompts + Canva brief (no auto-execution) | Hàng tuần |
| **AI Execution** | `/ai execution [plan-file]` | Quy trình sản xuất + lịch hàng tuần + sơ đồ tái sử dụng | Đầu quý, bàn giao |
| **Schedule Posting** | `/schedule posting [brand]` | Manual + Buffer scheduling (no Zapier auto) | Sau khi approve |

---

## 🚀 Quick Start (10 phút)

### **Bước 1: Clone & Setup**
```bash
git clone https://github.com/hangphuong-91/content-workspace
cd content-workspace
cat .claude/AGENTS-SETUP.md
```

### **Bước 2: Xác nhận MCPs Được Kết Nối**
```
✅ Notion (Notion database tracking)
✅ Google Drive (File storage)
✅ Canva (Visual design reference)
✅ GitHub CLI (Version control)
```

### **Bước 3: Set OpenAI API Key** (Optional but recommended)
```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-proj-[YOUR-KEY]", "User")
```

### **Bước 4: Chạy Workflow Đầu Tiên**
```bash
# Quý 1: Communication Strategist (ngày 1)
/stakeholder-alignment "brand của bạn"
/competitor research "brand của bạn"
/market-intelligence "brand của bạn" "tháng 5"
/content plan "chủ đề của bạn"

# Cùng ngày: Content Planner (ngay sau khi comm plan xong)
/content plan "chủ đề của bạn"  # Đọc communication-plan.md

# Hàng tuần: Content Execution
/copywrite facebook "brief của bạn"
/visual creative "brief hình ảnh"
/weekly-report "brand" "tuần-1"
```

---

## 📁 Cấu Trúc Folder

```
content-workspace/
├── README.md                          ← Bạn đang ở đây
├── CLAUDE.md                          ← Quy tắc dự án, ngôn ngữ
├── AGENTS-README.md                   ← Chi tiết 3 agents
├── 3-AGENTS-WORKFLOW-DIAGRAM.md       ← Workflow + automation points + file formats
├── plan.md                            ← Kế hoạch chi tiết
│
├── .claude/
│   ├── agents/
│   │   ├── communication-strategist.md   ← Agent 1
│   │   ├── content-planner.md            ← Agent 2
│   │   ├── content-execution.md          ← Agent 3
│   │   └── agents-manifest.json
│   │
│   └── skills/
│       ├── market-intelligence.md        ← NEW (v2.0)
│       ├── performance-tracking.md       ← NEW (v2.0)
│       ├── weekly-report.md              ← NEW (v2.0)
│       ├── competitor-research.md        (with GPT integration)
│       ├── copywrite.md
│       ├── visual-creative.md
│       ├── platform-algorithm.md
│       ├── ai-execution.md
│       ├── schedule-posting.md
│       ├── openai-research-helper.py     ← Helper module
│       ├── OPENAI-INTEGRATION-GUIDE.md
│       │
│       └── [supporting templates & frameworks]
│
├── outputs/
│   └── [brand]-[YYYY-MM]/
│       ├── communication-plan.md
│       ├── message-house.md
│       ├── tone-voice-guide.md
│       ├── positioning-map.md
│       ├── campaign-themes.md
│       ├── gpt-competitor-analysis.json
│       ├── gpt-market-synthesis.json
│       ├── content-plan.md
│       ├── strategic-calendar.xlsx
│       ├── kpi-benchmark.xlsx
│       ├── production-allocation.xlsx
│       ├── copywrite-[platform]-W[X].md
│       ├── visual-brief-W[X].md
│       ├── ai-prompts-W[X].md
│       ├── weekly-summary-W[X].md
│       └── execution-log.xlsx
│
└── exports/
    └── chat-history.txt
```

---

## 🔄 Workflow by Role

### **Cho Marketer Một Người**
```
Tháng 1:
  ├─ Day 1-2: Communication Strategist chạy phases 0→6 (2-3 giờ)
  │  └─ Output: communication-plan.md
  ├─ Day 3: Content Planner chạy /content plan (1 giờ)
  │  └─ Output: 3-month calendar + Excel templates
  └─ Approval: 30 min review + adjust

Tháng 2-4 (Hàng tuần):
  ├─ Thứ 2: /platform algorithm (15 min)
  ├─ Thứ 3-4: /copywrite (30 min) → approve (15 min)
  ├─ Thứ 4: Research visual + /visual creative (45 min) → approve (15 min)
  ├─ Thứ 5-6: Manual schedule posts (30 min)
  └─ Thứ 6-7: Input metrics + /weekly-report (30 min)
  
  **Total per week:** ~4 hours

Tháng 4 cuối:
  ├─ Communication Strategist: điều chỉnh positioning (nếu cần)
  └─ Content Planner: review Q2 data, adjust Q3 strategy
```

### **Cho Nhóm Nhỏ (3 người)**
```
Role 1 — Strategic Lead (30% time):
  ├─ Monthly: /market-intelligence (1 hour)
  ├─ Quarterly: Communication Strategist workflow (8 hours)
  └─ Weekly: Review KPI report + decide adjustments (30 min)

Role 2 — Content Writer (80% time):
  ├─ Hàng tuần: /copywrite (4 × 30 min = 2 hours)
  ├─ Hàng tuần: Approve & adjust copy (1 hour)
  └─ Hàng tuần: Research angle + brief ideas (2 hours)

Role 3 — Designer (80% time):
  ├─ Hàng tuần: Research visual inspiration (1.5 hours)
  ├─ Hàng tuần: /visual creative (2 hours)
  ├─ Hàng tuần: Create assets in Canva (3 hours)
  └─ Hàng tuần: Approve + export (30 min)

Weekly Sync:
  ├─ Monday: Planner shares weekly direction
  ├─ Wednesday: Writer + Designer sync on approvals
  └─ Friday: All review weekly metrics report
```

---

## 📚 Key Documents

| Document | Purpose | For Whom |
|----------|---------|----------|
| **[README.md](./README.md)** | Workspace overview (you are here) | Everyone |
| **[CLAUDE.md](./CLAUDE.md)** | Project rules, language, context | Claude (AI) |
| **[AGENTS-README.md](./AGENTS-README.md)** | Detailed agent definitions & workflows | All users |
| **[3-AGENTS-WORKFLOW-DIAGRAM.md](./3-AGENTS-WORKFLOW-DIAGRAM.md)** | Diagrams, automation points, file formats | Architects, technical leads |
| **[plan.md](./plan.md)** | Full implementation roadmap | Project managers, developers |
| **[.claude/AGENTS-SETUP.md](./.claude/AGENTS-SETUP.md)** | How to register agents in Claude Code | Technical setup |
| **[OPENAI-INTEGRATION-GUIDE.md](./.claude/skills/OPENAI-INTEGRATION-GUIDE.md)** | OpenAI API setup & integration | Advanced users |

---

## 🔌 Integration Points

| Tool | Used By | For What |
|------|---------|----------|
| **Notion** | All agents | Content tracking database, brand guide repository |
| **Google Drive** | Planner + Execution | File storage, Excel templates, shared documents |
| **Canva** | Visual Creative | Design reference briefs (no auto-execution) |
| **GitHub** | All | Version control, workflow history, team knowledge base |
| **Buffer** | Content Execution | Manual post scheduling |
| **OpenAI API** | Communication Strategist | GPT o1 deep analysis (competitor + market data) |
| **Google Sheets** | Content Planner | KPI tracking, performance reporting (manual input) |

---

## ✅ Checklist Bắt Đầu

- [ ] Clone repo
- [ ] Read [AGENTS-README.md](./AGENTS-README.md)
- [ ] Read [CLAUDE.md](./CLAUDE.md)
- [ ] Verify MCPs: Notion, Google Drive, Canva, GitHub
- [ ] Set OPENAI_API_KEY (optional but recommended)
- [ ] Run test workflow with demo brand
- [ ] Share outputs folder with team (if group)
- [ ] Create Notion database for content tracking
- [ ] Schedule Communication Strategist briefing (Q1 kickoff)

---

## 🤝 Collaboration & Handoff

**Cho bàn giao team:** Tất cả file .md + Excel templates đủ rõ để người không biết Claude Code follow được.

**Cho agency:** Thư mục `outputs/[brand]-[YYYY-MM]/` = deliverable hoàn chỉnh (strategy + calendar + SOP).

**Cho tiếp tục kỳ sau:** GitHub history + Notion database = đầy đủ context.

---

## 📝 License

Workspace này được tạo để học tập & sử dụng nội bộ.

---

**Build with:** Claude Code × Think-Kit + SUME Methods × OpenAI API  
**v2.0.0 | 2026-05-14**  
**GitHub:** https://github.com/hangphuong-91/content-workspace
