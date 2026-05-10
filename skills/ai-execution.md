# Skill: /ai execution

## Mô tả
Biến content plan 3 tháng thành SOP vận hành thực tế cho 1 người (solo marketer). Phân tích từng content piece → assign AI tool phù hợp → tính thời gian → tạo repurposing tree → sinh weekly production queue. Output đủ rõ để hand-off cho người không biết Claude Code.

## Cú pháp
```
/ai execution [đường dẫn file content-plan.md]
/ai execution  ← tự động dùng file mới nhất trong content-outputs/
```

**Ví dụ:**
```
/ai execution content-outputs/bacsi-sanphukhoa-2026-05/content-plan.md
/ai execution
```

## Claude sẽ hỏi gì khi chạy
1. Nguồn lực thực tế: Mỗi tuần có bao nhiêu giờ làm content? (VD: 5h/tuần)
2. Có ngân sách cho AI tools trả phí không? (ảnh hưởng đến tool được recommend)
3. Ai sẽ dùng SOP này: chỉ bạn hay hand-off cho người khác?
4. Kênh nào là ưu tiên số 1 tháng này?

## Output — 4 Documents

### Document 1: AI Tool Matrix
Bảng đầy đủ cho mỗi content piece:

| # | Content Piece | Kênh | AI Tool | Prompt Template | Thời gian | Review |
|---|---|---|---|---|---|---|
| 1 | Infographic tuần 28 | Facebook | Canva AI + `/visual creative` | visual-prompt-01 | 20 phút | Self-review |
| 2 | TikTok Q&A script | TikTok | `/copywrite tiktok` | tiktok-framework | 15 phút | Đọc to trước quay |
| 3 | Blog thai kỳ tháng 7 | Website | `/copywrite blog` + Grammarly | blog-seo-framework | 45 phút | Keyword check |

**AI Tools được recommend (free → trả phí):**

| Tool | Dùng cho | Free? |
|---|---|---|
| Claude (`/copywrite`) | Tất cả text content | Có (trong Claude Code) |
| Canva AI (`/visual creative`) | Social graphics, infographic | Freemium |
| DALL-E 3 (via ChatGPT) | Custom illustration | $20/tháng |
| CapCut AI | Video edit, subtitle tự động | Có |
| Midjourney | Photography-style image | $10/tháng |
| Mailchimp | Email scheduling + AI subject line | Freemium |
| Buffer / Meta Business Suite | Social scheduling | Freemium |

### Document 2: Weekly Production Queue
Priority queue cho 4 tuần đầu:

```markdown
## Tuần 1 — [Ngày bắt đầu]
Thời gian dự kiến: [X] giờ

| Thứ tự | Content piece | Tool | Thời gian | Deadline đăng |
|---|---|---|---|---|
| 1 (ưu tiên) | ... | ... | ... | Thứ 3 |
| 2 | ... | ... | ... | Thứ 5 |
| 3 | ... | ... | ... | Thứ 6 |

**Ghi chú tuần này:** [Sự kiện đặc biệt / deadline quan trọng]
```

### Document 3: Repurposing Tree
1 pillar content → tất cả derivative pieces:

```
📄 BLOG PILLAR: "7 điều cần biết về thai kỳ tuần 28"
├── 📱 Facebook Post (3 posts — mỗi post 1 điểm nổi bật)
├── 💼 LinkedIn Article (professional angle: tư vấn bác sĩ)
├── 🎵 TikTok (5 videos ngắn — mỗi video 1 tip)
├── 📧 Email Newsletter (tóm tắt + link blog full)
├── 🖼️ Instagram Carousel (7 slides = 7 điểm)
└── 📌 Pinterest Infographic (visual summary)

⏱️ Tổng thời gian: ~3 giờ thay vì 8 giờ nếu làm riêng lẻ
💰 Tiết kiệm: 5 giờ/pillar × 4 pillars/tháng = 20 giờ/tháng
```

### Document 4: Weekly SOP (Standard Operating Procedure)
Quy trình mỗi tuần cho 1 người vận hành:

```markdown
## SOP: Quy Trình Sản Xuất Content Tuần [X]

### Thứ 2 — Planning (30 phút)
- [ ] Mở Weekly Production Queue
- [ ] Confirm nội dung đăng tuần này (check calendar + sự kiện)
- [ ] Check `/platform algorithm facebook` nếu reach tuần trước thấp

### Thứ 3 — Production Text (2 giờ)
- [ ] Chạy `/copywrite` cho [X] pieces theo queue
- [ ] Review và chỉnh sửa — luôn đọc to trước khi approve
- [ ] Lưu vào Notion với status "Draft"

### Thứ 4 — Production Visual (1.5 giờ)
- [ ] Chạy `/visual creative` cho các pieces cần ảnh/design
- [ ] Export từ Canva, upload Google Drive
- [ ] Ghép caption + visual, lưu Notion status → "Ready to Post"

### Thứ 5–6 — Schedule & Publish
- [ ] Schedule trên Meta Business Suite / Buffer
- [ ] Đăng TikTok thủ công (TikTok không schedule được với free account)

### Cuối tuần — Review 15 phút
- [ ] Check số: reach, engagement, click
- [ ] Note bất thường vào Notion tracking
- [ ] Prep brief cho tuần sau
```

## Lưu ý
- **Quy tắc 80/20:** 20% content tạo ra 80% kết quả. Dùng repurposing tree để tối đa hóa 1 pillar tốt thay vì tạo nhiều content mới.
- **Batch production:** Viết tất cả caption 1 lần/tuần thay vì mỗi ngày → tiết kiệm 60% thời gian chuyển context
- **Buffer 20%:** Luôn có 2–3 content pieces "dự phòng" sẵn để đăng nếu tuần đó bận
- **SOP này cho người mới:** Người không biết Claude Code có thể follow SOP bằng cách dùng AI tools thủ công theo hướng dẫn trong từng bước
