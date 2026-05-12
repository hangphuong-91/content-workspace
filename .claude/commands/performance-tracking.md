# Skill: Theo Dõi Hiệu Suất — Performance Tracking

**Lệnh:** `/performance-tracking [brand] [tuần/tháng]`

**Chức năng:** Thu thập metrics thực tế → so sánh KPI đã plan → CMO-level recommendations + cập nhật Google Sheets

**Vai trò trong hệ thống:** Đây là "mắt của CMO" — đánh giá cả kết quả lẫn chất lượng thực thi

**Chạy khi nào:**
- **Hàng tuần (quick):** Thứ 2 đầu tuần — review tuần vừa rồi, 10 phút
- **Hàng tháng (deep):** Cuối tháng — báo cáo đầy đủ, 30 phút

---

## Inputs Cần Chuẩn Bị

Trước khi chạy, cần có:
- Metrics từ **Buffer Analytics** hoặc **Meta Business Suite** (Reach, Engagement từng bài)
- File `content-plan.md` của brand (để đọc KPI đã planned)
- File `weekly-summary-[tuần].md` từ `/weekly-report` (nếu có)

---

## Quy Trình Chạy

### Phase 1 — Thu Thập & So Sánh KPI (5 phút)

**Bước 1: Đọc KPI planned từ content plan**
```
Đọc: outputs/[brand]-[YYYY-MM]/content-plan.md
Tìm: Phần "Tracking Framework" → KPIs per channel
```

**Bước 2: Nhập metrics thực tế**
Claude hỏi user điền vào bảng:
```
| Kênh | Bài đăng | Reach | Engagement | ER% | Comments | Shares |
|---|---|---|---|---|---|---|
| Facebook | [Tên bài] | [số] | [số] | [%] | [số] | [số] |
```

**Bước 3: So sánh Actual vs Planned**
- Kênh nào đang on-track / overperform / underperform?
- Pillar nào hoạt động tốt nhất?
- Format nào (Video/Image/Text) có ER% cao nhất?

---

### Phase 2 — CMO Quality Check (5 phút)

Đây là phần phân biệt skill này với báo cáo số liệu thông thường.

**Đánh giá chất lượng thực thi của Execution Agent:**

| Tiêu chí | Câu hỏi | Thang điểm |
|---|---|---|
| **Đúng brand voice?** | Giọng văn có nhất quán? | 1–5 |
| **Đúng format?** | Đúng format platform không? | 1–5 |
| **Hook đủ mạnh?** | 3 giây đầu có giữ được người đọc? | 1–5 |
| **CTA rõ ràng?** | Người đọc biết làm gì tiếp theo? | 1–5 |
| **Đúng pillar?** | Bài có thuộc đúng content pillar? | 1–5 |
| **Đúng tần suất?** | Đăng đủ số lần theo plan không? | Có/Không |

**Đánh giá market intelligence:**
- Có tận dụng trending topics tháng này không?
- Algorithm hiện tại đang reward format gì → bài có dùng format đó không?

---

### Phase 3 — Recommendations (5 phút)

**Phân tích nguyên nhân underperform:**
```
Reach thấp → Algorithm? Timing? Format?
ER% thấp  → Hook yếu? CTA mờ? Topic không resonate?
Comments ít → Không kêu gọi tương tác? Topic không tranh luận được?
```

**3–5 Action Items cụ thể:**
Không viết "cần cải thiện engagement" — viết cụ thể:
- ❌ "Cần cải thiện engagement Facebook"
- ✅ "Facebook: Thêm câu hỏi cuối bài để kích thích comment. Thử nghiệm (A/B test) với 2 bài tuần sau"

---

## Output

### Quick Report (Hàng Tuần)
**Lưu tại:** `outputs/[brand]-[YYYY-MM]/performance-weekly-W[X].md`

```markdown
# Báo Cáo Hiệu Suất Tuần [X] — [Brand]

**Kỳ:** [Ngày - Ngày]
**Người đánh giá:** Content Planner Agent
**Tổng bài đăng:** [X] bài / [X] kênh

## Tổng Quan Nhanh
| Kênh | Bài | Reach TB | ER% TB | vs KPI |
|---|---|---|---|---|
| Facebook | [X] | [số] | [%] | ✅/⚠️/❌ |
| TikTok | [X] | [số] | [%] | ✅/⚠️/❌ |

## Bài Hoạt Động Tốt Nhất
[Tên bài] — [Kênh] — [Reach] reach — [ER%] ER%
→ Tại sao hiệu quả: [phân tích ngắn]

## Bài Hoạt Động Kém Nhất
[Tên bài] — [Kênh] — [Reach] reach — [ER%] ER%
→ Nguyên nhân: [phân tích ngắn]
→ Fix tuần sau: [action cụ thể]

## Chất Lượng Thực Thi
Brand voice: [X/5] | Format: [X/5] | Hook: [X/5] | CTA: [X/5]
Nhận xét: [1–2 câu]

## 3 Action Items Tuần Sau
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

### Deep Report (Hàng Tháng)
**Lưu tại:** `outputs/[brand]-[YYYY-MM]/performance-monthly-[YYYY-MM].md`

Thêm các sections:
- Bảng KPI đầy đủ (Actual vs Planned vs Benchmark ngành)
- Phân tích theo Pillar (pillar nào mạnh/yếu)
- Phân tích theo Phễu tiếp thị (Funnel) (Awareness vs Consideration vs Conversion)
- Top 3 insight chiến lược tháng này
- Điều chỉnh kế hoạch tháng tới (cụ thể)

---

## Google Sheets Update

**Link sheet:** https://docs.google.com/spreadsheets/d/1yHqda0EOtWidPyHAwqhsacmL0iyk97jrDTpbo6W3SU0/

Skill này tạo **Google Apps Script** để update 2 tabs:

### Tab "Performance" — Từng Bài
```javascript
// Script mẫu — Claude tạo script đầy đủ khi chạy skill
function updatePerformance() {
  var sheet = SpreadsheetApp.openById('1yHqda0EOtWidPyHAwqhsacmL0iyk97jrDTpbo6W3SU0')
                            .getSheetByName('Performance');
  // Thêm row mới với data từ báo cáo
  sheet.appendRow([date, brand, channel, title, reach, engagement, er_percent, comments, shares]);
}
```

### Tab "Monthly KPI" — Actual vs Planned
```javascript
function updateMonthlyKPI() {
  var sheet = SpreadsheetApp.openById('...')
                            .getSheetByName('Monthly KPI');
  // Update cells trong tháng hiện tại
  // Tự tô màu đỏ nếu < 80% KPI, xanh nếu ≥ 100%
}
```

**Cách dùng Apps Script:**
```
1. Claude chạy skill → tạo file google-apps-script.js trong outputs/
2. Bạn vào Google Sheet → Extensions → Apps Script
3. Paste code từ file .js vào editor
4. Click "Run" → Sheet tự động cập nhật
5. Set trigger: chạy tự động mỗi tuần nếu muốn
```

---

## Tiêu Chuẩn Đánh Giá (Benchmark)

Dùng để so sánh khi không có benchmark ngành cụ thể:

| Kênh | ER% Tốt | ER% Trung bình | ER% Cần cải thiện |
|---|---|---|---|
| Facebook Page | > 3% | 1–3% | < 1% |
| Instagram | > 3% | 1–3% | < 1% |
| TikTok | > 5% | 2–5% | < 2% |
| LinkedIn | > 2% | 0.5–2% | < 0.5% |
| Blog | > 2 phút/trang | 1–2 phút | < 1 phút |
| Email | Open rate > 25% | 15–25% | < 15% |

*Nguồn: Benchmark trung bình ngành 2025–2026. Điều chỉnh theo ngành cụ thể.*

---

**Agent sử dụng:** Content Planner Agent  
**Cadence:** Hàng tuần (quick) + Hàng tháng (deep)  
**Tạo bởi:** Marketing Content Workspace v2  
**Ngày:** 2026-05-12
