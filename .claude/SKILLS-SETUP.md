# Hướng Dẫn Setup 6 Skills vào Claude Code

**Workspace:** Marketing Content Workspace v1.0.0  
**Repository:** https://github.com/hangphuong-91/content-workspace  
**Created:** 2026-05-10

---

## Bước 1: Clone Repository

```bash
git clone https://github.com/hangphuong-91/content-workspace.git
cd content-workspace
```

---

## Bước 2: Kiểm Tra Claude Code Settings

Mở Claude Code → Settings (⚙️) → tìm section về Skills hoặc Workspace Configuration.

Đường dẫn thường là:
- **Mac/Linux:** `~/.claude/` hoặc `~/.config/claude/`
- **Windows:** `C:\Users\[YourName]\.claude\` hoặc `C:\Users\[YourName]\AppData\Local\claude\`

---

## Bước 3: Copy Skills Folder

**Option A — Tự động (Recommended):**
```bash
# Từ trong repo folder
cp -r .claude/skills ~/.claude/skills
cp .claude/skills-manifest.json ~/.claude/skills-manifest.json
```

**Option B — Thủ công:**
1. Mở folder `.claude/skills/` từ repo
2. Copy toàn bộ vào `~/.claude/skills/`
3. Copy file `skills-manifest.json` vào `~/.claude/`

---

## Bước 4: Đăng Ký Skills trong Claude Code

### Cách 1: File Config YAML/JSON (Nếu Claude Code hỗ trợ)

Tạo hoặc edit file `~/.claude/skills-config.json`:

```json
{
  "skills_directories": [
    "~/.claude/skills"
  ],
  "custom_skills": [
    {
      "name": "content-plan",
      "description": "Content Plan Orchestrator",
      "manifest": "~/.claude/skills-manifest.json"
    }
  ]
}
```

Restart Claude Code.

### Cách 2: Khai Báo trong Settings UI

1. Mở Claude Code → Settings
2. Tìm "Skills" hoặc "Custom Skills"
3. Thêm folder path: `~/.claude/skills`
4. Save và restart

### Cách 3: Dùng Commands (Nếu Claude Code hỗ trợ CLI)

```bash
claude-code skill add content-plan ~/.claude/skills/content-plan.md
claude-code skill add competitor-research ~/.claude/skills/competitor-research.md
claude-code skill add platform-algorithm ~/.claude/skills/platform-algorithm.md
claude-code skill add copywrite ~/.claude/skills/copywrite.md
claude-code skill add visual-creative ~/.claude/skills/visual-creative.md
claude-code skill add ai-execution ~/.claude/skills/ai-execution.md
```

---

## Bước 5: Xác Minh Setup Thành Công

Sau khi setup, test mỗi skill:

```
/content plan "test topic"
/competitor research "test brand"
/platform algorithm facebook
/copywrite facebook "test brief"
/visual creative "test visual"
/ai execution
```

Nếu skills hiện lên gợi ý hoặc chạy được → **Setup thành công!**

---

## Cấu Trúc Folder Sau Setup

```
~/.claude/
├── skills/
│   ├── content-plan.md
│   ├── competitor-research.md
│   ├── platform-algorithm.md
│   ├── copywrite.md
│   ├── visual-creative.md
│   ├── ai-execution.md
│   ├── content-plan/
│   │   ├── templates/
│   │   │   ├── brief-template.md
│   │   │   ├── plan-template.md
│   │   │   └── tracking-template.md
│   │   ├── sources.md
│   │   └── notion-schema.md
│   ├── competitor-research/
│   │   ├── templates/
│   │   │   └── audit-template.md
│   │   └── analysis-framework.md
│   ├── copywrite/
│   │   ├── frameworks/
│   │   │   ├── social-media.md
│   │   │   ├── email.md
│   │   │   ├── blog.md
│   │   │   └── ads.md
│   │   ├── brand-voice-template.md
│   │   └── platform-specs.md
│   ├── visual-creative/
│   │   ├── platform-specs.md
│   │   ├── ai-prompt-templates.md
│   │   └── canva-guide.md
│   └── ai-execution/
│       ├── tool-matrix.md
│       ├── sop-template.md
│       └── repurposing-matrix.md
│
├── skills-manifest.json
└── skills-config.json (tạo từ Cách 1)
```

---

## External Integrations Cần Cài

Các MCPs/tools mà skills dùng:

| Tool | Cần cho skill nào | Cách setup |
|---|---|---|
| **Notion MCP** | content-plan, copywrite, ai-execution | Kết nối Notion account từ Claude Code |
| **Google Drive MCP** | content-plan, visual-creative | Kết nối Google account từ Claude Code |
| **Canva MCP** | visual-creative | Kết nối Canva account từ Claude Code |
| **GitHub CLI** | ai-execution, content-plan | `winget install GitHub.cli` (Windows) |

Setup MCPs:
1. Claude Code → Extensions/Integrations
2. Tìm từng MCP, authenticate
3. Cho phép access cần thiết

---

## Troubleshooting

**Q: Skills không xuất hiện khi gõ `/`**
- A: Kiểm tra PATH đúng chưa, restart Claude Code, check file .md syntax

**Q: Skill chạy nhưng báo lỗi "MCP not found"**
- A: Cần setup Notion/Google Drive/Canva MCP trước

**Q: Muốn update skill code sau này**
- A: Edit file `.md` trong `~/.claude/skills/`, tự động update (reload Claude Code)

**Q: Muốn share workspace với người khác**
- A: Share GitHub repo link + hướng dẫn Bước 1-5 này

---

## Quick Reference — Common Commands

```
# Xem tất cả skills
/skills list

# Chạy skill với quick mode
/copywrite facebook "brief" --quick
/content plan "topic" --quick

# Chạy skill với full mode
/content plan "topic"

# Competitor research
/competitor research "brand"

# Platform algorithm (fresh search)
/platform algorithm facebook

# AI Execution từ plan file
/ai execution path/to/content-plan.md
```

---

## Tips Dùng Hiệu Quả

1. **Chạy theo thứ tự workflow:** competitor-research → platform-algorithm → content-plan → ai-execution → copywrite + visual-creative
2. **Dùng quick mode khi:** cần nhanh, test ý tưởng, hoặc chỉ cần 1 output
3. **Dùng full mode khi:** lập plan lớn, A/B testing, hand-off cho người khác
4. **Luôn cung cấp brand voice guide:** Khi chạy copywrite lần đầu để output consistent
5. **Lưu outputs vào Notion:** Tracking + hand-off dễ dàng hơn

---

## Support & Updates

- **Bugs:** Report tại https://github.com/hangphuong-91/content-workspace/issues
- **Feature requests:** GitHub discussions
- **Updates:** Check GitHub releases mỗi tháng

**Last updated:** 2026-05-10
