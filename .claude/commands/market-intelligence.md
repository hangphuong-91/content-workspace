# Skill: Nghiên Cứu Thị Trường — Market Intelligence

**Lệnh:** `/market-intelligence [brand] [tháng]`

**Chức năng:** 1 skill thay cho 3 — SEO keywords + algorithm updates + competitor pulse — chạy hàng tháng, date-stamped

**Thời gian:** 15–20 phút mỗi lần chạy

**Chạy khi nào:** Đầu mỗi tháng, trước khi điều chỉnh kế hoạch nội dung (Content Plan)

---

## Đây Không Phải Là

- **Không** thay thế `/competitor research` (audit sâu hàng quý)
- **Không** thay thế `/platform algorithm` (tra algorithm trước khi viết bài)
- Đây là **monthly pulse check** — nhanh, tươi, actionable

---

## Quy Trình Chạy

### Phase 1 — SEO & Từ Khóa (5 phút)

**Bước 1: Search từ khóa trending trong ngành**
```
WebSearch: "[ngành] trending topics [tháng/năm] Việt Nam"
WebSearch: "[topic chính] tìm kiếm nhiều nhất [tháng]"
WebFetch: trends.google.com/trends (nếu accessible)
```

**Bước 2: Phân tích nhu cầu tìm kiếm**
- Top 10 từ khóa người đang tìm trong ngành tháng này
- Từ khóa nào đang tăng (trending up) vs giảm
- Câu hỏi thường gặp (People Also Ask) liên quan đến brand
- Angle nội dung phù hợp với từng từ khóa

**Nếu có Ahrefs/SEMrush API key:**
```
→ Điền API key trong section "Tích Hợp API" bên dưới
→ Skill tự kéo volume + keyword difficulty + CPC
→ Output chính xác hơn nhiều
```

---

### Phase 2 — Algorithm Updates (5 phút)

**Bước 1: Tra algorithm tươi từng nền tảng**

Chạy cho 2–3 nền tảng chính của brand (Facebook, TikTok, Instagram mặc định):

```
WebSearch: "Facebook algorithm update [tháng năm hiện tại]"
WebFetch: newsroom.fb.com/news/
WebSearch: "TikTok algorithm [tháng năm] what's working"
WebFetch: newsroom.tiktok.com/
```

**Bước 2: Tổng hợp thay đổi**
- Gì đang được ưu tiên tháng này?
- Gì đang bị giảm reach?
- Format nào đang trending (Reels, Carousel, Text post...)?
- Thay đổi nào ảnh hưởng trực tiếp đến brand?

---

### Phase 3 — Competitor Pulse (5 phút)

**Đây là check nhanh — không phải audit sâu**

```
WebSearch: "[tên đối thủ chính] Facebook/TikTok [tháng năm]"
WebFetch: [URL fanpage đối thủ nếu public]
```

**Quan sát 3 điều:**
1. Bài nào của đối thủ có tương tác (Engagement) cao nhất tháng này?
2. Format/angle nào họ đang dùng nhiều?
3. Chủ đề nào họ chưa khai thác (gap mới)?

---

## Output — File Date-Stamped

**Lưu tại:** `outputs/[brand]-[YYYY-MM]/market-intelligence-[YYYY-MM].md`

```markdown
# Nghiên Cứu Thị Trường — [Brand] — [Tháng/Năm]

**Ngày chạy:** [Date]
**Người chạy:** Content Planner Agent
**Hiệu lực đến:** [Ngày cuối tháng]

---

## 1. Từ Khóa & Xu Hướng Tìm Kiếm (SEO)

### Top 10 Từ Khóa Tháng Này
| Từ khóa | Xu hướng | Volume* | Angle gợi ý |
|---|---|---|---|
| [từ khóa 1] | ↑ Tăng | [cao/TB/thấp] | [angle] |
| ... | | | |

*Volume: Ước tính từ Google Trends / Ahrefs nếu có

### Câu Hỏi Người Dùng Đang Tìm
1. [Câu hỏi 1]
2. [Câu hỏi 2]
3. [Câu hỏi 3]

### Gợi Ý Nội Dung Từ SEO
- Blog: [Tiêu đề bài blog có từ khóa]
- FAQ post: [Câu hỏi → trả lời ngắn cho Facebook]
- Video: [Angle video cho TikTok từ câu hỏi trending]

---

## 2. Cập Nhật Thuật Toán (Algorithm)

### Facebook — [Tháng/Năm]
- ✅ Đang ưu tiên: [...]
- ❌ Đang bị giảm: [...]
- 💡 Best practice tháng này: [...]

### TikTok — [Tháng/Năm]
- ✅ Đang ưu tiên: [...]
- ❌ Đang bị giảm: [...]
- 💡 Best practice: [...]

### [Platform khác nếu có]
...

### Thay Đổi Quan Trọng Cần Adjust Ngay
1. [Action item 1]
2. [Action item 2]

---

## 3. Đối Thủ — Pulse Check Tháng Này

### Bài Viral Nhất Của Đối Thủ
| Đối thủ | Bài | Format | Tương tác ước tính | Angle |
|---|---|---|---|---|
| [Đối thủ A] | [Tóm tắt] | Video | [cao/TB] | [angle] |

### Gap Mới Phát Hiện Tháng Này
- [Chủ đề đối thủ chưa khai thác]
- [Format đối thủ chưa dùng]

---

## 4. Khuyến Nghị Cho Tháng Tới

### Điều Chỉnh Kế Hoạch Nội Dung
- [ ] Thêm từ khóa [...] vào bài blog tuần [X]
- [ ] Chuyển sang format [...] cho Facebook (algorithm thay đổi)
- [ ] Khai thác gap: [chủ đề] mà đối thủ chưa làm

### Priority Nội Dung
1. [Nội dung ưu tiên 1 — lý do]
2. [Nội dung ưu tiên 2 — lý do]
3. [Nội dung ưu tiên 3 — lý do]

---
*Nguồn: Google Trends, [Platform] Newsroom, WebSearch. Cần chạy lại tháng sau.*
```

---

## Tích Hợp API (Optional)

### Ahrefs API
```
API Endpoint: https://api.ahrefs.com/v3/keywords-explorer
Method: GET
Headers: Authorization: Bearer [YOUR_API_KEY]
Params: keywords=[keyword], country=vn

Lấy: volume, keyword_difficulty, clicks_per_search
```

### SEMrush API
```
API Endpoint: https://api.semrush.com/
Params: type=phrase_organic&phrase=[keyword]&database=vn

Lấy: search_volume, cpc, competition
```

### Điền API Key
Để dùng API, thêm vào `.env` hoặc báo cho Claude khi chạy skill:
```
AHREFS_API_KEY=your_key_here
SEMRUSH_API_KEY=your_key_here
```

Nếu không có API key → dùng Google Trends + WebSearch (đủ cho content marketing cơ bản).

---

## Khi Nào Dùng Skill Này vs Skills Khác

| Nhu cầu | Dùng skill nào |
|---|---|
| Monthly intelligence update | `/market-intelligence` (skill này) |
| Deep competitor audit hàng quý | `/competitor research` |
| Tra algorithm trước khi viết bài hôm nay | `/platform algorithm` |
| Từ khóa cho bài SEO cụ thể | `/market-intelligence` → lấy từ section 1 |

---

**Agent sử dụng:** Content Planner Agent  
**Cadence:** Hàng tháng, đầu tháng  
**Tạo bởi:** Marketing Content Workspace v2  
**Ngày:** 2026-05-12
