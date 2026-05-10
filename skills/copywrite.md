# Skill: /copywrite

## Mô tả
Viết copy cho bất kỳ kênh và format nào, áp dụng đúng framework copywriting cho từng platform. Tạo 3 variations mỗi lần để A/B test. Có thể đọc brand voice guide từ Notion nếu có. Tự động compliance check nếu ngành cần.

## Cú pháp
```
/copywrite [platform] [brief ngắn]
```

**Platforms:** `facebook` | `instagram` | `tiktok` | `linkedin` | `email` | `blog` | `ads`

**Ví dụ:**
```
/copywrite facebook "Bài giáo dục sức khỏe thai kỳ tuần 28, angle: điều bất ngờ về sự phát triển của bé"
/copywrite tiktok "Script video Q&A: bác sĩ trả lời câu hỏi thật của bệnh nhân về sinh thường vs sinh mổ"
/copywrite email "Newsletter tháng 5: tổng hợp tips chăm sóc sức khỏe thai kỳ mùa nóng"
/copywrite ads "Facebook Ad cho dịch vụ khám thai định kỳ, audience: phụ nữ 25-35 đang mang thai"
```

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

Hiểu bias của audience giúp viết copy chạm đúng tâm lý. Với mỗi content piece, xác định 1-2 bias đang chi phối audience rồi address trực tiếp trong copy.

**Biases phổ biến nhất trong content marketing:**

| Bias | Audience đang nghĩ | Cách dùng trong copy |
|---|---|---|
| **Anchoring (Neo giá)** | Thông tin đầu tiên chi phối đánh giá | Đặt frame sớm: "Hầu hết bác sĩ mất 15 năm mới có X. Mình làm được sau 3 năm vì..." |
| **Availability Heuristic (Dễ nhớ dễ tin)** | Đánh giá rủi ro qua thứ dễ nhớ nhất | Dùng story cụ thể, tên thật, case thật thay vì số liệu trừu tượng |
| **Confirmation Bias (Xác nhận niềm tin)** | Chỉ thấy thông tin ủng hộ sẵn | Bắt đầu bằng điều audience đã tin, rồi dẫn dắt sang insight mới |
| **Sunk Cost (Chi phí chìm)** | Tiếp tục vì đã đầu tư quá nhiều | Trong retention content: "Bạn đã đi được nửa chặng đường, đây là bước tiếp theo..." |
| **Negativity Bias (Tiêu cực mạnh hơn)** | Việc xấu tác động mạnh hơn việc tốt | Pain point copy mạnh hơn benefit copy. Dùng cho awareness/consideration stage. |
| **Social Proof (Tư duy bầy đàn)** | Theo số đông để giảm rủi ro | "1,200 mẹ bầu đã..." / "Câu hỏi được hỏi nhiều nhất tuần này..." |
| **Framing Effect (Đóng khung)** | Cách trình bày thay đổi cách đánh giá | "Chỉ 50k/ngày" thay vì "1.5 triệu/tháng". Cùng số tiền, khác cảm nhận. |
| **Halo Effect (Hào quang)** | Ấn tượng tốt 1 khía cạnh lan sang tổng thể | Credential + warm story cùng lúc: chuyên môn tạo trust, story tạo gần gũi |

**Quy trình 3 bước khi phát hiện bias trong brief:**
1. Gọi tên bias đang chi phối audience mục tiêu
2. Quyết định: address thẳng hay dùng bias đó để dẫn dắt?
3. Tích hợp vào hook và core message

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
