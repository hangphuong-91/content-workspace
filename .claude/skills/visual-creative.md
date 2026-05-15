---
name: visual-creative
description: Tạo visual cho content — Creative Brief + AI Image Prompts cho Midjourney/DALL-E/Canva AI + design thực tế trên Canva qua MCP + export lên Google Drive.
---

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

## Workflow — 4 Bước (+ MeiGen AI Design MCP)

### Bước 0 (NEW): MeiGen AI Design Research
**Khi nào:** Trước khi viết creative brief, research template + design patterns từ MeiGen

**Dùng MeiGen MCP để:**
- `search-design-templates` — Tìm template theo keyword (VD: "infographic medical", "social media post healthcare")
- `get-template-details` — Xem chi tiết design mẫu (layout, colors, typography, elements)
- `analyze-design-patterns` — Phân tích design trends cho ngành (VD: "healthcare", "personal brand", "education")
- `generate-design-description` — Tạo detailed description từ template

**Process:**
```
1. User cung cấp: Content theme + platform + brand style
2. Claude chạy: /search-design-templates [theme] [industry]
3. MeiGen trả về: Top 5-10 template phù hợp
4. Claude phân tích: Layout, color palette, typography, composition
5. Output: Design reference + insights để viết creative brief tốt hơn
```

**Example:**
```
User: "Infographic thai kỳ tuần 28 cho Facebook"

Claude search MeiGen:
  → search-design-templates("medical infographic", "healthcare", "facebook-post")
  → Kết quả: 8 templates
  → get-template-details(template_id_1, template_id_2)
  → analyze-design-patterns("healthcare infographic", "2026")

Output:
- 3 design patterns phổ biến (kiểu layout, color scheme)
- Typography recommendations (font hierarchy)
- Element composition (icons, images, text ratios)
- Trending color palettes cho healthcare content
```

### Bước 1: Creative Brief (Improved by MeiGen Research)
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

**Design References từ MeiGen:**
- Template inspiration: [Link hoặc description từ MeiGen research]
- Composition style: [Ví dụ: "Hero image left + text right" hoặc "Full-bleed infographic"]
- Color palette: [Color codes từ MeiGen templates]
- Typography style: [Font recommendation từ MeiGen analysis]

**Dos:** 
- Follow MeiGen pattern nếu trending [+20% engagement]
- Sử dụng color psychology từ design analysis
- Bao gồm CTA element (MeiGen suggest phổ biến nhất)

**Don'ts:** 
- Tránh hình ảnh bệnh viện lạnh lẽo / tránh stock photo quá generic (MeiGen flagged as low-engagement)
- Không dùng deprecated design patterns (từ MeiGen trending analysis)
```

### Bước 2: AI Image Prompts (Enhanced with MeiGen Data)
**Midjourney** (cho ảnh người/cảnh thật):
```
[Subject description], [style: photorealistic/illustration], [lighting], 
[color palette], [composition], [platform specs], --ar [ratio] --v 6
```

**DALL-E 3** (cho infographic/graphic) — Enhanced by MeiGen:
```
[Style: từ MeiGen trending analysis], [color scheme: từ MeiGen palette],
[elements: icons/charts/images từ MeiGen composition],
[text placeholder areas], [mood], square/portrait/landscape format

Example:
"Flat design infographic style (MeiGen trending), healthcare blue + mint green palette,
medical icons (stethoscope, heartbeat) + 3 data visualization elements arranged left-to-right,
mint green CTA button bottom right, clean sans-serif typography, emotional + professional mood"
```

**Canva AI Text-to-Image** (nhanh nhất, tích hợp sẵn) — Enhanced by MeiGen:
```
[MeiGen template style description] + [brand-specific customization]

Example:
"Modern medical infographic template style: healthcare theme, professional color palette 
(blue + mint + white), contains medical icons and data viz elements, clean layout, 
suitable for Facebook post with CTA button"
```

**MeiGen AI Design Direct** (NEW — tối ưu nhất):
```
Sử dụng MeiGen templates trực tiếp với custom overlay:
1. Chọn template từ search results
2. Customize: Text, colors, images
3. Export thẳng PNG/JPG
4. Tiết kiệm 30-40% thời gian vs viết prompt từ 0
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

## Tích Hợp MeiGen AI Design MCP

### Setup (Một lần)
1. **Clone MeiGen MCP repository:**
   ```bash
   git clone https://github.com/jau123/MeiGen-AI-Design-MCP
   cd MeiGen-AI-Design-MCP
   npm install
   ```

2. **Register MCP trong Claude Code:**
   - Thêm vào `.claude/settings.json`:
   ```json
   {
     "mcps": {
       "meigen": {
         "command": "node",
         "args": ["path/to/MeiGen-AI-Design-MCP/index.js"]
       }
     }
   }
   ```

3. **Test connection:**
   - Claude sẽ tự động detect MCP
   - First prompt sẽ hỏi "Enable MeiGen MCP?"

### Available MeiGen Functions
```
• search-design-templates(keyword, industry, format)
  → Trả về: list templates với thumbnail + metadata
  
• get-template-details(template_id)
  → Trả về: Layout structure, colors (hex), typography, dimensions
  
• analyze-design-patterns(industry, year)
  → Trả về: Trending patterns, color trends, composition styles
  
• generate-design-description(template_id)
  → Trả về: Detailed text description của template (dùng cho AI prompts)
  
• get-color-palette(industry, mood)
  → Trả về: Color codes + psychology + usage guidelines
  
• get-typography-recommendations(industry, mood)
  → Trả về: Font pairs + sizing + hierarchy recommendations
```

### Fallback (Nếu MeiGen không available)
- Dùng Canva brand kit + manual prompt engineering
- Dùng reference images từ Behance/Pinterest (manual curation)
- Vẫn generate AI prompts, nhưng chất lượng 20-30% thấp hơn

---

## Output
- `visual-brief-[topic].md` — Creative brief đầy đủ (+ MeiGen insights nếu có)
- `ai-prompts-[topic].md` — Prompts sẵn dùng (optimized by MeiGen templates)
- `meigen-research-[topic].md` — MeiGen research result (templates + analysis) [NEW]
- Link Canva design thực tế (hoặc MeiGen template link nếu dùng trực tiếp)
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
