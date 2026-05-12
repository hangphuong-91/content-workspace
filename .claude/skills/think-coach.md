# Skill: Think-Coach — Structured Problem Decomposition

**Trigger:** `/think-coach [problem statement]`

**Thời gian:** 10–15 phút per session

**Dùng khi nào:** Bạn cần phân rã problem phức tạp thành các thành phần nhỏ, xác định constraints, rủi ro, trước khi hành động. Phù hợp cho QA gate trước khi publish content, hoặc validate strategy.

---

## Quy Trình — 5W/1H Framework

Với bất kỳ problem nào, skill sẽ:

### 1. **What — Định Nghĩa Vấn Đề**
- Vấn đề chính xác là gì?
- Nó ảnh hưởng gì?
- Scope: toàn org hay từng team?

**Output:** 1 câu định nghĩa rõ ràng

### 2. **Why — Gốc Rễ & Động Lực**
- Tại sao vấn đề lại xảy ra?
- Motivation: tại sao nó quan trọng ngay bây giờ?
- Cost of inaction: chi phí nếu không fix?

**Output:** 3–5 root causes candidate

### 3. **Who — Stakeholders & Ownership**
- Ai bị ảnh hưởng (decision maker, executor, user)?
- Ai sở hữu giải pháp?
- Ai cần sign-off?

**Output:** Stakeholder map + decision authority

### 4. **Where — Context & Constraints**
- Constraints: ngân sách, thời gian, resources, compliance?
- Trade-offs: cái gì phải hy sinh để có cái khác?
- Dependencies: vấn đề này phụ thuộc gì?

**Output:** Constraint matrix + critical path

### 5. **When — Timing & Urgency**
- Deadline thực tế là khi nào?
- MVP version: phải có gì bây giờ vs sau?
- Phased rollout hay big bang?

**Output:** Timeline + milestone

### 6. **How — Solution Directions (3 options)**
Với constraints ở #4, sinh ra 3 solution approaches:
- **Option A:** Conservative (low risk, low reward, chắc chắn work)
- **Option B:** Balanced (trung bình risk/reward, practical)
- **Option C:** Ambitious (high risk, high reward, cần verify)

Mỗi option gồm: approach cụ thể + pros/cons + effort + risk.

**Output:** Decision matrix với 3 options

---

## Example — Content Plan QA Gate

```
Problem: "Mình muốn verify chiến lược pillar trước khi publish plan lên Notion"

[Skill runs 5W/1H:]

WHAT: Pillar strategy P1-P5 có đủ sâu + khác biệt không? Có overlap không?
├─ Scope: Toàn Q2 content
└─ Ảnh hưởng: Nếu overlap → bài bị confusing, audience không clear segmentation

WHY: P1-P5 được tạo từ admin logic (Thai kỳ lo lắng, cẩm nang, BS opinion, Mẹ thái, News) — chưa validate lại từ audience intent
├─ Cost of inaction: 40% content bị thừa hoặc confusing → reach thấp, optimization khó
└─ Motivation: Hypothesis H1-H3 phụ thuộc vào pillar rõ ràng

WHO: Content Planner (verify logic) → Content Execution (implement) → BS Thư (approve tone)

WHERE: Constraints:
├─ Time: 1 tuần để adjust plan nếu cần
├─ Resource: Chỉ BS Thư + Content Planner
└─ Compliance: Luật KCB 2023 — pillar P5 cần extra review vì news

WHEN: Bây giờ (deadline W19) bớt hơn wait đến W20 (deadline tuần thực thi)

HOW: 3 solutions:
├─ Option A: Keep P1-P5 as-is. Pros: timeline tight, ready ngay. Cons: risk overlap khi execute.
├─ Option B: Merge 2 pillar (P3+P4), test with H1 data W20-21, adjust. Pros: better segmentation, low risk. Cons: delay 3 ngày.
└─ Option C: Rebuild pillar từ persona intent (Thủy Q&A vs Hương concern). Pros: scientifically sound. Cons: 1 week rebuild, high effort.

RECOMMENDATION: Option B. Effort vs reward = best. Merge P3+P4, validate W20-21.
```

---

## Output Format

Skill luôn sinh ra file `.md` dạng:

```markdown
# Think-Coach Session — [Problem Title]

**Date:** [YYYY-MM-DD]
**Submitted by:** [User name]
**Status:** [Recommended / In Review / Approved]

---

## Problem Statement
[What]

## Root Causes & Motivation
[Why]

## Stakeholder Map
[Who]

## Constraints & Trade-offs
[Where]

## Timing & Phases
[When]

## 3 Solution Options
[How — Option A/B/C]

---

## Recommendation
[Highest signal solution based on constraints]

## Next Action
[Specific next step + owner + deadline]
```

---

## Khi Nào Dùng

- ✅ **Content strategy:** QA gate trước khi publish (validate pillar, messaging, KPI)
- ✅ **Product roadmap:** Prioritize features (compare 3 options, identify constraints)
- ✅ **Team conflict:** Structured debate (WHO vs HOW, highlight trade-offs)
- ✅ **Resource allocation:** 70% AI vs agency mix (cost-benefit analysis)
- ❌ **Brainstorm:** Không dùng for open-ended ideation (dùng Sume-kit cho synthesis)
- ❌ **Execution:** Không dùng nếu đã quyết định (dùng để validate decision trước, không change mind sau)

---

## Tích Hợp Workflow

- **Content Planner Agent:** Chạy trước khi publish plan (QA gate)
- **Content Execution Agent:** Chạy khi có blockers (định hướng priority)

Skill output → lưu vào `outputs/[brand]/think-coach-[YYYY-MM-DD].md` → reference vào Notion

---

**Created:** 2026-05-12
**Agent:** Content Planner QA
**Mục tiêu:** Cải thiện decision quality = reduce rework = faster execution
