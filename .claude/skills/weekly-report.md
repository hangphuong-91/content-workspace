# Skill: Báo Cáo Tuần — Weekly Report

**Lệnh:** `/weekly-report [brand] [tuần]`

**Chức năng:** Tổng hợp tuần sản xuất → cập nhật Notion → tạo Apps Script update Google Sheets → handoff cho Planner review

**Vai trò:** Cầu nối giữa Execution Agent (đã làm gì) và Planner Agent (kết quả thế nào)

**Chạy khi nào:** Cuối tuần (Thứ 6 hoặc Chủ Nhật) sau khi bài đã được đăng

---

## Inputs Cần Có

- Danh sách bài đã đăng trong tuần (từ Buffer hoặc Notion)
- Số liệu ban đầu sau 24–48h đăng (Reach sơ bộ, Reactions)
- File `ai-execution-sop.md` để kiểm tra đã thực hiện đúng SOP chưa

---

## Quy Trình

### Bước 1 — Tổng Hợp Tuần (5 phút)

Claude hỏi user xác nhận:
```
Tuần [X] (Ngày - Ngày), bạn đã đăng:
- Bài 1: [Tên] — [Kênh] — [Ngày] — [Reach sơ bộ]?
- Bài 2: [Tên] — [Kênh] — [Ngày] — [Reach sơ bộ]?
...
Còn bài nào chưa liệt kê không?
```

### Bước 2 — Cập Nhật Notion (3 phút)

Với mỗi bài đã đăng, update Notion properties:
```
Status: 📤 Published
Published Date: [ngày thực tế đăng]
Reach: [số sơ bộ sau 24h]
Notes: "Link post: [URL]"
```

Nếu có Notion MCP:
→ Tự động update qua `mcp__claude_ai_Notion__notion-update-page`

Nếu không:
→ Claude tạo checklist → bạn update thủ công (2 phút)

### Bước 3 — Tạo Weekly Summary File

**Lưu tại:** `outputs/[brand]-[YYYY-MM]/weekly-summary-W[X]-[YYYY-MM-DD].md`

```markdown
# Tóm Tắt Tuần [X] — [Brand]

**Kỳ:** [Ngày - Ngày]
**Người thực hiện:** Content Execution Agent
**Tạo bởi:** /weekly-report

---

## Bài Đã Đăng Tuần Này

| # | Tiêu đề | Kênh | Format | Ngày đăng | Reach (24h) | Link |
|---|---|---|---|---|---|---|
| 1 | [Tên] | Facebook | Infographic | [Date] | [số] | [URL] |
| 2 | [Tên] | TikTok | Video | [Date] | [số] | [URL] |

**Tổng:** [X] bài / [X] kênh

---

## So Sánh Với Kế Hoạch

| Kênh | Planned | Actual | Ghi chú |
|---|---|---|---|
| Facebook | [X] bài | [X] bài | ✅ / ⚠️ thiếu [X] bài |
| TikTok | [X] bài | [X] bài | ✅ / ❌ |

---

## Highlight Tuần Này

**Bài có Reach cao nhất:** [Tên] — [Kênh] — [Số]
**Bài cần theo dõi thêm:** [Tên] — Lý do: [...]

---

## Nội Dung Chưa Hoàn Thành (Carry-over)

- [ ] [Bài chưa đăng] — Lý do: [...] — Dời sang tuần [X+1]

---

## Notes Cho Content Planner

[Quan sát ngắn: có gì bất thường? Trend nào nổi lên? Cần quyết định gì từ Planner?]

---

*Handoff cho: Content Planner Agent → chạy /performance-tracking để đánh giá sâu hơn*
```

### Bước 4 — Tạo Google Apps Script

Claude tạo script để user paste vào Google Sheets:

**Lưu tại:** `outputs/[brand]-[YYYY-MM]/update-sheets-W[X].js`

```javascript
/**
 * Weekly Report — [Brand] — Tuần [X]
 * Paste vào Google Sheets: Extensions → Apps Script → Run
 */
function updateWeeklyData() {
  var ss = SpreadsheetApp.openById('1yHqda0EOtWidPyHAwqhsacmL0iyk97jrDTpbo6W3SU0');
  
  // Tab Performance: thêm từng bài đã đăng
  var perfSheet = ss.getSheetByName('Performance');
  if (!perfSheet) perfSheet = ss.insertSheet('Performance');
  
  var weekData = [
    // [Date, Brand, Channel, Title, Reach, Engagement, ER%, Comments, Shares, Link]
    ['[DATE]', '[BRAND]', 'Facebook', '[TITLE]', [REACH], [ENG], [ER], [CMT], [SHR], '[URL]'],
    // ... thêm row cho từng bài
  ];
  
  weekData.forEach(function(row) {
    perfSheet.appendRow(row);
  });
  
  // Tab Calendar: cập nhật status
  var calSheet = ss.getSheetByName('Calendar View');
  if (!calSheet) calSheet = ss.insertSheet('Calendar View');
  // Update status của bài đã đăng thành "Published"
  
  SpreadsheetApp.flush();
  Logger.log('Updated ' + weekData.length + ' posts for Week [X]');
}

// Chạy hàm này:
// 1. Vào Extensions → Apps Script
// 2. Paste code này
// 3. Click ▶ Run → Authorize nếu cần → Done
```

### Bước 5 — Commit & Push

```bash
git add outputs/[brand]-[YYYY-MM]/weekly-summary-W[X]-*.md
git add outputs/[brand]-[YYYY-MM]/update-sheets-W[X].js
git commit -m "Week [X] report: [X] posts published, [brand]"
git push
```

---

## Output Summary

| File | Nội dung | Ai dùng |
|---|---|---|
| `weekly-summary-W[X].md` | Tổng hợp tuần, bài đã đăng, compare plan | Planner Agent đọc |
| `update-sheets-W[X].js` | Apps Script → paste vào Google Sheets | User chạy 1 lần |
| Notion updated | Từng bài: Status = Published, Reach sơ bộ | Tự động nếu có MCP |

---

## Handoff Workflow

```
Execution Agent chạy /weekly-report
    ↓
weekly-summary-W[X].md tạo xong
    ↓
User paste update-sheets-W[X].js vào Google Sheets
    ↓
Planner Agent nhận notification (hoặc user chạy)
    ↓
/performance-tracking đọc weekly-summary + Notion
    ↓
CMO-level evaluation + action items tuần sau
```

---

**Agent sử dụng:** Content Execution Agent  
**Cadence:** Cuối mỗi tuần  
**Tạo bởi:** Marketing Content Workspace v2  
**Ngày:** 2026-05-12
