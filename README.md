# Content Workspace — Marketing Content Skills cho Claude Code

Workspace gồm 6 skills dùng với Claude Code, hoạt động như một content team đầy đủ cho solo marketer hoặc small team.

## Cài đặt

1. Copy folder `skills/` vào `.claude/skills/` trong project của bạn
2. Mở Claude Code trong project đó
3. Bắt đầu dùng bằng lệnh bên dưới

## 6 Skills

| Skill | Lệnh | Mô tả |
|---|---|---|
| Competitor Research | `/competitor research [brand]` | Audit đối thủ, gap analysis, top 10 ideas |
| Platform Algorithm | `/platform algorithm [platform]` | Thuật toán mới nhất từ nguồn chính thống |
| Content Plan | `/content plan [topic]` | Plan 3 tháng: personas, OPE calendar, tracking |
| Copywrite | `/copywrite [platform] [brief]` | Copy 3 variations theo framework từng platform |
| Visual Creative | `/visual creative [brief]` | Creative brief + AI prompts + Canva design |
| AI Execution | `/ai execution [plan-file]` | SOP vận hành + tool matrix + repurposing tree |

## Flow Khuyến Nghị

```
Bước 1: /competitor research "ngành của bạn"
Bước 2: /platform algorithm facebook
         /platform algorithm tiktok
Bước 3: /content plan "brand/topic của bạn"
Bước 4: /ai execution → nhận SOP + tool matrix
Bước 5 (mỗi tuần): /copywrite + /visual creative cho từng content piece
```

## Kết Nối External

- **Notion:** Lưu content plan database, tracking status per piece
- **Google Drive:** Upload file .md, export visual
- **Canva:** Tạo design trực tiếp qua MCP (cần Canva account)
- **GitHub (repo này):** Version control tất cả output

## Folder Structure

```
content-workspace/
├── README.md
├── skills/                    ← Copy vào .claude/skills/ của project
│   ├── content-plan.md
│   ├── competitor-research.md
│   ├── platform-algorithm.md
│   ├── copywrite.md
│   ├── visual-creative.md
│   └── ai-execution.md
├── outputs/                   ← Output từ mỗi lần chạy skill
│   └── [brand-topic]-[YYYY-MM]/
└── exports/                   ← Chat history exports
```

## Test Case

Test với case: **Bác sĩ sản phụ khoa tư nhân có thương hiệu cá nhân**

```
/competitor research "phòng khám sản phụ khoa tư nhân TPHCM"
/platform algorithm facebook
/platform algorithm tiktok
/content plan "Personal brand bác sĩ sản phụ khoa tư nhân"
```

## Yêu Cầu

- Claude Code (claude.ai/code hoặc CLI)
- Notion account (cho Notion MCP)
- Canva account (cho Visual Creative skill)
- Google Drive (cho file storage)

---

*Được tạo bằng Claude Code | Skills lưu tại `.claude/skills/` (project-level)*
