# Buffer Setup — Hướng Dẫn Chi Tiết

**Mục tiêu:** Tạo Buffer account, kết nối Facebook fanpage, lấy API token

---

## Bước 1: Tạo Buffer Account

### 1.1 Truy Cập Buffer
```
https://buffer.com
```

### 1.2 Sign Up
```
1. Click "Sign up" (hoặc "Get started free")
2. Email: [email của bạn]
3. Password: [tạo password mạnh]
4. Click "Create account"
5. Xác thực email (kiểm tra inbox)
```

### 1.3 Lựa Chọn Plan
```
Free plan: 5 social profiles (đủ dùng)
  - Posting (no scheduling)
  - Basic analytics
  - 1 user

Pro plan: $5/tháng
  - All from Free + Scheduling
  - Advanced analytics
  - Recommended for automation
```

**Khuyến cáo:** Dùng **Free plan trước**, upgrade thành Pro nếu cần scheduling advanced

---

## Bước 2: Kết Nối Facebook Fanpage

### 2.1 Trang Dashboard
```
1. Login Buffer
2. Bạn thấy: "Add your first channel"
3. Click button hoặc "Channels" menu → "Add Channel"
```

### 2.2 Chọn Facebook
```
1. Click "Facebook"
2. Chọn loại: "Facebook Page" (không phải Personal profile)
```

### 2.3 Kết Nối Facebook Account
```
1. Buffer sẽ redirect tới Facebook login
2. Login với Facebook account của bạn
3. Chọn fanpage cần kết nối
4. Click "Allow" để cấp quyền cho Buffer
5. Redirect lại Buffer → "Connected!"
```

### 2.4 Xác Nhận Kết Nối
```
Buffer Dashboard → "Your channels"
Nên thấy: [Fanpage name] — Connected ✅
```

---

## Bước 3: Lấy Buffer API Token (Quan Trọng)

### 3.1 Vào Settings
```
1. Buffer → Profile icon (top right)
2. Click "Settings"
```

### 3.2 Tìm API Tokens
```
1. Sidebar: "Integrations"
2. Tab: "API Tokens" (hoặc "Connected Apps")
```

### 3.3 Tạo Token Mới
```
1. Click "Create New Token"
2. Hoặc: "Generate API Token"
3. Confirm: "Yes, create token"
```

### 3.4 Copy Token
```
1. Token sẽ hiện dạng: abc123def456xyz...
2. Click "Copy to clipboard"
3. Paste vào file notes (VD: Google Keep, Notion)

⚠️ KHÔNG SHARE TOKEN NÀY VỚI AI HOẶC PUBLIC!
Nó giống password.
```

---

## Bước 4: Kiểm Tra Queue

### 4.1 Vào Queue
```
1. Buffer Dashboard
2. Chọn fanpage
3. Click "Queue" (hoặc "Scheduled posts")
```

### 4.2 Nên Thấy
```
- "Scheduled" tab (empty hoặc có posts cũ)
- "Publishing next" section
- Thời gian publish cho mỗi post
```

### 4.3 Test Manual Post
```
1. Click "Create post"
2. Viết: "Test post từ Buffer"
3. Schedule: 1 giờ tới
4. Click "Schedule"
5. Check Queue → Nên thấy post
```

**OK → Ready cho Zapier automation**

---

## Bước 5: Cấu Hình Tối Ưu (Advanced)

### 5.1 Posting Schedule
```
Buffer → Settings → [Fanpage] → Posting times

Khuyến cáo cho fanpage marketing:
  Thứ 2-5: 14:00 (2 chiều)
  Thứ 6: 10:00 (sáng)
  Thứ 7-CN: 18:00 (tối)
```

### 5.2 Auto-Schedule
```
Buffer → Settings → Auto-schedule

Nếu ON: Buffer tự động schedule post theo best time
(Khuyến cáo: OFF nếu dùng Zapier — ta schedule manual)
```

### 5.3 Analytics
```
Buffer → Analytics → [Fanpage]

Xem:
  - Reach (độ tiếp cận)
  - Engagement (tương tác)
  - Top posts
  - Best posting times
```

---

## Bước 6: Lỗi & Cách Khắc Phục

### Lỗi: "Cannot connect to Facebook"
**Nguyên nhân:** Quyền Facebook không đủ  
**Fix:**
1. Buffer → Channels → [Fanpage] → Disconnect
2. Re-connect và chọn quyền đầy đủ
3. Đảm bảo bạn là Admin of fanpage

### Lỗi: "API Token không hoạt động"
**Nguyên nhân:** Token hết hạn hoặc sai  
**Fix:**
1. Buffer Settings → Regenerate token
2. Copy token mới
3. Update trong Zapier

### Lỗi: "Post không đăng lúc scheduled"
**Nguyên nhân:** Fanpage bị restrict hoặc Buffer server issue  
**Fix:**
1. Check fanpage không bị locked
2. Manual post test
3. Contact Buffer support

---

## Tổng Hợp: Buffer Credentials Cho Zapier

Lưu trữ an toàn (VD: password manager):

```
Buffer Account:
  Email: _______________
  Password: _______________

Facebook Fanpage:
  Page name: _______________
  Page URL: _______________

API Token:
  Token: _______________
  (Lưu ở Zapier)
```

---

## Checklist: Ready for Zapier

- [ ] Buffer account created
- [ ] Facebook fanpage connected
- [ ] API token generated & copied
- [ ] Test post scheduled (& deleted after test)
- [ ] Analytics dashboard accessible
- [ ] Posting times configured
- [ ] Ready to connect to Zapier

✅ Done → Next: Setup Zapier (`zapier-template.md`)

---

**Ngày:** 2026-05-12  
**Status:** Ready for Zapier integration
