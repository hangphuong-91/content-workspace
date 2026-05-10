# Skill: /visual creative

## Mô tả
Tạo visual cho content theo 3 bước: (1) Creative Brief, (2) AI Image Prompts sẵn dùng cho Midjourney/DALL-E/Canva AI, (3) Tự động tạo design thực tế trên Canva qua MCP. Output gồm brief .md + prompts + link Canva design + export lên Google Drive.

## Cú pháp
```
/visual creative [mô tả nội dung + platform]
```

**Ví dụ:**
```
/visual creative "Infographic thai kỳ tuần 28 cho Facebook post, brand màu xanh mint"
/visual creative "TikTok thumbnail bác sĩ trả lời Q&A, cần có text hook to rõ"
/visual creative "LinkedIn banner cho personal brand bác sĩ, professional, tông xanh navy"
/visual creative "Email header ảnh mùa hè chăm sóc sức khỏe, warm tone"
```

## Claude sẽ hỏi gì khi chạy
1. Brand colors và fonts? (hoặc Claude đọc từ Canva brand kit nếu có)
2. Mood: educational / inspirational / promotional / storytelling / trust-building
3. Có ảnh thật của brand/người không? (để tránh generate khuôn mặt sai)
4. Text overlay cần ghi gì? (title, subtitle, CTA)

## Workflow — 3 Bước

### Bước 1: Creative Brief
```markdown
## Creative Brief: [Tên content piece]

**Platform & Dimensions:** [Facebook Post: 1200×628px / TikTok: 1080×1920px / ...]
**Mood board:** [3 từ mô tả cảm xúc visual: ví dụ "Ấm áp, Tin cậy, Chuyên nghiệp"]

**Visual concept:**
- Kiểu ảnh: Photography / Illustration / Infographic / Text-dominant
- Composition: [Subject bên trái/phải, full bleed, split layout...]
- Màu chủ đạo: [Brand colors + accent]
- Ánh sáng: Natural / Studio / Soft / Dramatic

**Text overlay:**
- Headline: [...]
- Subtext: [...]
- CTA: [...]

**Dos:** [...]
**Don'ts:** [Tránh hình ảnh bệnh viện lạnh lẽo / tránh stock photo quá generic...]
```

### Bước 2: AI Image Prompts
**Midjourney** (cho ảnh người/cảnh thật):
```
[Subject description], [style: photorealistic/illustration], [lighting], 
[color palette], [composition], [platform specs], --ar [ratio] --v 6
```

**DALL-E 3** (cho infographic/graphic):
```
[Style: flat design/minimal], [color scheme], [elements to include],
[text placeholder areas], [mood], square/portrait/landscape format
```

**Canva AI Text-to-Image** (nhanh nhất, tích hợp sẵn):
```
[Brief prompt phù hợp Canva AI style]
```

### Bước 3: Tạo Design trên Canva (MCP)
Claude sẽ tự động:
1. `list-brand-kits` — lấy màu sắc và font của brand
2. `generate-design-structured` — tạo design theo brief
3. Xem lại design qua `get-design-content`
4. `export-design` — export PNG/PDF
5. Upload lên Google Drive qua MCP

## Platform Specs (dimensions)

| Platform | Format | Kích thước | Lưu ý |
|---|---|---|---|
| Facebook Post | Landscape | 1200×628px | |
| Facebook Post | Square | 1080×1080px | |
| Facebook Story / Reels | Portrait | 1080×1920px | Safe zone: tránh 250px trên/dưới |
| Instagram Post | Square | 1080×1080px | |
| Instagram Reels thumbnail | Portrait | 1080×1920px | |
| TikTok | Portrait | 1080×1920px | Text safe zone: 150px trên/dưới |
| LinkedIn Post | Landscape | 1200×627px | |
| LinkedIn Banner | Wide | 1584×396px | |
| YouTube Thumbnail | Landscape | 1280×720px | Text to trên 60% diện tích |
| Email Header | Wide | 600×200px | |

## Output
- `visual-brief-[topic].md` — Creative brief đầy đủ
- `ai-prompts-[topic].md` — Prompts sẵn dùng
- Link Canva design thực tế
- File export trong Google Drive folder "Visual Assets"

## Ví dụ Output — Infographic Thai Kỳ
```markdown
## Creative Brief: Infographic Thai Kỳ Tuần 28

**Platform:** Facebook Post (1080×1080px)
**Mood:** Ấm áp, Giáo dục, Tin cậy

**Concept:** Infographic dạng timeline/journey — bên trái là hình minh họa bé 28 tuần,
bên phải là 3 điểm phát triển chính của bé. Màu nền pastel xanh mint (#E8F5F0),
text xanh navy (#1B3A4B), accent hồng nhạt (#FFD6E0).

**Text overlay:**
- Headline to: "Bé 28 Tuần Tuổi"
- Sub: "3 điều đang xảy ra trong bụng bạn"
- Footer: [Tên bác sĩ] • [Số điện thoại phòng khám]

**Midjourney prompt:**
cute illustrated baby at 28 weeks gestation, medical infographic style,
pastel mint and navy color palette, soft warm lighting, educational poster,
flat design with subtle gradients --ar 1:1 --v 6
```

## Bước Tiếp Theo Sau Khi Có Visual
- Upload design lên Notion content database, update status thành "Ready to Post"
- Nếu cần copy đi kèm: `/copywrite [platform] [brief]` với cùng angle và tone
- Nếu cần nhiều visual cho 1 series: dùng cùng Canva template, chỉ đổi content từng slide

## Lưu ý
- **Ngành y tế:** Không dùng ảnh bệnh nhân thật chưa được đồng ý. Tránh hình ảnh máu hoặc phẫu thuật. Hình minh họa và animation an toàn hơn ảnh thật.
- **Khuôn mặt:** AI thường generate khuôn mặt không thực tế. Nếu cần ảnh người thật, dùng ảnh thật của bác sĩ, chỉ dùng AI cho background và element.
- **Brand consistency:** Luôn dùng cùng màu sắc, font, logo placement. Canva brand kit giúp tự động hóa điều này.
- **Export resolution:** Luôn export PNG cho social, PDF cho print.
- **Ngôn ngữ output:** Không dùng dấu gạch ngang dài trong creative brief tiếng Việt.
