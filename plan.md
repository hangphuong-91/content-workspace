# Kế Hoạch Xây Dựng — Marketing Content Workspace

**Phiên bản:** 1.0  
**Ngày tạo:** 2026-05-10  
**Trạng thái:** Hoàn thành 100%

---

## Mục Tiêu

Xây dựng một workspace Claude Code hoạt động như một content team đang vận hành, dành cho solo marketer hoặc nhóm nhỏ. Workspace gồm 6 skills kết nối với nhau, có tích hợp công cụ ngoài (Notion, Google Drive, GitHub, Canva), đầu ra có thể bàn giao và dạy lại cho người khác.

**Trường hợp thử nghiệm:** Ngành sản phụ khoa — bác sĩ tư nhân có thương hiệu cá nhân (Personal Brand) tại TPHCM.

---

## Tổng Quan 6 Skills

| Skill | Lệnh | Vai trò | Tích hợp ngoài |
|---|---|---|---|
| Kế Hoạch Nội Dung | `/content plan` | Điều phối — tạo kế hoạch nội dung (Content Plan) 3 tháng | Notion, Drive, GitHub |
| Nghiên Cứu Đối Thủ | `/competitor research` | Phân tích khoảng trống (Gap Analysis), đưa vào giai đoạn nghiên cứu | Tìm kiếm web, Notion |
| Thuật Toán Nền Tảng | `/platform algorithm` | Cập nhật thuật toán (Algorithm) mới nhất | Tìm kiếm web (tươi mỗi lần) |
| Viết Bài | `/copywrite` | Thực thi từng bài nội dung | Notion (đọc hướng dẫn giọng văn) |
| Thiết Kế Hình Ảnh | `/visual creative` | Brief thiết kế + câu lệnh AI tạo ảnh + Canva | Canva MCP, Drive |
| Thực Thi AI | `/ai execution` | Quy trình sản xuất + bảng công cụ cho nguồn lực có hạn | Notion, GitHub |

**Luồng tổng:** `/competitor research` + `/platform algorithm` → đưa vào → `/content plan` → `/ai execution` sinh quy trình → mỗi tuần chạy `/copywrite` + `/visual creative`

---

## Kiến Trúc Files & Folders

```
content-workspace/
├── CLAUDE.md                    ← Hướng dẫn cho Claude (quy tắc ngôn ngữ, ngữ cảnh)
├── plan.md                      ← File này — kế hoạch dự án
├── README.md                    ← Tổng quan cho người dùng mới
├── QUICK-REFERENCE.md           ← Cheat sheet lệnh hàng ngày
├── skills/
│   ├── content-plan.md          ← Skill điều phối, 5 giai đoạn
│   ├── competitor-research.md   ← Phân tích đối thủ
│   ├── platform-algorithm.md    ← Thuật toán (Algorithm) theo nền tảng
│   ├── copywrite.md             ← Viết bài theo nền tảng
│   ├── visual-creative.md       ← Thiết kế hình ảnh
│   ├── ai-execution.md          ← Quy trình thực thi
│   ├── content-plan/            ← Templates cho content-plan
│   ├── competitor-research/     ← Framework phân tích
│   ├── platform-algorithm/      ← Nguồn chính thức theo nền tảng
│   ├── copywrite/               ← Frameworks, thông số nền tảng, hướng dẫn giọng văn
│   ├── visual-creative/         ← Thông số thiết kế, câu lệnh AI tạo ảnh
│   └── ai-execution/            ← Bảng công cụ, mẫu quy trình
├── .claude/
│   ├── SKILLS-SETUP.md          ← Hướng dẫn cài đặt skills (3 cách)
│   └── skills-manifest.json     ← Registry đầy đủ 6 skills
├── outputs/
│   └── [thương-hiệu]-[YYYY-MM]/
│       ├── competitor-audit.md
│       ├── platform-algorithm-[nền-tảng]-[YYYY-MM].md
│       ├── content-plan.md
│       ├── ai-execution-sop.md
│       ├── copywrite-sample-[nền-tảng].md
│       └── visual-creative-sample-[loại].md
└── exports/
    └── chat-history.txt
```

---

## Chi Tiết Từng Skill

### SKILL 1: `/content plan`
**5 giai đoạn:**
1. Phân tích thực trạng — tìm kiếm ngành, đối thủ, bối cảnh
2. Nền tảng chiến lược — 2 chân dung khách hàng (Persona), mục tiêu SMART, ma trận kênh truyền thông (OPE)
3. Kiến trúc thông điệp — 5 trụ cột nội dung (Content Pillar), thông điệp theo phễu tiếp thị (Funnel)
4. Lịch nội dung (Content Calendar) 3 tháng
5. Khung đánh giá — KPI, lịch đánh giá, dấu hiệu cần tối ưu

### SKILL 2: `/competitor research`
**Quy trình:** Tìm kiếm trang web + mạng xã hội → phân tích nội dung → phân tích khoảng trống (Gap Analysis) → SWOT → top 10 ý tưởng nội dung

### SKILL 3: `/platform algorithm`
**Nền tảng hỗ trợ:** Facebook, TikTok, LinkedIn, Google, Instagram, YouTube  
**Quy tắc:** Tìm kiếm TƯƠI mỗi lần — không dùng kiến thức cũ. Date-stamp bắt buộc.

### SKILL 4: `/copywrite`
**Frameworks theo nền tảng:**
- Facebook/Instagram: Câu thu hút (Hook) → Xung đột → Giải pháp → Bằng chứng → Lời kêu gọi hành động (CTA)
- TikTok: Câu thu hút (Hook) 3 giây → Căng thẳng → Tiết lộ → Lời kêu gọi hành động (CTA)
- Email: Dòng tiêu đề + xem trước → Câu chuyện → Giá trị → Nút lời kêu gọi hành động (CTA)
- Blog: Tiêu đề SEO → Meta → Mở đầu thu hút → Cấu trúc H2 → Lời kêu gọi hành động (CTA)
- Quảng cáo: 3 biến thể (lý trí / cảm xúc / khẩn cấp) cho thử nghiệm A/B

### SKILL 5: `/visual creative`
**3 bước:** Brief thiết kế → Câu lệnh AI tạo ảnh (Midjourney/DALL-E/Canva AI) → Thông số Canva

### SKILL 6: `/ai execution`
**Đầu ra:** Quy trình hàng tuần, bảng công cụ (loại nội dung → công cụ AI → thời gian), sơ đồ tái sử dụng nội dung (Repurposing) (1 bài gốc → 7 bài phát sinh)

---

## Tích Hợp Ngoài

| Nền tảng | Công cụ | Dùng bởi skill nào | Chức năng |
|---|---|---|---|
| **Notion** | MCP | Kế hoạch nội dung, Viết bài, Thực thi | Theo dõi nội dung, hướng dẫn giọng văn |
| **Google Drive** | MCP | Kế hoạch nội dung, Thiết kế hình ảnh | Lưu file, export Canva |
| **GitHub** | gh CLI | Kế hoạch nội dung, Thực thi | Quản lý phiên bản, lưu output |
| **Canva** | MCP | Thiết kế hình ảnh | Tạo thiết kế, lấy bộ nhận diện thương hiệu |
| **Tìm kiếm web** | Built-in | Nghiên cứu đối thủ, Thuật toán | Nghiên cứu, cập nhật thuật toán |

---

## Quy Tắc Ngôn Ngữ (Xem CLAUDE.md để biết đầy đủ)

Thuật ngữ chuyên ngành: **tiếng Việt (tiếng Anh)** — ví dụ: Tỷ lệ tương tác (Engagement Rate)  
Giữ nguyên: tên nền tảng, tên công cụ, tính năng chính thức (Reels, Stories)

---

## Trường Hợp Thử Nghiệm — Bác Sĩ Sản Phụ Khoa

**Chạy theo thứ tự:**
```
/competitor research "phòng khám sản phụ khoa tư nhân TPHCM"
/platform algorithm facebook
/platform algorithm tiktok
/content plan "Thương hiệu cá nhân bác sĩ sản phụ khoa tư nhân"
/ai execution outputs/bacsi-sanphukhoa-2026-05/content-plan.md
/copywrite facebook "Bài giáo dục sức khỏe thai kỳ tuần 28"
/visual creative "Ảnh thông tin (Infographic) thai kỳ tuần 28 cho Facebook"
```

**Đầu ra mẫu:** `outputs/bacsi-sanphukhoa-2026-05/` — 6 files hoàn chỉnh

---

## Danh Sách Kiểm Tra Hoàn Thành

### Skill Files
- [x] `skills/content-plan.md` — 5 giai đoạn, phương pháp SUME
- [x] `skills/competitor-research.md` — Phân tích khoảng trống (Gap Analysis), SWOT
- [x] `skills/platform-algorithm.md` — Nguồn chính thức, date-stamp
- [x] `skills/copywrite.md` — Frameworks nền tảng, 24 thiên kiến nhận thức
- [x] `skills/visual-creative.md` — Brief thiết kế, câu lệnh AI tạo ảnh
- [x] `skills/ai-execution.md` — Quy trình, bảng công cụ, sơ đồ tái sử dụng

### Supporting Files
- [x] Brand voice template (hướng dẫn giọng văn thương hiệu)
- [x] Platform specs (thông số nền tảng)
- [x] AI prompt templates (câu lệnh tạo ảnh mẫu)
- [x] Repurposing matrix (ma trận tái sử dụng)

### Documentation
- [x] README.md — Tổng quan cho người dùng mới
- [x] QUICK-REFERENCE.md — Cheat sheet hàng ngày
- [x] CLAUDE.md — Hướng dẫn cho Claude (quy tắc ngôn ngữ)
- [x] plan.md — File này
- [x] SKILLS-SETUP.md — Hướng dẫn cài đặt

### Output Mẫu
- [x] `competitor-audit.md` — Phân tích đối thủ hoàn chỉnh
- [x] `platform-algorithm-facebook-2026-05.md` — Thuật toán (Algorithm) Facebook
- [x] `content-plan.md` — Kế hoạch nội dung (Content Plan) 3 tháng
- [x] `ai-execution-sop.md` — Quy trình sản xuất hàng tuần
- [x] `copywrite-sample-facebook.md` — 3 biến thể bài viết sẵn sàng đăng
- [x] `visual-creative-sample-infographic.md` — Brief thiết kế ảnh thông tin (Infographic)

### GitHub
- [x] Repository: https://github.com/hangphuong-91/content-workspace
- [x] Tất cả commits với message rõ ràng
- [x] Output files được push lên repo

---

**Hoàn thành:** 2026-05-10  
**Phiên bản tiếp theo:** Thêm TikTok algorithm output, LinkedIn content plan, email nurture sequence
