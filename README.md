# Marketing Content Workspace — Hệ Thống 7 Skills Claude Code

**Phiên bản:** 1.1.0  
**Ngày tạo:** 2026-05-10  
**Cập nhật:** 2026-05-12  
**Repository:** https://github.com/hangphuong-91/content-workspace

Workspace Claude Code hoàn chỉnh cho marketer một người hoặc nhóm nhỏ. 7 skills kết nối với nhau + tích hợp công cụ ngoài (Notion, Google Drive, Canva, GitHub, Buffer, Zapier) = máy tạo & đăng nội dung tự động từ đầu đến cuối.

---

## Workspace Này Làm Gì?

Biến một brief nội dung thành **chiến lược nội dung thực thi 3 tháng**:

```
Nghiên cứu đối thủ → Phân tích thuật toán nền tảng → Tạo kế hoạch nội dung
→ Xây quy trình sản xuất → Viết bài → Thiết kế hình ảnh
```

Phù hợp cho:
- Marketer một người / solopreneur
- Nhóm marketing nhỏ cần tự động hóa
- Agency muốn quy trình có thể lặp lại
- Bàn giao và chia sẻ kiến thức nội dung

---

## 7 Skills Cốt Lõi

| Skill | Lệnh | Chức năng | Khi nào dùng |
|---|---|---|---|
| **Kế hoạch nội dung** | `/content plan [chủ đề]` | Chiến lược 3 tháng: phân tích, chân dung khách hàng (Persona), lịch, theo dõi | Bắt đầu từ đây |
| **Nghiên cứu đối thủ** | `/competitor research [thương hiệu]` | Phân tích đối thủ, phân tích khoảng trống (Gap Analysis), SWOT | Trước kế hoạch nội dung |
| **Thuật toán nền tảng** | `/platform algorithm [nền tảng]` | Thuật toán (Algorithm) mới nhất từ nguồn chính thức | Trước kế hoạch nội dung |
| **Viết bài** | `/copywrite [nền tảng] [brief]` | Bài viết theo nền tảng × 3 biến thể thử nghiệm A/B | Sản xuất hàng tuần |
| **Thiết kế hình ảnh** | `/visual creative [brief]` | Brief thiết kế, câu lệnh AI tạo ảnh, thiết kế Canva | Sản xuất hình ảnh hàng tuần |
| **Thực thi AI** | `/ai execution [file-kế-hoạch]` | Biến kế hoạch thành quy trình + lịch hàng tuần + sơ đồ tái sử dụng (Repurposing) | Vận hành và bàn giao |
| **Lịch đăng bài tự động** | `/schedule posting [brand]` | Setup Zapier → Buffer → Facebook automation. Zero manual posting. | Sau khi approve content |

---

## Bắt Đầu Nhanh (5 phút)

### Bước 1: Cài Đặt Skills

Xem: **[.claude/SKILLS-SETUP.md](./.claude/SKILLS-SETUP.md)**

Tóm tắt:
```bash
# Sao chép thư mục skills
cp -r .claude/skills ~/.claude/skills
cp .claude/skills-manifest.json ~/.claude/

# Khởi động lại Claude Code
# Gõ / để thấy 7 skills
```

### Bước 2: Kết Nối Công Cụ Ngoài

Cần kết nối MCP:
- Notion (theo dõi nội dung)
- Google Drive (lưu trữ file)
- Canva (tạo thiết kế)
- GitHub CLI (quản lý phiên bản)

### Bước 3: Chạy Workflow

```bash
/competitor research "thương hiệu của bạn"
/platform algorithm facebook
/content plan "chủ đề của bạn"
/ai execution
/copywrite facebook "brief"
/visual creative "brief hình ảnh"
```

---

## Nội Dung Workspace

### Skills (7 files)
- `content-plan.md` — Điều phối, 5 giai đoạn, lịch nội dung (Content Calendar) 3 tháng
- `competitor-research.md` — Phân tích, phân tích khoảng trống (Gap Analysis), SWOT
- `platform-algorithm.md` — Thuật toán (Algorithm) mới nhất theo nền tảng
- `copywrite.md` — Frameworks theo nền tảng + 24 thiên kiến nhận thức
- `visual-creative.md` — Quy trình 3 bước: brief → câu lệnh AI tạo ảnh → Canva
- `ai-execution.md` — Quy trình, bảng công cụ, sơ đồ tái sử dụng nội dung (Repurposing)
- `schedule-posting.md` — Zapier + Buffer + Notion automation cho đăng bài tự động

### Supporting Files (19 mẫu & hướng dẫn)
- Mẫu: brief, kế hoạch, theo dõi, kiểm tra, quy trình
- Frameworks: viết bài mạng xã hội, email, blog, quảng cáo
- Hướng dẫn: giọng văn thương hiệu, thông số nền tảng, câu lệnh AI tạo ảnh, Canva, tuân thủ

### Đầu Ra Mẫu
- Trường hợp: Thương hiệu cá nhân (Personal Brand) bác sĩ sản phụ khoa tư nhân (Việt Nam)
- Trình tự: phân tích đối thủ → kế hoạch nội dung → quy trình → mẫu bài viết & hình ảnh

---

## Cách Hoạt Động

### Cho Marketer Một Người
1. Tuần 1: `/content plan` → nhận chiến lược 3 tháng
2. Tuần 2: `/ai execution` → nhận quy trình sản xuất hàng tuần
3. Mỗi tuần: `/copywrite` + `/visual creative`

**Kết quả:** 5-7 bài/tuần, lên kế hoạch nhanh hơn 80%

### Cho Nhóm Nhỏ
1. Quản lý: `/content plan` + `/ai execution` hàng quý
2. Người viết: dùng `/copywrite` hàng ngày
3. Người thiết kế: dùng `/visual creative` hàng ngày
4. Bàn giao: Quy trình đủ rõ để người không biết Claude Code follow được

### Cho Agency
1. Onboarding: `/competitor research` → phân tích thị trường
2. Đề xuất: `/content plan` → lộ trình 3 tháng
3. Thực thi: `/ai execution` → quy trình có thể lặp lại
4. Hàng quý: `/platform algorithm` → cập nhật thuật toán (Algorithm)

---

## Tính Năng Chính

**Kế hoạch 5 giai đoạn:** Phân tích thực trạng → Nền tảng chiến lược → Thông điệp → Lịch nội dung (Content Calendar) → Theo dõi

**Ma trận kênh OPE:** Chiến lược kênh Sở hữu/Trả phí/Lan truyền

**Viết bài dựa trên tâm lý học:** 24 thiên kiến nhận thức được ánh xạ với cách tiếp cận

**Ma trận Thiên kiến × Phễu tiếp thị (Funnel):** Thiên kiến nào hiệu quả nhất ở từng giai đoạn

**Chế độ nhanh:** Nhận đầu ra ngay cho nội dung khẩn cấp

**Chế độ đầy đủ:** Phân tích sâu cho quyết định chiến lược

**Sinh quy trình:** Sẵn sàng bàn giao để ủy thác

**Tích hợp Canva:** Tự động tạo hình ảnh với bộ nhận diện thương hiệu

**Theo dõi Notion:** Bảng trạng thái nội dung

**Tuân thủ tích hợp:** Ghi chú cho ngành có quy định (y tế, tài chính)

---

## Cấu Trúc Thư Mục

```
content-workspace/
├── CLAUDE.md           ← Hướng dẫn cho Claude (quy tắc ngôn ngữ)
├── plan.md             ← Kế hoạch dự án
├── README.md           ← Bạn đang ở đây
├── QUICK-REFERENCE.md  ← Cheat sheet lệnh
├── skills/
│   ├── content-plan.md
│   ├── competitor-research.md
│   ├── platform-algorithm.md
│   ├── copywrite.md
│   ├── visual-creative.md
│   ├── ai-execution.md
│   └── [mẫu & frameworks]
├── .claude/
│   ├── skills-manifest.json
│   └── SKILLS-SETUP.md
├── outputs/
│   └── [thương-hiệu-YYYY-MM]/
│       ├── content-plan.md
│       ├── competitor-audit.md
│       ├── ai-execution-sop.md
│       └── ...
└── exports/
    └── chat-history.txt
```

---

## Lệnh Thường Dùng

```bash
# Trình tự workflow (theo thứ tự)
/competitor research "thương hiệu của bạn"
/platform algorithm facebook
/platform algorithm tiktok
/content plan "chủ đề của bạn"

# Từ kế hoạch
/ai execution

# Sản xuất hàng tuần
/copywrite facebook "brief"
/copywrite email "bản tin"
/visual creative "brief hình ảnh"

# Chế độ nhanh (ngay lập tức, không hỏi)
/copywrite facebook "brief" --quick
/content plan "chủ đề" --quick
```

---

## Trường Hợp Thử Nghiệm: Bác Sĩ Sản Phụ Khoa

Workspace đã được thử nghiệm với: **Thương hiệu cá nhân (Personal Brand) bác sĩ sản phụ khoa tư nhân (TPHCM)**

Chạy trình tự này để kiểm tra cài đặt:
```bash
/competitor research "phòng khám sản phụ khoa tư nhân TPHCM"
/platform algorithm facebook
/platform algorithm tiktok
/content plan "Thương hiệu cá nhân bác sĩ sản phụ khoa tư nhân"
/ai execution outputs/bacsi-sanphukhoa-2026-05/content-plan.md
/copywrite facebook "Bài giáo dục sức khỏe thai kỳ tuần 28"
/visual creative "Ảnh thông tin (Infographic) thai kỳ tuần 28 cho Facebook"
```

---

## Tài Liệu Đầy Đủ

- **[CLAUDE.md](./CLAUDE.md)** — Quy tắc ngôn ngữ, ngữ cảnh dự án
- **[plan.md](./plan.md)** — Kiến trúc đầy đủ, danh sách kiểm tra
- **[SKILLS-SETUP.md](./.claude/SKILLS-SETUP.md)** — Cài đặt & đăng ký skills
- **[skills/content-plan.md](./skills/content-plan.md)** — Workflow 5 giai đoạn đầy đủ
- **[skills/copywrite.md](./skills/copywrite.md)** — Ánh xạ thiên kiến nhận thức
- **[skills/visual-creative.md](./skills/visual-creative.md)** — Mẫu câu lệnh AI tạo ảnh

---

## Frameworks Tích Hợp

- **Ma trận OPE:** Kênh Sở hữu/Trả phí/Lan truyền với % phân chia
- **Phễu tiếp thị (Funnel):** Nhận biết → Cân nhắc → Chuyển đổi → Giữ chân
- **Thiên kiến nhận thức:** 24 thiên kiến × kỹ thuật viết bài theo nền tảng
- **Phương pháp SUME:** Lọc insight chiến lược, tìm đòn bẩy, kiểm tra độ vững
- **Phương pháp Think-Kit:** Quy tắc dừng cứng, minh bạch, nhận thức thiên kiến
- **Tái sử dụng nội dung (Repurposing):** 1 bài gốc → 5-7 bài phát sinh (tối ưu 80/20)

---

## Danh Sách Kiểm Tra Bắt Đầu

- [ ] Clone repo: `git clone https://github.com/hangphuong-91/content-workspace`
- [ ] Đọc [SKILLS-SETUP.md](./.claude/SKILLS-SETUP.md)
- [ ] Sao chép skills vào Claude Code
- [ ] Cài đặt Notion MCP
- [ ] Cài đặt Google Drive MCP
- [ ] Cài đặt Canva MCP
- [ ] Cài đặt GitHub CLI
- [ ] Chạy thử nghiệm với `/competitor research`
- [ ] Kiểm tra thư mục outputs

---

## Đóng Góp

Tìm thấy lỗi? Ý tưởng cải tiến?

1. Fork repo
2. Tạo branch: `git checkout -b feature/cai-tien-copywrite`
3. Chỉnh sửa skill files
4. Kiểm tra với brief mẫu
5. Gửi Pull Request

---

**Xây dựng với Claude Code × Phương pháp Think-Kit + SUME**  
**v1.0.0 | 2026-05-10**
