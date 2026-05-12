# Skill: Sume-Kit — Data Synthesis & Insight Extraction

**Trigger:** `/sume-kit [source files or data chunks]`

**Thời gian:** 10–20 phút per session (tùy volume source)

**Dùng khi nào:** Bạn có 3+ data sources (reports, metrics, competitor posts, user feedback) cần rút ra consolidated insights + action items. Không phải summary (tóm tắt), mà synthesis (liên kết patterns + rút ra implications).

---

## Quy Trình — 4 Bước Synthesis

### 1. **Ingest — Đọc & Normalize Tất Cả Sources**

Skill sẽ:
- Đọc files cung cấp (PDF reports, markdown, Google Sheets export, JSON)
- Normalize dữ liệu vào 3 categories:
  - **Quantitative:** metrics, numbers, trends (reach, ER%, conversion rate)
  - **Qualitative:** comments, sentiment, themes (user feedback, competitor angles)
  - **Contextual:** dates, attributions, sources (who said what when)

**Output:** Unified data map (không là summary, là connection graph)

### 2. **Identify Patterns — Tìm Liên Kết Cross-Source**

Từ sources khác nhau, tìm:
- **Agreement:** "3/5 sources cảnh báo về X" → tín hiệu mạnh
- **Contradiction:** "A nói X tăng, B nói X giảm" → cần dig deeper
- **Emergence:** Pattern không rõ ở 1 source nhưng manifest ở combination
- **Absence:** "Tất cả sources skip topic Y" → có implication hay chỉ oversight?

**Output:** Pattern matrix (source 1 ∩ source 2 ∩ source 3 = pattern P)

### 3. **Extract Insights — Từ Pattern Đến Meaning**

Transform patterns thành insights:
- **Insight = Pattern + Context + Implication**

VD:
- Pattern: "Reels reach 2x higher than static images"
- Context: "Across W20-W21, both on Facebook algo update month"
- Implication: "TikTok Reels-first strategy pays off on Facebook — double-down on video M2-3"

**Output:** 5–7 key insights (không phải 20 observations)

### 4. **Action Items — Từ Insight Đến Concrete Next Steps**

Mỗi insight → 1–2 action items:
- **What:** Cụ thể làm gì
- **Who:** Owner (bạn, team, vendor?)
- **When:** Deadline
- **Why:** Link back to insight (tracing logic)

**Output:** Prioritized action list (top 3 critical, top 5 nice-to-have)

---

## Example — Weekly Performance Synthesis

```
Sources:
1. Buffer analytics export (W20 reach/ER% per channel)
2. Notion content database (status + hypothesis tags)
3. Competitor posts (top 5 from Hang's audit)
4. User comments (10 most-liked comments from TikTok/FB)

[Skill runs 4 steps]

PATTERNS FOUND:
├─ P1: Reels (Video) ER% = 5.2% vs Static (Infographic) = 2.1% — 2.5x gap ✓ Confirms H1
├─ P2: "Luật Dân số" post = 200 shares (vs 40 avg) — but medical baseline not yet measured
├─ P3: Comments on "thai tuần 8" = 150, but competitors have 300+ on similar content
└─ P4: BS Thư voice/face = 40% higher engagement than generic design

INSIGHTS (5):
1. Reels format 2.5x better than static — algorithm signal validated. Action: allocate 70% video budget M2.
2. "Luật Dân số" viral signal = untapped angle — other OB/GYN not covering. Action: make 1 follow-up content tuần 21.
3. Comment volume low vs competitor — possibly tonality issue (too clinical). Action: A/B test warmer script W21.
4. BS Thư personal brand working — face content more engaging. Action: feature BS more in P3 "BS Thư Nói Thật".
5. TikTok watch completion vs Facebook ER% don't align — may have audience gap. Action: investigate viewer profile differences.

ACTION ITEMS (Prioritized):
[Critical — do this W21]
▢ Increase video % to 70% per week (owner: Content Execution, deadline 19/5)
▢ Create 1 follow-up Luật Dân số content (owner: BS Thư, deadline 20/5)

[High — do this M2]
▢ Test warmer script tone on TikTok (owner: Copywriter, deadline 26/5)
▢ Analyze TikTok vs FB audience profile (owner: Planner, deadline 31/5)

[Medium — do this M3]
▢ Feature BS Thư more in P3 (owner: Creative, deadline launch W25)
▢ Implement person-centric visual template (owner: Design, deadline 7/6)
```

---

## Output Format

Skill luôn sinh ra file `.md` dạng:

```markdown
# Synthesis Report — [Topic] — [YYYY-MM-DD]

**Sources:** [List files/data inputs]
**Synthesis window:** [Date range covered]
**Confidence level:** [High/Medium/Low — based on data quality]

---

## Data Landscape
[Quick summary: what data exist, what's missing]

## Patterns Identified
[3–7 key patterns với cross-reference vào sources]

## 5–7 Key Insights
[Numbered insights, each with: finding + context + implication]

## Action Items (Prioritized)
[Critical / High / Medium tier actions]

---

## Data Quality Notes
[Nếu có gaps hay inconsistencies, flag here — affect confidence level]

## Next Synthesis Trigger
[Khi nào nên chạy lại synthesis? E.g., W21 khi có new weekly metrics]
```

---

## Khi Nào Dùng

- ✅ **Weekly performance review:** Tổng 4 channels' metrics (Buffer, Notion, comments, hypothesis tracking)
- ✅ **Hypothesis measurement:** Combine multiple metric sources để validate H1-H3
- ✅ **Competitor intelligence:** Synthesize top 5 competitor posts + own content → identify gap
- ✅ **User feedback synthesis:** 50 comments from TikTok + DM + Notion → consolidated themes
- ✅ **Post-campaign analysis:** Combine all 4 Ps (Product, Promotion, Price, Place) metrics
- ❌ **Real-time decisions:** Quá slow — dùng khi data đã settle (end of week)
- ❌ **Operational reporting:** Không dùng nếu chỉ cần tóm tắt (dùng summary template thay vì synthesis)

---

## Tích Hợp Workflow

- **Content Execution Agent:** Chạy thứ 6 cuối tuần để synthesis W20 data → tạo weekly-summary
- **Content Planner Agent:** Chạy hàng tháng để synthesis monthly insights → decide content direction adjustment M+1

Skill output → lưu vào `outputs/[brand]/synthesis-[YYYY-MM-DD].md` → present to Planner

---

## Khác Biệt: Summary vs Synthesis vs Analysis

| | Summary | Synthesis | Analysis |
|---|---|---|---|
| **Input** | 1 source | 3+ sources | Historical series |
| **Output** | Tóm tắt facts | Patterns + implications | Trend + forecast |
| **Output goal** | "Chuyện gì xảy ra?" | "Tại sao & so sánh?" | "Sẽ như thế nào?" |
| **Effort** | Low | Medium | High (ML) |
| **Dùng khi** | Quick recap | Weekly review | Monthly planning |

**Sume-kit = Synthesis mode.** Nếu cần summary (facts recap), dùng template thay vì skill.

---

**Created:** 2026-05-12
**Agent:** Content Execution Data Integration
**Mục tiêu:** Extract signal từ noise = better decisions faster
