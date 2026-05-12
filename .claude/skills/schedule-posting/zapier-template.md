# Hướng Dẫn Chi Tiết — Setup Zapier Automation

**Mục tiêu:** Tạo Zap để tự động post từ Notion → Buffer → Facebook

---

## Bước 1: Tạo Zap Mới

### 1.1 Truy Cập Zapier
```
1. Vào https://zapier.com
2. Login (hoặc Sign up nếu chưa có)
3. Dashboard → "Create" → "New Zap"
```

### 1.2 Đặt Tên Zap
```
Zap name: "[Brand] - Content Scheduler"
Description: "Auto-schedule content từ Notion vào Facebook qua Buffer"
```

---

## Bước 2: Cấu Hình Trigger (Notion)

### 2.1 Chọn App Trigger
```
1. Search: "Notion"
2. Chọn "Notion"
3. Chọn Event: "Database - Row Updated" (hoặc "Row Created")
```

### 2.2 Kết Nối Notion
```
1. Click "Sign in with Notion"
2. Chọn Notion workspace
3. Grant permissions → Done
```

### 2.3 Cấu Hình Trigger
```
Database: "Content Plan — [Brand] — [Tháng/Năm]"

Filter (QUAN TRỌNG):
  Condition: Status is equal to "✅ Ready"
  
(Chỉ trigger khi row có Status = ✅ Ready)
```

### 2.4 Test Trigger
```
1. Click "Test trigger"
2. Zapier sẽ lấy danh sách rows từ Notion
3. Chọn 1 row để test
4. Click "Continue with selected record"
```

**Kiểm tra:** Nên thấy dữ liệu từ Notion (Title, Publish Date, CTA, v.v.)

---

## Bước 3: Cấu Hình Action 1 (Buffer - Create Post)

### 3.1 Chọn App Action
```
1. Search: "Buffer"
2. Chọn "Buffer"
3. Chọn Event: "Create Post"
```

### 3.2 Kết Nối Buffer
```
1. Click "Sign in with Buffer"
2. Cho phép access
3. Chọn tài khoản Buffer
4. Done
```

### 3.3 Cấu Hình Post

**Field 1: Profile**
```
Chọn: [Facebook fanpage name]
```

**Field 2: Post Text (Nội dung bài viết)**
```
Công thức:
[Title] 

[Angle]

[CTA] → [Link nếu có]

---
#[Pillar hashtag]

Ví dụ mapping:
- {Title} = Notion: Title field
- {Angle} = Notion: Angle field
- {CTA} = Notion: CTA field
- {Pillar hashtag} = Notion: Pillar field (convert to hashtag)
```

**Field 3: Schedule Time (Thời gian đăng)**
```
Type: "Specific date/time"
Value: {Publish Date} từ Notion

Ví dụ: 2026-05-15 14:00 (14h chiều ngày 15/5)
```

**Field 4: Image/Media (Tuỳ chọn)**
```
Nếu có visual trong Notion:
  - URL: {Visual URL từ Notion Notes field}
  - hoặc: Lưu link Canva trong Notes
```

### 3.4 Test Action
```
1. Click "Test action"
2. Zapier sẽ gửi test post tới Buffer
3. Check Buffer dashboard → Nên thấy post ở queue
4. Xóa test post khỏi Buffer (nếu cần)
```

---

## Bước 4: Cấu Hình Action 2 (Notion - Update Row)

### 4.1 Chọn App Action
```
1. Click "Add another action"
2. Search: "Notion"
3. Chọn Event: "Update Database Item"
```

### 4.2 Kết Nối Notion
```
(Đã kết nối từ Trigger, nên skip)
```

### 4.3 Cấu Hình Update

**Field 1: Database**
```
Chọn: "Content Plan — [Brand] — [Tháng/Năm]"
(Cùng database từ trigger)
```

**Field 2: Row ID**
```
Chọn: {ID} từ Notion trigger (tự động)
```

**Field 3: Update Fields**

Update 3 fields:

| Field | Giá Trị |
|---|---|
| **Status** | 📤 Published |
| **Published Date** | {Publish Date từ Notion} hoặc {Today} |
| **Notes** | "Posted via Zapier\nBuffer link: [auto-filled later]" |

### 4.4 Test Action
```
1. Click "Test action"
2. Check Notion → Row nên update Status = 📤 Published
3. Nếu ok, continue
```

---

## Bước 5: Turn ON Zap

```
1. Review toàn bộ Zap:
   Trigger: Notion (Status = Ready)
   ↓
   Action 1: Buffer (Post)
   ↓
   Action 2: Notion (Update)

2. Click "Publish" (hoặc "Turn on" nếu đã tạo)

3. Zap bây giờ ACTIVE ✅
```

---

## Bước 6: Test End-to-End

### 6.1 Chuẩn Bị Content
```
1. Mở Notion "Content Plan"
2. Chọn 1 row test (ví dụ: "Thai kỳ tuần 28")
3. Kiểm tra:
   - Title: ✅ Có
   - Angle: ✅ Có
   - CTA: ✅ Có
   - Publish Date: ✅ 2026-05-15 14:00
   - Status: Hiện tại = "✍️ Draft"
```

### 6.2 Trigger Zap
```
1. Notion: Update Status → ✅ Ready
2. Chờ 30 giây (Zapier delay)
3. Check Buffer → Nên thấy post ở queue lúc 14:00
4. Check Notion → Status nên = 📤 Published
```

### 6.3 Kết Quả
```
✅ Buffer queue: Post scheduled for 2026-05-15 14:00
✅ Notion: Status updated = 📤 Published
✅ Zap working correctly!
```

---

## Advanced: Customize Post Text

Nếu muốn format đẹp hơn, dùng:

```
🎯 {Title}

💡 {Angle}

👉 {CTA}

#{{Pillar}}

---
📅 Đăng lúc: {Publish Date}
💼 {Brand Name}
```

Hoặc theo brand guidelines của bạn.

---

## Troubleshooting

### Lỗi: "Cannot find database"
**Fix:**
1. Đảm bảo Notion database tên chính xác
2. Zapier được cấp access tới database đó
3. Re-connect Notion

### Lỗi: "Buffer profile not found"
**Fix:**
1. Buffer account → Settings → Verify Facebook page kết nối đúng
2. Zapier → Reconnect Buffer
3. Re-test

### Post không vào queue
**Fix:**
1. Check Buffer analytics logs
2. Xem Zapier task history (Dashboard → Zap → View logs)
3. Thường do token hết hạn → Reconnect

### Notion không update
**Fix:**
1. Check Notion field names đúng không
2. Re-test Action 2
3. View Zapier logs để thấy error detail

---

## Dùng Lại (Recurring)

Sau khi setup xong, mỗi tuần:

```
Thứ 2: Tạo content trong Notion
Thứ 4: Chạy /copywrite + /visual creative
Thứ 5: Update Status → ✅ Ready (Zapier tự động trigger)
Thứ 6 đến CN: Buffer tự động post theo schedule
```

**Zero manual posting effort!**

---

**Ngày:** 2026-05-12  
**Status:** Ready to setup
