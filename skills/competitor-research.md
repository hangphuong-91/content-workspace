# Skill: /competitor research

## Mô tả
Audit nội dung của đối thủ cạnh tranh trong một ngành. Output gồm profile từng đối thủ, bảng so sánh content strategy, gap analysis, và top 10 content ideas từ cơ hội bị bỏ ngỏ. Kết quả tự động feed vào Phase 1 của `/content plan` nếu file audit tồn tại trong `content-outputs/`.

## Cú pháp
```
/competitor research [brand/ngành]
/competitor research [brand/ngành] --competitors [tên đối thủ 1, đối thủ 2]
```

**Ví dụ:**
```
/competitor research "phòng khám sản phụ khoa tư nhân TPHCM"
/competitor research "cà phê specialty Hà Nội" --competitors "The Coffee House, Katinat, Phúc Long"
/competitor research "app fintech sinh viên" --competitors "MoMo, ZaloPay"
```

## Claude sẽ hỏi gì khi chạy
1. Tên brand của bạn (để so sánh positioning)
2. 2–5 đối thủ cần audit (nếu chưa cung cấp qua --competitors)
3. Kênh nào cần focus: social media, website/SEO, email, quảng cáo?

## Workflow — 5 bước

### Bước 1: Tìm đối thủ (nếu chưa biết)
- Search: "[ngành] nổi tiếng tại [thị trường]"
- Search: "[ngành] top [thị trường] 2024 2025"
- Chọn top 3–5 đối thủ phù hợp nhất để audit

### Bước 2: Audit từng đối thủ
Với mỗi đối thủ, WebSearch + WebFetch để thu thập:
- **Website:** Cấu trúc nội dung, blog, SEO focus
- **Facebook:** Tần suất đăng, loại content, engagement rate ước tính
- **TikTok/Instagram/YouTube:** Format ưu tiên, số view/follow
- **Quảng cáo:** Có đang chạy ads không? Angle quảng cáo là gì?

### Bước 3: So sánh Content Strategy
Bảng so sánh:

| Tiêu chí | Đối thủ A | Đối thủ B | Đối thủ C |
|---|---|---|---|
| Tần suất post/tuần | | | |
| Format chủ đạo | | | |
| Content pillar chính | | | |
| Tone of voice | | | |
| Điểm mạnh nội dung | | | |
| Điểm yếu rõ nhất | | | |
| Kênh đang đầu tư nhiều | | | |

### Bước 4: Gap Analysis
- Chủ đề nào CHƯA ai khai thác trong ngành?
- Format nào đối thủ bỏ ngỏ?
- Audience segment nào chưa được phục vụ tốt?

### Bước 5: SWOT Positioning Matrix
- **Strengths:** Đối thủ đang làm tốt gì?
- **Weaknesses:** Điểm yếu content của từng đối thủ
- **Opportunities:** Khoảng trống cho brand của bạn
- **Threats:** Xu hướng nào đối thủ đang đi trước?

## Output
1. File `competitor-audit.md` tại `content-outputs/[brand]-[YYYY-MM]/`
2. Notion: entry vào database "Competitor Intelligence"
3. Top 10 content ideas từ gap analysis (sẵn sàng dùng trong `/content plan`)

## Ví dụ Output — Case Sản Phụ Khoa
```markdown
## Đối Thủ: Phòng Khám Bác Sĩ Nguyễn Thị X
- Facebook: 45K follows, đăng 3x/tuần, chủ yếu ảnh clinic + certificate
- TikTok: 12K follows, video "hỏi bác sĩ" 5–7 phút, view 5K–50K
- Điểm mạnh: Authority cao, nhiều certificate, testimonial bệnh nhân
- Điểm yếu: Không có infographic, caption ngắn, không reply comment

## Gap Analysis — Top 3 Cơ Hội
1. Infographic theo tuần thai (không ai làm series này)
2. Video "ngày trong cuộc sống của bác sĩ sản phụ khoa" (human story)
3. Series Q&A từ câu hỏi thật của bệnh nhân (engagement rất cao ở ngành này)
```

## Lưu ý
- Chỉ audit public content — không truy cập thông tin nội bộ hoặc có bảo mật
- Số liệu engagement là ước tính từ public data, không phải số chính xác
- Chạy skill này TRƯỚC `/content plan` để research phase chất lượng hơn
- Nên cập nhật audit mỗi 2–3 tháng vì chiến lược đối thủ thay đổi
