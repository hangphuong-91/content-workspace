# Hướng Dẫn Cho Claude — Content Workspace

## Quy Tắc Ngôn Ngữ (BẮT BUỘC)

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
**Mục tiêu:** Tạo chiến lược nội dung 3 tháng → thực thi hàng tuần với 6 skills

---

## 6 Skills Trong Workspace

| Lệnh | Chức năng |
|---|---|
| `/competitor research` | Phân tích đối thủ, SWOT, phân tích khoảng trống (Gap Analysis) |
| `/platform algorithm` | Thuật toán (Algorithm) mới nhất từ nguồn chính thức |
| `/content plan` | Kế hoạch nội dung (Content Plan) 3 tháng, 5 giai đoạn |
| `/ai execution` | Quy trình sản xuất hàng tuần, sơ đồ tái sử dụng nội dung (Repurposing) |
| `/copywrite` | Viết bài theo từng nền tảng, 3 biến thể |
| `/visual creative` | Brief thiết kế, câu lệnh AI tạo ảnh, thông số Canva |

**Thứ tự chạy chuẩn:**
1. `/competitor research` → 2. `/platform algorithm` → 3. `/content plan` → 4. `/ai execution` → 5. `/copywrite` + `/visual creative` (song song)

---

## Quy Tắc Đầu Ra

- Tất cả file output lưu vào `outputs/[tên-thương-hiệu]-[YYYY-MM]/`
- Mỗi output có frontmatter: Tạo bởi, Trạng thái, Nền tảng, Ngày tạo
- Tuân thủ y tế: Không dùng "chữa khỏi", dùng "hỗ trợ cải thiện"
- Commit output lên GitHub sau mỗi lần chạy skill

---

## Phong Cách Viết

- **Giọng điệu:** Ấm áp nhưng chuyên nghiệp — như người đồng nghiệp giàu kinh nghiệm
- **Độ dài:** Đủ thông tin, không lòng vòng
- **Cấu trúc:** Header rõ ràng, dùng bảng khi có nhiều dữ liệu, bullet point khi liệt kê
- **Số liệu:** Dùng nghìn (K) thay vì "50,000" — viết "50 nghìn"
