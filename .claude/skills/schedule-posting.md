# Skill: Lịch Đăng Bài Tự Động — Buffer + Zapier

**Lệnh:** `/schedule posting [brand] [tháng]`

**Chức năng:** Tự động schedule content từ Notion → Buffer → Facebook fanpage theo lịch

**Thời gian:** 5 phút setup lần đầu, sau đó tự động 100%

---

## Workflow Tổng Quát

```
Notion Database (Content Calendar)
    ↓ (Zapier automation)
Buffer Queue (scheduling tool)
    ↓ (Buffer scheduled task)
Facebook Fanpage (tự động đăng)
    ↓
Notion: Update Published Date + Link
```

---

## Điều Kiện Tiên Quyết

### 1. Notion Database
- ✅ Content Calendar đã tạo từ `/content plan`
- Columns cần có:
  - **Kênh** (Channel) — Facebook / TikTok / Instagram / LinkedIn
  - **Publish Date** — Ngày dự kiến đăng
  - **Status** — ✅ Ready (mới được schedule)
  - **Notes** — Để lưu link post sau khi đăng

### 2. Buffer Account
- Tạo tại: https://buffer.com
- Plan: **Free (5 social profiles) hoặc Pro ($5/tháng)**
- Kết nối Facebook fanpage vào Buffer

### 3. Zapier Account
- Tạo tại: https://zapier.com
- Plan: **Free (100 tasks/tháng) đủ dùng**
- Authentication: Email + password

### 4. Facebook Business Account
- Admin của fanpage cần cấp quyền cho Buffer
- Hoặc: Tạo Facebook App + generate token (advanced)

---

## Bước 1: Setup Buffer

### 1.1 Tạo Buffer Account
```
1. Vào https://buffer.com → Sign up
2. Email + password
3. Kết nối kênh: Facebook Page → Chọn fanpage
4. Lấy Buffer API Token:
   - Settings → Integrations → API Tokens
   - Generate new token → Copy
```

**Lưu token này — cần cho Zapier**

### 1.2 Kiểm Tra Queue
```
Buffer Dashboard → [Your Page] → Queue
Nên trống hoặc có vài posts hiện tại
```

---

## Bước 2: Setup Zapier Automation

### 2.1 Tạo Zap Mới
```
1. Zapier.com → Create → New Zap
2. Chọn trigger: Notion → Database → Row Updated
3. Cấu hình Notion:
   - Database: "Content Plan — [Brand] — [Tháng]"
   - Update filter: Status = "✅ Ready"
   - Event: When row updated
```

### 2.2 Thêm Buffer Action
```
1. Action: Buffer → Create Post
2. Kết nối Buffer:
   - Button "Connect Buffer"
   - Paste token từ step 1.1
3. Cấu hình posting:
   - Profile: [Chọn Facebook fanpage]
   - Post text: {Notion Title} + {Angle} + {CTA}
   - Scheduled time: {Publish Date} từ Notion
   - Attach image: {Visual link từ Notion (nếu có)}
```

### 2.3 Thêm Notion Update (Post-Publishing)
```
1. Action 2: Notion → Update Database Item
2. Cấu hình:
   - Database: Content Plan
   - Row: Same row từ trigger
   - Update fields:
     - Status → 📤 Published
     - Notes → {Buffer post link}
     - Published Date → {today}
```

### 2.4 Test Zap
```
1. Click "Test" → Chọn 1 row trong Notion
2. Update Status = ✅ Ready
3. Check Buffer → Nên thấy post ở queue
4. Turn Zap ON
```

---

## Bước 3: Sử Dụng Hàng Tuần

### Workflow Hàng Tuần

**Thứ 2 (Lên Kế Hoạch):**
1. Mở Notion "Content Calendar — By Week"
2. Xem tuần này có bao nhiêu content cần đăng
3. Chạy `/copywrite` + `/visual creative` để tạo nội dung

**Thứ 4 (Approve & Schedule):**
1. Review content trong Notion (Status = ✍️ Draft)
2. Update Status → ✅ Ready (tự động trigger Zapier)
3. Buffer sẽ tự động schedule theo Publish Date

**Thứ 5 (Publish):**
- Buffer tự động post lúc scheduled time
- Zapier tự động update Notion: Status → 📤 Published

**Thứ 2 tuần sau (Measure):**
1. Vào Buffer → Analytics
2. Điền Reach + Engagement vào Notion
3. Update Status → 📊 Measured

---

## Mẫu Zapier Configuration

Xem chi tiết: `.claude/skills/schedule-posting/zapier-template.md`

---

## Troubleshooting

### Buffer không post
**Nguyên nhân:** Token hết hạn hoặc fanpage chưa kết nối  
**Fix:**
1. Buffer Settings → Integrations → Refresh token
2. Zapier → Reconnect Buffer
3. Test lại

### Zapier task hết quota
**Nguyên nhân:** Free plan = 100 tasks/tháng (~3-4 posts/tuần)  
**Fix:**
- Upgrade Buffer Pro ($5/tháng) để có unlimited Zapier tasks
- Hoặc: Setup Zapier Pro ($19.99/tháng)

### Notion không update sau khi post
**Nguyên nhân:** Zapier 2nd action failed  
**Fix:**
1. Zapier → Dashboard → Xem error log
2. Re-test Notion update action
3. Check field names đúng không

---

## Advanced: Multi-Platform Scheduling

Nếu muốn schedule cho **Facebook + Instagram + TikTok**:

1. **Buffer Pro** ($5/tháng) — hỗ trợ 6 platforms
2. **Thêm action trong Zapier:**
   ```
   Zapier Trigger (Notion)
   → Buffer Post (Facebook)
   → Buffer Post (Instagram)  
   → Buffer Post (TikTok)
   → Notion Update
   ```

---

## Chi Phí Hàng Tháng

| Công cụ | Free | Pro | Ghi chú |
|---|---|---|---|
| **Zapier** | 100 tasks | $19.99 | Đủ cho 3-4 posts/tuần |
| **Buffer** | 5 profiles | $5 | Cơ bản + analytics |
| **Notion** | Unlimited | Free | Miễn phí |
| **Meta Business Suite** | Free | — | Scheduling native, nhưng chậm |
| **Tổng** | **Free** | **~$24.99/tháng** | Tối ưu 80/20 |

---

## Next Steps

1. ✅ Setup Buffer account + lấy token
2. ✅ Tạo Zap trong Zapier
3. ✅ Test với 1 content piece
4. ✅ Turn ON Zap
5. ✅ Chạy hàng tuần cùng `/copywrite` + `/visual creative`

---

**Tạo bởi:** Claude Code — Marketing Content Workspace  
**Ngày:** 2026-05-12  
**Trạng thái:** Ready to setup
