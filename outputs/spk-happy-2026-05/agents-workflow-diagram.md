# 2-Agent Workflow — SPK HAPPY Content Workspace
**Architecture:** Content Planner (CMO) + Content Execution (Operator)  
**Version:** 2.0 — Fully Integrated  
**Last updated:** 2026-05-12

---

## 🎯 High-Level Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  QUARTERLY CYCLE (Q2 = May 12 - July 31)                                   │
│                                                                             │
│  [Content Planner]                  [Content Execution]                     │
│  1. Situation analysis              5. Copywrite heroes                     │
│  2. Strategy foundation             6. Design + visual creative             │
│  3. Messaging architecture          7. Produce 56 pieces                    │
│  4. Content calendar (56 pieces)    8. Schedule + post                      │
│                                      9. Track metrics (weekly)              │
│                          ↓                                                  │
│                     Handoff Brief (9 sections)                              │
│                          ↓                                                  │
│  QA GATES + WEEKLY REVIEWS          MEASUREMENT → FEEDBACK LOOP             │
│  • Think-Coach (validation)         • Hypothesis H1-H3 testing              │
│  • Sume-Kit (synthesis)             • Notion database updates               │
│  • Pivot decisions (26/5, 31/5)     • Weekly synthesis reports              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Agent 1: Content Planner (CMO Role)

### Workflow — Month-by-Month

```
┌─── MAY (W20-W22) ────────────────────────────────────────────────────────┐
│                                                                           │
│  [12-16/5 — PHASE 1-4 RESEARCH & PLANNING]                               │
│  ├─ Input: Brand brief + competitor audit + market intel + PPTX          │
│  ├─ Process:                                                             │
│  │  ├─ Situation analysis (market + algorithm + compliance)              │
│  │  ├─ 2 personas (Thủy vs Hương) + SMART objectives                    │
│  │  ├─ 5 pillars + OPE channel matrix                                    │
│  │  ├─ 56 content pieces (3 tháng, 11 weeks)                             │
│  │  └─ 6 hypotheses (H1-H3 immediate, H4-H6 planned)                     │
│  ├─ Output: content-plan.md + hypothesis-log.md                          │
│  ├─ QA: /think-coach "Pillar có overlap không?" → validate              │
│  └─ Sign-off: ✅ APPROVED (16/5)                                          │
│                                                                           │
│  [16/5 — HANDOFF TO EXECUTION]                                           │
│  ├─ Document: handoff-brief-happy.md (9 sections)                        │
│  ├─ Brief includes: Brand + objectives + resources + KPIs                │
│  ├─ Self-check gate: 5 YES/NO questions before publish                   │
│  └─ Handoff: ✅ COMPLETE (16/5)                                           │
│                                                                           │
│  [17-22/5 — WEEK 1 LAUNCH + MONITORING]                                  │
│  ├─ Monitor: Execution starts W20 production                             │
│  ├─ H1 data collection: Reels vs static reach (post 13/5)               │
│  ├─ H2 data collection: Luật Dân số shares (post 13/5)                  │
│  ├─ Friday (21/5): /sume-kit W20 data → synthesis report               │
│  └─ Findings: Early signal on Reels performance (H1)                    │
│                                                                           │
│  [23-26/5 — H1 DECISION POINT]                                          │
│  ├─ Measurement deadline: 26/5 (2 weeks data)                            │
│  ├─ H1 Confirmed (Reels 2x+)?: → PIVOT visual strategy M2              │
│  │  └─ If YES: Request /think-coach "Video-first production system?"   │
│  │  └─ If NO: Investigate content quality issue                         │
│  └─ Action: M2 direction update (30/5)                                  │
│                                                                           │
│  [27-31/5 — H2 DECISION + M2 PLANNING]                                  │
│  ├─ Measurement deadline: 31/5 (3 weeks data)                            │
│  ├─ H2 Confirmed (Luật 3x shares)?: → Scale policy education angle     │
│  │  └─ If YES: Queue 2-3 follow-up policy content (W22-24)             │
│  │  └─ If NO: Review copy tone/audience fit                             │
│  ├─ H3 prep: Baseline TikTok vs Facebook audience difference           │
│  └─ Output: M2 content direction (updated calendar W23-W30)            │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Core Responsibilities

| Responsibility | Cadence | Input | Output | Gating |
|---|---|---|---|---|
| **Research & Strategy** | Quarterly | Brand + market data | Content plan (56 pieces) | /think-coach validation |
| **Hypothesis Design** | Per campaign | Market signal + data gap | H1-H6 tracking (deadlines) | H status updates |
| **Weekly QA Review** | Every Friday | Execution metrics + Notion | Synthesis report | /sume-kit synthesis |
| **Decision Gating** | Per milestone | H1-H3 data (26/5, 31/5) | M2 direction pivot | Go/no-go analysis |
| **Escalation** | As-needed | Execution blockers | Resolution path | Planner decision |

### Tools & Skills Used

| Tool | Skill | Purpose |
|---|---|---|
| Notion | Fetch + Create/Update | Read KPI targets, update hypothesis status |
| GitHub | Bash git commands | Version control for planning docs |
| Claude (AI) | /think-coach | QA validation before handoff |
| Claude (AI) | /sume-kit | Weekly synthesis → pattern extraction |
| Google Drive | Upload | Archive finalized plans |
| Spreadsheet (future) | Google Sheets MCP | KPI dashboard (read-only for team) |

### Escalation Rules (Stop-Go Gates)

**🟢 Continue Execution:**
- ✅ Hypothesis H1-H2 on track (data within range)
- ✅ Compliance check: 0 violations
- ✅ Notion database updated (>80% current)
- ✅ BS Thư engagement stable

**🟡 Flag for Review (Execution slows, don't stop):**
- ⚠️ Hypothesis H1/H2 trending opposite (e.g., static ER% > Reels)
- ⚠️ One piece violates compliance → quarantine, fix, republish
- ⚠️ Notion updates >3 days late (measurement breaks)
- ⚠️ BS Thư scheduling unstable (need contingency)

**🔴 STOP Execution:**
- ❌ Hypothesis H1/H2 rejected (confidence interval, not just minor variance)
- ❌ Multiple compliance violations (systemic issue, not typo)
- ❌ Patient data/image posted without consent (legal risk)
- ❌ BS Thư unavailable (cannot maintain 2 shoots/week baseline)

---

## 🎬 Agent 2: Content Execution (Operator Role)

### Workflow — Week-by-Week

```
┌─── WEEK 20 (May 12-18) ─────────────────────────────────────────────────┐
│                                                                           │
│  [MONDAY 12/5 — Receive Handoff]                                         │
│  ├─ File: handoff-brief-happy.md                                         │
│  ├─ Checklist: 9 sections complete? 5 self-check gates pass?            │
│  └─ Go/No-Go: YES → proceed; NO → ask Planner for clarity              │
│                                                                           │
│  [TUESDAY 13/5 — PRODUCTION DAY 1: Copywrite + Shooting]                │
│  ├─ Copywrite:                                                           │
│  │  ├─ /copywrite tiktok "Luật Dân số 7 tháng — who gets it"           │
│  │  ├─ /copywrite tiktok "Thai tuần 8 — sizes & timeline"              │
│  │  └─ Output: 3 script variations each + captions                      │
│  ├─ Compliance check: Each script against 5-item checklist              │
│  │  └─ Gate: YES all pass → approve to BS Thư                          │
│  │  └─ Gate: NO violation → revise script                              │
│  ├─ BS Thư filming: 2 videos (60-90s, 2+ takes each)                    │
│  ├─ CapCut rough edit: Watermark removal + export .mp4                 │
│  └─ Upload to folder: `outputs/W20/videos-raw/`                        │
│                                                                           │
│  [WEDNESDAY 14/5 — Design + Social Graphic]                             │
│  ├─ /visual creative "Infographic 9 mốc khám thai"                     │
│  │  ├─ Brief: 1080x1350, colors #FFF8F5 + #E8A598, vertical timeline   │
│  │  └─ Output: Canva design link                                        │
│  ├─ Export PNG: 1080x1350px, >150dpi, check mobile readability         │
│  └─ Upload: Google Drive → copy link → Notion update                   │
│                                                                           │
│  [WEDNESDAY 14/5 19:00 — PUBLISH Bài #1 (TikTok)]                      │
│  ├─ Video: Luật Dân số (Variation V1 approved)                          │
│  ├─ Caption: "Nghỉ thai sản 7 tháng từ 1/7/2026..."                     │
│  ├─ CTA: "Comment your questions below"                                 │
│  ├─ Notion update: Status → "In-progress", Posted Date → 13/5          │
│  └─ Buffer: Schedule 30s before manual post (freshness signal)         │
│                                                                           │
│  [WEDNESDAY 14/5 19:30 — PUBLISH Bài #1 Repost (FB Reels)]             │
│  ├─ Video: Same TikTok (watermark removed, CapCut export)              │
│  ├─ Caption: "Từ 1/7/2026: Nghỉ thai sản con thứ 2 lên 7 tháng"        │
│  ├─ Tone: Warmer (private sharing CTA, family-focused)                  │
│  └─ Notion update: Status → "In-progress", Posted Date → 13/5          │
│                                                                           │
│  [THURSDAY 14/5 08:00 — PUBLISH Bài #2 (FB Post, Infographic)]         │
│  ├─ Image: 9 mốc khám thai infographic                                  │
│  ├─ Caption: "Lịch khám thai chuẩn..."                                  │
│  ├─ CTA: "Save + tag bạn bầu"                                           │
│  └─ Notion update: Status → "In-progress", Posted Date → 14/5          │
│                                                                           │
│  [THURSDAY 15/5 12:00 — PUBLISH Bài #3 (TikTok Q&A)]                    │
│  ├─ Video: Thai tuần 8 (Variation VA approved)                          │
│  ├─ Caption: "Thai tuần 8 bé nặng bao nhiêu?..."                        │
│  ├─ CTA: "Comment your concerns"                                        │
│  └─ Notion update: Status → "In-progress", Posted Date → 15/5          │
│                                                                           │
│  [THURSDAY 15/5 12:30 — PUBLISH Bài #4 (FB Reels Repost)]              │
│  ├─ Video: Repost bài #3 (watermark removed)                            │
│  ├─ Caption: Shorter than TikTok (FB audience, different tone)          │
│  └─ Notion update: Status → "In-progress", Posted Date → 15/5          │
│                                                                           │
│  [FRIDAY-SUNDAY 17-18/5 — MEASUREMENT SETUP]                            │
│  ├─ Meta Business Suite: Verify Reach/ER% access for all 4 posts       │
│  ├─ Buffer Analytics: Export W20 performance baseline                    │
│  ├─ Comments monitoring: TikTok + FB top 10 comments screenshot         │
│  └─ Notion snapshot: Take Friday 21/5 status (data for Sume-Kit)       │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘

┌─── WEEK 21+ (May 19-31) ──────────────────────────────────────────────┐
│                                                                         │
│  [DAILY — PRODUCTION RHYTHM ESTABLISHED]                               │
│  ├─ Monday: Receive Planner's W[n] direction brief                    │
│  ├─ Mon-Wed: Copywrite (3 pieces) + Design (1-2 pieces) + Shooting   │
│  ├─ Wed-Fri: Publish 3-4 pieces across channels                       │
│  ├─ Friday: Measurement snapshot → fill Notion actual results        │
│  └─ Friday EOD: Forward metrics to Planner for Sume-Kit synthesis    │
│                                                                         │
│  [WEEKLY CADENCE]                                                      │
│  ├─ Monday 09:00: Get weekly direction from Planner                   │
│  ├─ Mon 10:00: Brief BS Thư on scripts (send 24h before shooting)    │
│  ├─ Tue-Wed: Shoot + edit                                             │
│  ├─ Wed-Fri: Publish (timing staggered per channel/audience)          │
│  ├─ Friday 16:00: Measurement collection (buffer export)             │
│  ├─ Friday 17:00: Notion update (reach, ER%, status)                │
│  └─ Friday 18:00: Send data snapshot to Planner                      │
│                                                                         │
│  [HYPOTHESIS TRACKING — Weekly Updates]                              │
│  ├─ H1: Monday morning → check 7-day reach (Reels vs static)        │
│  ├─ H2: Thursday morning → check shares (Luật vs baseline)          │
│  ├─ H3: Friday end-of-day → new followers count (TikTok only)       │
│  └─ Action: Flag anomalies to Planner immediately (don't wait)       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Core Responsibilities

| Responsibility | Cadence | Input | Output | Gating |
|---|---|---|---|---|
| **Copywrite Heroes** | 2-3/week | Script brief | 3 variations per piece | Compliance checklist |
| **Visual Creative** | 1-2/week | Design brief | Canva link + PNG export | Mobile readability test |
| **Production (Shoot/Edit)** | 2x/week | Script approved + BS Thư | Processed videos ready | Audio/video quality check |
| **Publishing** | 3-4/week | Assets ready | Live post (Notion updated) | CTA + caption accuracy |
| **Measurement** | Weekly | Buffer + Meta | Reach/ER%/Shares filled | Friday snapshot |
| **Hypothesis Tracking** | 3x/week | Daily post data | H1-H3 metrics logged | Anomaly flag to Planner |

### Tools & Skills Used

| Tool | Skill | Purpose |
|---|---|---|
| Claude (AI) | /copywrite | Generate 3 script variations |
| Canva (AI) | /visual creative | Design infographics + social graphics |
| CapCut | Manual | Remove watermarks, batch edit videos |
| Buffer | Manual | Schedule posts, verify timing |
| Meta Business Suite | Manual | Collect Reach/ER% data daily |
| Notion | Update pages | Post status, actual results |
| GitHub | Bash | Commit weekly snapshots |

### Quality Gates Before Publishing

**Compliance Checklist (5 items):**
- [ ] No claims of "cure" / "100% safe" / "guaranteed"
- [ ] No patient images/faces (unless written consent noted)
- [ ] No livestream exams or medical procedure videos
- [ ] Language uses "monitor / support / accompany" (not "treat / fix")
- [ ] Source cited if any external medical claim made

**Production Checklist (5 items):**
- [ ] Audio: Clear, no background noise, BS Thư intelligible
- [ ] Video: Watermark removed (if TikTok repost), exposure correct, focus sharp
- [ ] Caption: Spelling/grammar checked, CTA present, hashtags relevant
- [ ] Timing: Scheduled within ±5 min of planned time (freshness signal)
- [ ] Notion: Status + Posted Date filled immediately after going live

---

## 🔄 Handoff & Feedback Loop

### Handoff Format (Mondays 09:00)

**From Content Planner → Content Execution:**

```markdown
# Weekly Direction — SPK HAPPY — W[n]

**Date:** 2026-05-[nn]
**From:** Content Planner
**To:** Content Execution
**Deadline Production:** Friday 15:00

---

## This Week's Focus
- [Pillar emphasis]
- [Hypothesis to measure]
- [Special alerts/flags]

---

## Content Pieces (3-4 bài)
1. Bài [#]: [Title] | Channel: [TikTok/FB] | Format: [Video/Infographic]
   - Script brief: [Angle + hook + message + CTA]
   - Persona: [Thủy/Hương/Both]
   - KPI target: [Reach/Shares/Comments]

2. Bài [#]: ...

---

## Special Notes
- [Compliance flag if any]
- [Resource constraint]
- [Audience event/trend to leverage]

---

## Scripts Deadline
- Copywriter deliver: Wednesday 10:00
- BS Thư review: Wednesday 11:00
- Final approval: Wednesday 12:00 (lock for shoots)

---

## Measurement This Week
- H1 status: [7-day Reels vs static]
- H2 status: [3-week Luật shares]
- New metrics: [If applicable]
```

### Feedback Loop (Fridays 18:00)

**From Content Execution → Content Planner:**

```markdown
# Weekly Snapshot — W[n] — Metrics + Learnings

**Week:** W20 (May 12-18)
**Reported by:** Content Execution
**Data window:** 13/5 - 20/5 (7 days post-launch)

---

## Execution Status
- [ ] 4/4 bài published on schedule
- [ ] 0/4 compliance issues
- [ ] 4/4 Notion entries complete

---

## Metrics (7-Day Snapshot)

| Bài | Channel | Posted | Reach | ER% | Shares | Comments |
|---|---|---|---|---|---|---|
| #1 Luật | TikTok | 13/5 | [xxx] | [x%] | [xx] | [xxx] |
| #1 Luật | FB Reels | 13/5 | [xxx] | [x%] | [xx] | [xxx] |
| #2 Infographic | FB Post | 14/5 | [xxx] | [x%] | [xx] | [xxx] |
| #3 Thai W8 | TikTok | 15/5 | [xxx] | [x%] | [xx] | [xxx] |

---

## H1-H3 Status
- **H1 (Reels vs Static):** Reels reach = [xxx], Static = [xxx]. Ratio = [x.xx]x
- **H2 (Luật Dân Số):** Luật shares = [xxx], baseline shares = [xxx]. Ratio = [x.xx]x
- **H3 (Reply video prep):** TikTok new followers W20 = [xxx]. Baseline = [xxx].

---

## Production Learnings
- **Good:** [What worked — script tone / visual / timing]
- **Improve:** [What to adjust — BS Thư feedback / audience response]
- **Blocker:** [What blocked speed / quality]

---

## Next Week Request
- [Any resource / timeline adjustments needed]
```

---

## 🎯 Integration Points (Where Agents Overlap)

### 1. Weekly Direction (Monday Handoff)
- **Initiated by:** Content Planner
- **Received by:** Content Execution
- **Trigger:** Planner finishes Friday synthesis
- **Deadline:** Monday 09:00 (execution has 1 week to produce)

### 2. Hypothesis Measurement (Fri 18:00 Snapshot)
- **Initiated by:** Content Execution (collects data)
- **Received by:** Content Planner (runs Sume-Kit)
- **Trigger:** Friday EOD (7-day post-window for W20)
- **Deadline:** Snapshot sent to Planner by Friday 18:00

### 3. Pivot Decisions (26/5, 31/5)
- **Owned by:** Content Planner
- **Communicated to:** Content Execution
- **Trigger:** H1 or H2 confirms/rejects
- **Action:** M2 direction brief updated (if change needed)

### 4. Escalation (As-Needed)
- **Initiated by:** Either agent (blocker / data anomaly / compliance)
- **Resolved by:** Planner (final authority on strategy + rules)
- **Escalation examples:**
  - Execution: "BS Thư unavailable Thursday — need to reschedule shoots?"
  - Execution: "Comments on bài #1 suggest audience misunderstood message — revise W21?"
  - Planner: "H1 data showing static > Reels — investigate copy quality vs format issue?"

---

## 📈 Success Metrics — Agent Performance

### Content Planner KPIs

| Metric | Target | Deadline |
|---|---|---|
| Content plan completeness | 56 pieces mapped + KPI set | 16/5 ✅ |
| Hypothesis clarity | 6 hypotheses with measurement method | 16/5 ✅ |
| Weekly synthesis turnaround | 18-24h after Friday data | Every Friday |
| Decision velocity | Pivot decision <48h after H1-H3 deadline | 26/5, 31/5 |
| Escalation resolution time | Response <24h to Execution blockers | Ongoing |

### Content Execution KPIs

| Metric | Target | Deadline |
|---|---|---|
| Publishing on-time rate | >95% of posts within ±5 min planned | Weekly |
| Compliance violation rate | 0 posts published with violations | Ongoing |
| Notion update timeliness | Status filled within 24h of posting | Weekly |
| Production velocity | 5-6 pieces/week sustained from W21+ | W21 onward |
| Measurement data completeness | 100% of posts have Reach/ER% by Friday | Every Friday |

---

## 🔗 Workflow Integration Checklist

- [ ] **Notion database:** Shared access (Planner read, Execution write)
- [ ] **GitHub:** Both agents push to `content-workspace` (commits + outputs)
- [ ] **Google Drive:** Shared folder for scripts + assets (versioning)
- [ ] **Slack/Email:** Weekly handoff + snapshot notification (async)
- [ ] **Compliance checklist:** Documented + embedded in copywrite prompts
- [ ] **Hypothesis log:** Single source of truth (updated Fri EOD)
- [ ] **Buffer/Meta access:** Execution agent has read access (measurement)
- [ ] **Canva brand kit:** Shared between design + Planner

**Status:** ✅ All systems configured for W20 launch

---

**Workflow diagram finalized:** 2026-05-12  
**Ready for:** W20 execution starting 13/5/2026
