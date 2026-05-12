# Skill: /copywrite

## Mô tả
Viết copy cho bất kỳ kênh và format nào, áp dụng đúng framework copywriting cho từng platform. Có hai chế độ: **Full** (3 variations + bias analysis + compliance check) và **Quick** (1 variation, không hỏi thêm, ra ngay).

## Cú pháp

**Full mode** (mặc định, dùng khi có thời gian, cần A/B test):
```
/copywrite [platform] [brief ngắn]
```

**Quick mode** (dùng khi cần nhanh, không cần 3 variations):
```
/copywrite [platform] [brief] --quick
```

**Platforms:** `facebook` | `instagram` | `tiktok` | `linkedin` | `email` | `blog` | `ads`

**Ví dụ Full:**
```
/copywrite facebook "Bài giáo dục sức khỏe thai kỳ tuần 28, angle: điều bất ngờ về sự phát triển của bé"
/copywrite ads "Facebook Ad cho dịch vụ khám thai định kỳ, audience: phụ nữ 25-35 đang mang thai"
```

**Ví dụ Quick:**
```
/copywrite facebook "Chúc mừng Ngày của Mẹ, warm tone, CTA: nhắn tin đặt lịch" --quick
/copywrite tiktok "Hook cho video tips uống nước khi mang thai" --quick
/copywrite instagram "Caption ảnh buổi sáng tại phòng khám, vibe: ngày mới bắt đầu" --quick
```

## Quick Mode — Cách Hoạt Động

Khi có flag `--quick`, Claude:
- Không hỏi thêm câu hỏi nào
- Không hỏi về brand voice (dùng tone warm + professional làm default)
- Chỉ tạo **1 variation tốt nhất** thay vì 3
- Không chạy bias analysis hoặc compliance check trừ khi brief có từ khóa ngành nhạy cảm (y tế, tài chính)
- Không sync Notion, không lưu file
- Output trong vòng 1 lượt, không có follow-up

**Dùng Quick mode khi:**
- Content mang tính thời vụ (chúc mừng ngày lễ, reaction trending topic)
- Đã biết rõ brand voice, chỉ cần đẩy nhanh output
- Đang trong luồng sản xuất nhanh, không muốn bị ngắt
- Test ý tưởng trước khi commit vào full production

**Dùng Full mode khi:**
- Content quan trọng (campaign lớn, ad spend cao)
- Chưa chắc về angle hoặc tone
- Cần A/B test thật sự
- Lần đầu viết cho platform hoặc audience mới

## Claude sẽ hỏi gì khi chạy
1. Target audience là ai? (dùng persona từ content plan nếu có)
2. CTA mong muốn là gì? (đặt lịch / nhắn tin / xem thêm / mua ngay)
3. Tone: professional / warm & personal / educational / urgent
4. Có brand voice guide hoặc ví dụ copy cũ không?
5. Ngành gì? (để kiểm tra compliance)

## Frameworks Per Platform

### Facebook / Instagram Post
**Framework: Hook → Story/Pain → Solution → Social Proof → CTA**
```
[HOOK — câu đầu tiên phải dừng scroll]
[Line break]
[Story ngắn hoặc pain point của audience]
[Line break]
[Solution / insight / value]
[Line break]
[Social proof hoặc call to reflect]
[Line break]
👉 [CTA rõ ràng]
```

### TikTok / Reels Script
**Framework: Hook 3s → Tension → Reveal/Value → CTA Overlay**
```
[0–3s: Hook visual + hook câu nói — phải gây tò mò hoặc shock nhẹ]
[3–15s: Xây tension hoặc đặt câu hỏi]
[15–45s: Reveal / value / thông tin chính]
[Cuối: CTA bằng lời + text overlay]
```
*Thêm: Gợi ý B-roll, âm thanh background, text overlay timing*

### LinkedIn Article / Post
**Framework: Contrarian Insight Hook → Problem → Framework/Data → CTA**
```
[Hook: Quan điểm ngược số đông hoặc insight bất ngờ]
[Problem: Tại sao điều này quan trọng]
[Framework: 3–5 điểm có cấu trúc rõ ràng]
[Kết: Bài học / lời kêu gọi hành động professional]
```

### Email
**Framework: Subject + Preview → Story Hook → Value → CTA Button**
- Subject line: 40–50 ký tự, có số hoặc câu hỏi
- Preview text: Bổ sung cho subject, không lặp lại
- Body: Story ngắn → chuyển sang value → CTA rõ ràng 1 nút
- P.S. line: Thường đọc nhiều hơn body

### Blog Article
**Framework: SEO Title → Meta Description → Hook Intro → H2 Structure → CTA**
- Title: Có keyword + số hoặc "cách" + benefit
- Meta: 155 ký tự, có keyword
- Intro: Hook + promise + outline bài
- H2s: Mỗi section trả lời 1 câu hỏi cụ thể
- CTA: Cuối bài + sidebar

### Ad Copy (Facebook / Google)
**3 Variations bắt buộc:**
- **Rational:** Tập trung tính năng, số liệu, chứng cứ
- **Emotional:** Tập trung cảm xúc, nỗi sợ, khát vọng
- **Urgency:** Tập trung khan hiếm, deadline, FOMO

## Output
- 3 variations đánh số rõ ràng
- Giải thích ngắn tại sao mỗi variation dùng approach đó
- Ghi chú compliance nếu cần
- Lưu vào Notion content database nếu đang dùng

## Ví dụ Output — TikTok Script (Case Sản Phụ Khoa)
```markdown
## Variation 1: Hook "Câu hỏi bất ngờ"
---
[0–3s] Hook: Bạn có biết bé 28 tuần tuổi đang làm gì ngay lúc này không? 🤔
[Text overlay: "Tuần 28 — điều bác sĩ thấy mỗi ngày"]

[3–20s] Tension: Hầu hết các mẹ chỉ biết bé đạp. Nhưng siêu âm 4D tuần này cho thấy...
[B-roll: hình ảnh siêu âm / animation bé trong bụng]

[20–50s] Reveal: Bé đã có phản xạ mắt nhắm mở / học cách nuốt / nhận ra giọng nói mẹ.
3 điều quan trọng mẹ cần làm ở tuần này: [1], [2], [3]

[50–60s] CTA: Bình luận "Tuần [X]" để mình làm video về tuần thai của bạn nhé!
[Text overlay: Đặt lịch khám định kỳ — link in bio]

**Ghi chú compliance:** Không claim "bảo đảm", thêm "Tham khảo thêm ý kiến bác sĩ của bạn"
---

## Variation 2: Hook "Sự thật bác sĩ"
[0–3s] Hook: Là bác sĩ sản phụ khoa, câu hỏi mình nghe nhiều nhất tuần này là...
...
```

## Bẫy Tư Duy Khán Giả — Viết Copy Dựa Trên Cognitive Bias

Hiểu bias của audience giúp viết copy chạm đúng tâm lý. Quan trọng: **dùng đúng bias cho đúng funnel stage.** Dùng nhầm stage thì copy phản tác dụng hoặc đẩy người mua đi xa hơn.

### Bias × Funnel Stage Matrix

| Funnel Stage | Mục tiêu copy | Bias hiệu quả nhất | Bias tránh dùng |
|---|---|---|---|
| **Awareness** | Dừng scroll, gây chú ý, nhận ra vấn đề | Negativity Bias, Availability Heuristic, Curiosity Gap | Sunk Cost (họ chưa đầu tư gì), Urgency giả tạo |
| **Consideration** | Build trust, giải thích tại sao brand này | Halo Effect, Social Proof, Confirmation Bias | Anchoring giá sớm (chưa hiểu giá trị), Fear appeal quá mạnh |
| **Conversion** | Xóa bỏ lý do cuối cùng, thúc đẩy hành động | Anchoring, Framing Effect, Loss Aversion, Scarcity (thật) | Thêm thông tin mới (gây confusion), Quá nhiều lựa chọn |
| **Retention** | Củng cố quyết định đã mua, tăng LTV | Sunk Cost (đã đầu tư rồi, tiếp tục), Identity Bias, Social Proof từ cộng đồng | Negativity Bias (họ đã là khách, đừng làm họ sợ) |

### Biases Và Cách Dùng Chi Tiết

| Bias | Audience đang nghĩ | Dùng tốt nhất ở stage | Copy example |
|---|---|---|---|
| **Negativity Bias** | Việc xấu tác động mạnh hơn việc tốt | Awareness | "90% mẹ bầu bỏ qua dấu hiệu này ở tuần 28..." |
| **Availability Heuristic** | Đánh giá rủi ro qua thứ dễ nhớ nhất | Awareness | Story cụ thể, case thật, tên thật thay vì số liệu trừu tượng |
| **Curiosity Gap** | Muốn lấp đầy khoảng trống thông tin | Awareness | "Điều bác sĩ biết mà không nói với bạn về..." |
| **Halo Effect** | Ấn tượng tốt 1 khía cạnh lan sang tổng thể | Consideration | Credential đặt trước story: chuyên môn tạo trust, story tạo gần gũi |
| **Social Proof** | Theo số đông để giảm rủi ro | Consideration | "1,200 mẹ bầu đã tin tưởng / Câu hỏi được hỏi nhiều nhất..." |
| **Confirmation Bias** | Chỉ thấy thông tin ủng hộ niềm tin sẵn có | Consideration | Bắt đầu bằng điều audience đã tin, dẫn dắt sang insight mới |
| **Anchoring** | Thông tin đầu tiên chi phối mọi đánh giá sau | Conversion | Đặt anchor cao trước: "Nếu khám tại bệnh viện lớn, bạn mất X. Tại đây, chỉ..." |
| **Framing Effect** | Cách trình bày thay đổi cách đánh giá | Conversion | "Chỉ 50k/ngày" thay vì "1.5 triệu/tháng" cho cùng một giá |
| **Loss Aversion** | Sợ mất mạnh hơn muốn được | Conversion | "Mỗi tuần không khám là 1 tuần bỏ lỡ..." thay vì "Lợi ích của việc khám..." |
| **Scarcity (thật)** | Khan hiếm tạo giá trị | Conversion | Chỉ dùng khi scarcity là thật. Scarcity giả phá trust. |
| **Sunk Cost** | Tiếp tục vì đã đầu tư quá nhiều | Retention | "Bạn đã đi được nửa hành trình thai kỳ, đây là bước tiếp theo..." |
| **Identity Bias** | Hành động phù hợp với self-image | Retention | "Những mẹ bầu chủ động như bạn thường..." |

### Quy Trình 3 Bước Khi Viết Copy
1. Xác định funnel stage của content piece này
2. Chọn 1-2 bias phù hợp từ matrix trên
3. Claude thông báo: "Mình sẽ dùng [Bias] vì content này ở [Stage]. Hook sẽ khai thác [cụ thể]."

**Warning:** Dùng Fear/Negativity ở Conversion stage thường làm người mua do dự thêm thay vì chốt. Dùng Urgency giả ở bất kỳ stage nào đều phá trust dài hạn.

**Transparency — Skill sẽ thông báo:**
Trước khi viết, Claude sẽ nói rõ: "Mình sẽ dùng framework [X] vì [lý do]. Bias đang address: [Y]." Điều này giúp bạn hiểu logic sau mỗi variation và điều chỉnh nếu cần.

## Bước Tiếp Theo Sau Khi Có Copy
- Chạy `/visual creative` để tạo visual đi kèm
- Upload variations vào Notion để track A/B test results
- Nếu là ad copy, chạy `/platform algorithm [platform]` để verify format đang compliant với thuật toán hiện tại

## Lưu ý
- **Y tế:** Không claim chữa khỏi, không bảo đảm kết quả. Luôn có "Tham khảo bác sĩ của bạn"
- **Personal brand:** Dùng ngôi "mình/bạn", kể chuyện thật, tránh tone corporate
- **A/B test:** Chạy 2 variations cùng lúc, đo sau 48-72 giờ, giữ winner
- **Caption Facebook:** Dòng đầu tiên phải đủ mạnh để dừng scroll, đây là điều quyết định reach
- **Ngôn ngữ output:** Không dùng dấu gạch ngang dài trong copy tiếng Việt. Dùng dấu phẩy, dấu chấm, xuống dòng thay thế.
