# Skill: /content plan

## Mô tả
Tạo content plan 3 tháng đầy đủ cho bất kỳ chủ đề/brand nào. Output bao gồm: Situation Analysis, Audience Personas, Channel Strategy, Content Calendar (OPE), và Tracking Framework. Kết nối Notion + Google Drive + GitHub.

Chạy TRƯỚC khi dùng skill này: `/competitor research` và `/platform algorithm` để research phase đầy đủ hơn.

## Cú pháp
```
/content plan [chủ đề hoặc brand]
```

**Ví dụ:**
```
/content plan "Personal brand bác sĩ sản phụ khoa tư nhân"
/content plan "Thương hiệu cà phê specialty Hà Nội"
/content plan "App fintech cho sinh viên"
```

## Claude sẽ hỏi gì khi chạy
1. Tên brand + website + social handles
2. File marketing plan / comm plan hiện có không? (cung cấp path nếu có)
3. Ngành cụ thể (để kiểm tra compliance nếu cần: y tế, tài chính, trẻ em...)
4. Đã chạy `/competitor research` chưa? Nếu có, file audit ở đâu?

## Workflow — 5 Phases

### PHASE 1: Situation Analysis
**Claude sẽ:**
- Search 3 nhóm song song: (1) website/forum liên quan ngành + topic, (2) nội dung đối thủ đang làm, (3) tối đa 3 nguồn marketing uy tín
- Đọc file marketing plan nếu được cung cấp
- Ghi compliance notes nếu ngành cần (y tế → không claim chữa khỏi; tài chính → không cam kết lợi nhuận)

**Nguồn marketing được phép dùng** (chọn tối đa 3 phù hợp topic):
- HubSpot Blog — marketing strategy, email, inbound
- Content Marketing Institute — content strategy framework
- Think with Google — consumer insight, data
- Brands Vietnam (brandsvietnam.com) — thị trường Việt Nam
- Marketing AI (marketingai.vn) — case study trong nước

### PHASE 2: Strategic Foundation
- **2 Audience Personas:** demographics, pain points, hành vi tiêu thụ content, platform ưa dùng
- **SMART Objectives:** derived từ comm plan hoặc thảo luận với user
- **OPE Channel Matrix:**

| Kênh | Loại | Vai trò | Tần suất | Content Mix |
|---|---|---|---|---|
| Facebook Page | Owned | ... | ... | X% edu / Y% promo |
| TikTok | Owned | ... | ... | ... |
| Facebook Ads | Paid | ... | ... | ... |
| PR / UGC | Earned | ... | ... | ... |

### PHASE 3: Messaging Architecture
- **3–5 Content Pillars** hỗ trợ brand narrative
- **Core message theo funnel:** Awareness / Consideration / Conversion / Retention
- **Angle + format per kênh** (VD: Blog = deep-dive; TikTok = story hook 3s; Email = nurture)
- **Tone of voice** (đặc biệt quan trọng với personal brand)
- **Compliance notes** nếu ngành cần

### PHASE 4: Content Calendar (3 Tháng)
Output dạng bảng:

| Tuần | Tháng | Giai đoạn | Kênh | Pillar | Format | Angle | CTA | Responsible | Status |
|---|---|---|---|---|---|---|---|---|---|

- **Tháng 1:** Awareness / Setup baseline
- **Tháng 2:** Engagement / Execute & measure
- **Tháng 3:** Conversion / Optimize based on data

### PHASE 5: Tracking & Optimization Framework
- KPIs per kênh + benchmark ngành
- Baseline hiện tại (nếu brand đã có số liệu)
- Review cadence: Weekly check-in + Monthly deep review
- Optimization trigger: "Nếu [metric] < [X]% → làm [action cụ thể]"
- Template báo cáo tháng

## Output
1. Hiển thị trong chat (summary + highlights)
2. File `.md` lưu tại: `content-outputs/[brand-topic]-[YYYY-MM]/content-plan.md`
3. Notion database: 1 row per content piece với cột Status
4. Google Drive: upload file .md
5. GitHub: commit vào repo `content-workspace`

## Ví dụ Output — Case Sản Phụ Khoa
```markdown
## Audience Persona 1: Mẹ Bầu Lần Đầu
- Tuổi: 25–32, đang mang thai tháng 4–8
- Pain point: Lo lắng về sức khỏe, cần bác sĩ tin cậy, sợ thông tin sai
- Platform: Facebook (7h–9h sáng, 9h–11h tối), TikTok (giờ nghỉ trưa)
- Content trigger: Video "hỏi bác sĩ", infographic thai kỳ theo tuần

## Content Pillar 1: Giáo Dục Sức Khỏe Thai Kỳ
- Format: Infographic theo tuần thai / Video Q&A ngắn
- Angle: "Điều bạn chưa biết về tuần thai thứ [X]"
- Compliance: Không claim "chữa khỏi", không dùng "100%", có disclaimer
```

## Quy Tắc Hard Stop
Skill phải deliver output hoàn chỉnh sau 5 phases, không kéo dài thêm lượt hỏi. Nếu thiếu thông tin ở phase nào, Claude ghi "Chưa có dữ liệu, sẽ điền sau" và tiếp tục. Mục tiêu là bạn có output làm việc được ngay, không phải perfect plan trên lý thuyết.

## Transparency — Skill Thông Báo Trước Khi Làm
Ở mỗi phase, Claude sẽ nói ngắn: "Phase [X]: Mình sẽ [làm gì] vì [lý do]." Ví dụ: "Phase 2: Mình xây OPE matrix trước audience vì channel strategy phụ thuộc vào nguồn lực thực tế, không phải ngược lại."

## Phân Tích Sâu Hơn (SUME Methods tích hợp)
Sau khi có content plan, có thể chạy thêm:

**Lọc insight chiến lược:** Từ situation analysis, rút ra 5 insights quan trọng nhất và meta-pattern xuyên suốt. Dùng khi content plan quá rộng, cần ưu tiên.

**Tìm đòn bẩy:** Trong 3 tháng plan, xác định 3 content pieces có effort nhỏ nhưng tác động lớn nhất. Dùng khi nguồn lực hạn chế, cần focus.

**Kiểm tra độ vững:** Devil's advocate mode, tìm 3-5 lỗ hổng trong channel strategy hoặc messaging. Dùng trước khi present plan cho stakeholder.

## Bước Tiếp Theo Sau Khi Có Content Plan
1. Chạy ngay: `/ai execution [path-to-plan]` để nhận SOP + tool matrix tuần đầu
2. Nếu chưa có competitor research: `/competitor research [brand/ngành]`
3. Verify thuật toán kênh chính: `/platform algorithm [platform]`
4. Tạo content đầu tiên: `/copywrite [platform] [brief từ plan]`

## Lưu ý
- **Ngành y tế:** Tuân thủ Nghị định 38/2021/NĐ-CP về quảng cáo y tế. Không sử dụng hình ảnh bệnh nhân chưa được đồng ý. Không cam kết kết quả điều trị.
- **Personal brand:** Tone phải cá nhân, ấm áp, không viết như press release công ty
- **Kết quả tốt nhất:** Chạy `/competitor research` và `/platform algorithm` trước, cung cấp file comm plan nếu có
- **Ngôn ngữ output:** Không dùng dấu gạch ngang dài trong output tiếng Việt. Dùng dấu phẩy, dấu chấm, xuống dòng.
