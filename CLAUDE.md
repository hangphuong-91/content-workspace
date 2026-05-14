# CLAUDE.md — Project Context & Rules

**For:** Claude instances running skills in this workspace  
**Version:** 2.0.0  
**Updated:** 2026-05-14

---

## 🎯 Project Overview

**Marketing Content Workspace v2** — Integrated system for content strategy + execution using 3 specialized agents.

### **3 Agents Architecture**

1. **Communication Strategist Agent** (CMO role)
   - Input: Brand info, market context, business goals
   - Output: Strategy docs + GPT analysis
   - Tools: WebSearch, WebFetch, OpenAI API (if OPENAI_API_KEY set), Notion
   - Cadence: Quarterly (once per 3 months)

2. **Content Planner Agent** (Strategy execution)
   - Input: communication-plan.md from Communication Strategist
   - Output: Content calendar + 3 Excel templates + Notion database
   - Tools: Notion, Google Drive, manual spreadsheet coordination
   - Cadence: Quarterly planning + weekly KPI review

3. **Content Execution Agent** (Production & publishing)
   - Input: content-plan.md from Content Planner
   - Output: Copy variations + visual briefs + AI prompts + weekly reports
   - Tools: WebSearch (algorithm updates), Notion updates, manual approvals
   - Cadence: Weekly (Monday-Sunday)

---

## 📋 Quy Tắc Ngôn Ngữ (BẮT BUỘC)

### Định Dạng Thuật Ngữ Chuyên Ngành
Khi dùng thuật ngữ marketing hoặc từ chuyên ngành: **tiếng Việt trước, mở ngoặc tiếng Anh sau**.

| Tiếng Việt | (Tiếng Anh) |
|---|---|
| Tỷ lệ tương tác | (Engagement Rate) |
| Trụ cột nội dung | (Content Pillar) |
| Câu thu hút | (Hook) |
| Lời kêu gọi hành động | (CTA) |
| Bài đăng nhiều ảnh | (Carousel) |
| Ảnh thông tin | (Infographic) |
| Chân dung khách hàng | (Persona) |
| Độ tiếp cận | (Reach) |
| Tái sử dụng nội dung | (Repurposing) |
| Phễu tiếp thị | (Funnel) |
| Sản xuất theo lô | (Batch Production) |
| Điểm khó khăn | (Pain Point) |
| Thuật toán | (Algorithm) |
| Kế hoạch nội dung | (Content Plan) |
| Phân tích khoảng trống | (Gap Analysis) |
| Thương hiệu cá nhân | (Personal Brand) |
| Lịch nội dung | (Content Calendar) |

### Giữ Nguyên (Không Dịch)
- Tên nền tảng: Facebook, TikTok, Instagram, YouTube, LinkedIn, Pinterest
- Tên công cụ: Canva, Buffer, CapCut, Mailchimp, Notion, Claude
- Tên tính năng chính thức: Reels, Stories, Tin
- Từ viết tắt phổ biến: SEO, KPI, SWOT (giải thích lần đầu nếu cần)
- Hashtag vẫn dùng ký hiệu #

### Không Được Làm
- Không viết "check content plan" → viết "kiểm tra kế hoạch nội dung (Content Plan)"
- Không viết "post 3 lần/tuần" → viết "đăng bài 3 lần/tuần"
- Không viết "engagement cao" → viết "tỷ lệ tương tác (Engagement Rate) cao"
- Không trộn tiếng Anh vào giữa câu tiếng Việt

---

## Ngữ Cảnh Dự Án

Đây là workspace marketing cho solo marketer hoặc nhóm nhỏ người Việt Nam. Người dùng là marketer chuyên nghiệp — không giải thích khái niệm cơ bản, tập trung vào chiến lược và thực thi.

**Ngành thử nghiệm:** Bác sĩ sản phụ khoa tư nhân tại TPHCM  
**Mục tiêu:** Tạo chiến lược nội dung 3 tháng → thực thi hàng tuần với 3 agents + 10 skills

---

## 10 Skills & Cadence

### **New Skills (v2.0) — Associated with Agents**

| Skill | Command | Agent | Cadence |
|-------|---------|-------|---------|
| **Market Intelligence** | `/market-intelligence [brand] [month]` | Comm Strategist | Monthly |
| **Performance Tracking** | `/performance-tracking [brand] [period]` | Content Planner | Weekly |
| **Weekly Report** | `/weekly-report [brand] [week]` | Content Execution | Weekly |

### **Legacy Skills (v1.0) — Still Used**

| Skill | Command | Used By | When |
|-------|---------|---------|------|
| **Competitor Research** | `/competitor research [brand]` | Comm Strategist | Quarterly + on demand |
| **Platform Algorithm** | `/platform algorithm [platform]` | Content Execution | Before writing each week |
| **Content Plan** | `/content plan [topic]` | Content Planner | Quarterly |
| **Copywrite** | `/copywrite [platform] [brief]` | Content Execution | Weekly |
| **Visual Creative** | `/visual creative [brief]` | Content Execution | Weekly |
| **AI Execution** | `/ai execution [plan-file]` | Content Planner | After content plan |
| **Schedule Posting** | `/schedule posting [brand]` | Content Execution | Manual posting setup |

**Thứ tự chạy chuẩn:**
1. Communication Strategist phases 0→6 (quarterly)
2. Content Planner → /content plan (quarterly)
3. Content Execution → Weekly workflow (Monday-Sunday each week)

---

## Quy Tắc Đầu Ra

- Tất cả file output lưu vào `outputs/[tên-thương-hiệu]-[YYYY-MM]/`
- File formats:
  - `.md` = Strategy docs, copywriting briefs, content outlines
  - `.json` = GPT analysis data (structured, machine-readable)
  - `.xlsx` = Live tracking, KPI metrics, Excel calendars
  - `.py` = Automation helpers (e.g., openai-research-helper.py)
- Mỗi output có timestamp + creator info (frontmatter)
- Tuân thủ ngành: Không dùng "chữa khỏi", dùng "hỗ trợ cải thiện"
- Commit output lên GitHub sau mỗi workflow (agent run)

---

## Phong Cách Viết

- **Giọng điệu:** Ấm áp nhưng chuyên nghiệp — như người đồng nghiệp giàu kinh nghiệm
- **Độ dài:** Đủ thông tin, không lòng vòng
- **Cấu trúc:** Header rõ ràng, dùng bảng khi có nhiều dữ liệu, bullet point khi liệt kê
- **Số liệu:** Dùng nghìn (K) thay vì "50,000" — viết "50 nghìn"
