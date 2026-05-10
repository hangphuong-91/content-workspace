# Notion Database Schema — Content Plan

## Database: "Content Plan — [Brand] — [Tháng/Năm]"

Tạo bằng MCP tool: `mcp__claude_ai_Notion__notion-create-database`

## Columns (Properties)

| Tên cột | Type | Options / Notes |
|---|---|---|
| **Title** | Title | Tên content piece |
| **Kênh** | Select | Facebook / TikTok / Instagram / LinkedIn / Blog / Email / YouTube / Ads |
| **Pillar** | Select | [Tên 3–5 pillars từ content plan] |
| **Format** | Select | Video / Infographic / Carousel / Post / Article / Email / Script / Ad |
| **Tháng** | Select | Tháng 1 / Tháng 2 / Tháng 3 |
| **Tuần** | Select | W1 / W2 / W3 / W4 / W5 / W6 / W7 / W8 / W9 / W10 / W11 / W12 |
| **Giai đoạn** | Select | Awareness / Consideration / Conversion / Retention |
| **Angle** | Text | Mô tả góc nhìn content |
| **CTA** | Text | Call to action cụ thể |
| **Status** | Select | 📋 Planned / ✍️ Draft / 👀 Review / ✅ Ready / 📤 Published / 📊 Measured |
| **AI Tool** | Select | Claude / Canva AI / DALL-E / CapCut / Manual |
| **Copywrite Done** | Checkbox | |
| **Visual Done** | Checkbox | |
| **Publish Date** | Date | Ngày dự kiến đăng |
| **Published Date** | Date | Ngày thực tế đăng |
| **Reach** | Number | Điền sau khi đăng |
| **Engagement** | Number | Tổng reactions + comments + shares |
| **ER%** | Formula | `prop("Engagement") / prop("Reach") * 100` |
| **Notes** | Text | Ghi chú thêm, link post sau khi đăng |

## Status Workflow
```
📋 Planned → ✍️ Draft (sau khi chạy /copywrite) 
→ 👀 Review (đọc lại, chỉnh sửa)
→ ✅ Ready (đã approve, chờ đăng)
→ 📤 Published (đã đăng, điền link)
→ 📊 Measured (đã điền số liệu sau 48h)
```

## Views Nên Tạo
1. **By Week** — Group by Tuần, filter tháng hiện tại → thấy queue tuần này
2. **By Status** — Group by Status → thấy toàn bộ pipeline
3. **By Channel** — Group by Kênh → thấy balance OPE
4. **Calendar view** — By Publish Date → thấy lịch đăng

## Companion Database: "Competitor Intelligence"
Tạo riêng cho output của `/competitor research`:

| Cột | Type |
|---|---|
| Brand | Title |
| Ngành | Select |
| Kênh chính | Multi-select |
| Điểm mạnh | Text |
| Điểm yếu | Text |
| Gap opportunities | Text |
| Audit date | Date |
| File audit | URL |
