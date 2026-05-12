# Checklist: Notion Database Chuẩn Bị Cho Scheduling

**Mục tiêu:** Đảm bảo Notion database đã setup đúng để Zapier hoạt động

---

## Columns (Properties) Cần Có

### Bắt Buộc (MUST HAVE)

- [ ] **Title** (Title field)
  - Ví dụ: "Thai kỳ tuần 28 - Phát triển bé"
  - Dùng cho: Post content

- [ ] **Kênh** (Select field)
  - Options: Facebook / TikTok / Instagram / LinkedIn / Blog / Email
  - Dùng cho: Buffer profile selection

- [ ] **Publish Date** (Date field)
  - Format: 2026-05-15 14:00 (nếu có time)
  - Dùng cho: Scheduled time ở Buffer

- [ ] **Status** (Select field)
  - Options: 📋 Planned / ✍️ Draft / 👀 Review / ✅ Ready / 📤 Published / 📊 Measured
  - **Quan trọng:** ✅ Ready = trigger Zapier automation
  - Dùng cho: Zapier filter

### Khuyến Cáo (RECOMMENDED)

- [ ] **Angle** (Text field)
  - Ví dụ: "Myth-busting - xây dựng niềm tin"
  - Dùng cho: Post caption/description

- [ ] **CTA** (Text field)
  - Ví dụ: "Đặt lịch khám → Link"
  - Dùng cho: Call-to-action ở cuối post

- [ ] **Pillar** (Select field)
  - Options: [Tên 3-5 pillars từ content plan]
  - Dùng cho: Hashtag grouping

- [ ] **Format** (Select field)
  - Options: Video / Infographic / Carousel / Post / Article / Script
  - Dùng cho: Format indicator

- [ ] **AI Tool** (Select field)
  - Options: Claude / Canva AI / DALL-E / Manual
  - Dùng cho: Tool tracking

- [ ] **Notes** (Text field)
  - Dùng cho: Link post sau khi publish, ghi chú thêm

### Tracking (OPTIONAL)

- [ ] **Published Date** (Date field)
  - Điền sau khi post
  - Dùng cho: Performance tracking

- [ ] **Reach** (Number field)
  - Điền sau khi post (48h)
  - Dùng cho: Analytics

- [ ] **Engagement** (Number field)
  - Reactions + Comments + Shares
  - Dùng cho: Analytics

- [ ] **ER%** (Formula field)
  - Formula: `prop("Engagement") / prop("Reach") * 100`
  - Dùng cho: Engagement Rate calculation

---

## Status Workflow Chuẩn

Đảm bảo workflow này hiểu rõ:

```
📋 Planned (kế hoạch ban đầu)
    ↓ (Sau khi chạy /copywrite + /visual creative)
✍️ Draft (đã viết/thiết kế)
    ↓ (Review & approval)
👀 Review (chờ duyệt)
    ↓ (Approved, ready to publish)
✅ Ready ← ⭐ ZAPIER TRIGGERS HERE
    ↓ (Zapier schedules vào Buffer)
📤 Published (posted, Notion auto-updated)
    ↓ (Sau 48h, điền metrics)
📊 Measured (analytics collected)
```

**Quan trọng:** Khi update Status → ✅ Ready, Zapier tự động trigger

---

## Tạo Views Để Facilitate Workflow

### View 1: "By Week" (GROUP BY TUẦN)
```
Database → "+" → New view
Name: "By Week"
Type: Table
Group by: "Tuần" field
Filter: Tháng = [Current month]

Lợi ích: Xem clear tuần này cần publish bao nhiêu
```

### View 2: "By Status" (GROUP BY STATUS)
```
Name: "By Status"
Type: Table
Group by: "Status" field

Lợi ích: Thấy pipeline: Planned → Draft → Review → Ready → Published
```

### View 3: "Calendar View" (BY PUBLISH DATE)
```
Name: "Publishing Calendar"
Type: Calendar
Date property: "Publish Date"

Lợi ích: Visual lịch đăng, avoid conflicting dates
```

### View 4: "Ready to Schedule" (FILTER)
```
Name: "Ready to Schedule"
Type: Table
Filter: Status = "✅ Ready"

Lợi ích: Nhanh thấy posts chờ Zapier trigger
```

---

## Sample Row Setup

Tạo 1 row test để verify:

```
| Field | Giá Trị |
|---|---|
| Title | "Thai kỳ tuần 28 - Phát triển bé" |
| Kênh | Facebook |
| Status | ✍️ Draft |
| Publish Date | 2026-05-15 14:00 |
| Angle | "Myth-busting: Bé nghe được gì ở tuần 28?" |
| CTA | "Đặt lịch khám → link" |
| Pillar | "Giáo dục thai kỳ" |
| Format | Infographic |
| AI Tool | Canva AI |
| Notes | "Link Canva: [URL]" |
```

**Test:**
1. Create row này
2. Status = ✍️ Draft
3. Publish Date = hôm nay + 1 tiếng
4. Khi ready → Update Status = ✅ Ready
5. Check Buffer → Nên thấy post ở queue

---

## Zapier Integration Checklist

Trước khi setup Zapier, đảm bảo:

- [ ] Notion database được share với Zapier app
  - Database → Share → "+ Add guests"
  - Tìm "Zapier" → Add access

- [ ] Tất cả columns tên chính xác (không typo)
  - VD: "Status" không phải "status"

- [ ] Status options có "✅ Ready"
  - Không phải "ready" hoặc "READY"

- [ ] Publish Date field là Date type
  - Không phải Text hoặc Single line

- [ ] Có ít nhất 1 row sample (test)

- [ ] Notion workspace không private
  - Settings → Access → Allow third-party apps

---

## Hành Động Hàng Tuần

Để Zapier hoạt động smooth:

### Thứ 2 (Planning)
```
[ ] Tạo 4-6 rows mới cho tuần này
[ ] Status = 📋 Planned
[ ] Điền: Title, Kênh, Pillar, CTA, Publish Date
```

### Thứ 4 (Content Creation)
```
[ ] Chạy /copywrite cho mỗi row
[ ] Update Status = ✍️ Draft
[ ] Chạy /visual creative
[ ] Update Notes với link design
```

### Thứ 5 (Approval & Scheduling)
```
[ ] Review toàn bộ draft
[ ] Status = 👀 Review (nếu cần feedback)
[ ] Hoặc: Status = ✅ Ready (nếu approve)
[ ] Zapier tự động trigger
[ ] Check Buffer queue
```

### Thứ 6 đến CN (Publishing)
```
[ ] Buffer tự động post lúc scheduled
[ ] Zapier tự động update Notion (Status = 📤 Published)
[ ] Zero manual work! ✅
```

### Thứ 2 tuần sau (Measuring)
```
[ ] Vào Buffer Analytics
[ ] Điền Reach + Engagement vào Notion
[ ] Status = 📊 Measured
```

---

## Troubleshooting: Notion Side

### Zapier không trigger
**Fix:**
1. Check Status = "✅ Ready" (đúng chính xác)
2. Database shared với Zapier
3. Zapier → Reconnect Notion
4. Re-test

### Zapier update Notion fail
**Fix:**
1. Check field names chính xác
2. Format values match options (VD: "📤 Published" exact match)
3. Zapier logs → xem error detail

### Missing columns
**Fix:**
1. Add missing columns to database
2. Zapier → Refresh field list
3. Re-map fields trong Zap

---

## Final Checklist: Ready for Zapier

**Notion Database:**
- [ ] Title column ✅
- [ ] Kênh column ✅
- [ ] Publish Date (Date type) ✅
- [ ] Status column với option "✅ Ready" ✅
- [ ] Angle, CTA, Pillar, Format columns ✅
- [ ] Database shared với Zapier ✅
- [ ] 1 sample row tạo & tested ✅
- [ ] Views setup (By Week, By Status, Calendar) ✅

**Ready → Next step:** Zapier setup (`zapier-template.md`)

---

**Ngày:** 2026-05-12  
**Status:** Database ready for automation
