# Quick Reference — Common Commands

**Marketing Content Workspace v1.0.0**

---

## 🚀 Workflow Sequence (Copy & Paste)

### New Brand/Topic — Full Setup

```bash
# 1. Research competitors
/competitor research "your brand or niche"

# 2. Check algorithms
/platform algorithm facebook
/platform algorithm tiktok
/platform algorithm instagram
/platform algorithm linkedin

# 3. Create 3-month plan
/content plan "your brand or topic"

# 4. Generate production SOP
/ai execution content-outputs/[folder-from-step-3]/content-plan.md

# 5. Each week: produce content
/copywrite facebook "Specific brief for this week's post"
/visual creative "Instagram carousel about topic X"
```

---

## ⚡ Quick Commands (Fast Output)

```bash
# Copy these for quick content production

# Social post copy (no questions, 1 variation)
/copywrite facebook "Weekly tip: hydration during pregnancy" --quick
/copywrite tiktok "Hook: 'You've been doing this wrong'" --quick
/copywrite instagram "Caption for transformation photo" --quick
/copywrite linkedin "Thought leadership: future of healthcare" --quick

# Email copy
/copywrite email "Monthly newsletter summary" --quick

# Blog post
/copywrite blog "SEO article about prenatal care" --quick

# Ads
/copywrite ads "Facebook ad for consultation booking" --quick

# Visual design
/visual creative "Facebook post infographic: pregnancy week 28"
/visual creative "TikTok thumbnail for doctor Q&A video"
/visual creative "LinkedIn banner for personal brand"
```

---

## 📊 Platform-Specific Examples

### Facebook
```bash
/platform algorithm facebook
/copywrite facebook "Weekly educational post about maternal health" --quick
/visual creative "Facebook post graphic about trimester 2"
```

### TikTok
```bash
/platform algorithm tiktok
/copywrite tiktok "Script: Doctor answers real pregnancy question" --quick
/visual creative "TikTok thumbnail with hook text overlay"
```

### LinkedIn
```bash
/platform algorithm linkedin
/copywrite linkedin "Article about work-life balance in medicine" --quick
/visual creative "LinkedIn article cover image"
```

### Email
```bash
/copywrite email "Weekly health tips newsletter"
/copywrite email "Event invitation: consultation appointment"
```

### Blog
```bash
/platform algorithm google
/copywrite blog "Blog post: Nutrition during pregnancy (SEO optimized)"
```

---

## 🎯 Common Scenarios

### "I need one piece of content ASAP"
```bash
/copywrite [platform] "[your brief]" --quick
```
**Result in 30 seconds:** 1 piece of copy, ready to use

### "I need A/B test options"
```bash
/copywrite [platform] "[your brief]"
```
**Result in 2 minutes:** 3 variations, ready to test

### "Starting fresh with a new brand"
```bash
/competitor research "brand/niche"
/platform algorithm facebook
/content plan "brand name"
```
**Result:** 3-month roadmap + competitor intelligence

### "I have a plan, need production SOP"
```bash
/ai execution content-outputs/[brand-YYYY-MM]/content-plan.md
```
**Result:** Weekly production schedule + tool matrix + SOP

### "This week I have 2 hours to produce"
```bash
/copywrite facebook "specific brief" --quick
/copywrite instagram "specific brief" --quick
/copywrite email "specific brief" --quick
/visual creative "one visual brief"
```
**Result:** 4 content pieces ready to schedule

---

## 📋 Brand Voice Setup

**One-time setup (do once):**
```bash
# Edit the brand voice guide
# File: .claude/skills/copywrite/brand-voice-template.md
# OR save to Notion and provide path when running /copywrite

# Then when running copywrite:
/copywrite facebook "brief"
→ Claude will ask: "Path to brand voice guide?"
→ Provide path or Notion link
→ All future copy will match brand voice automatically
```

---

## 🔄 Weekly Production Workflow

**Assuming you have a content plan from `/content plan`:**

### Monday (30 min)
```bash
# Check this week's planned content
# Review content calendar from content-plan output

# If algorithm changed, refresh:
/platform algorithm facebook
/platform algorithm tiktok
```

### Tuesday–Wednesday (2 hours)
```bash
# Write all text content in one batch session
/copywrite facebook "Post 1 brief"
/copywrite facebook "Post 2 brief"
/copywrite facebook "Post 3 brief"
/copywrite email "Newsletter brief"
/copywrite tiktok "Video script brief"
```

### Thursday (1.5 hours)
```bash
# Design all visuals in one batch
/visual creative "Facebook post visual"
/visual creative "Email header visual"
/visual creative "Instagram carousel"
/visual creative "TikTok thumbnail"
```

### Friday (30 min)
```bash
# Review all outputs
# Schedule social posts in Meta Business Suite / Buffer
# Schedule email in Mailchimp
# Manual TikTok upload (can't schedule on free account)
```

---

## 🆚 Full Mode vs Quick Mode

| Need | Use | Time |
|---|---|---|
| A/B testing different angles | `/copywrite [platform] [brief]` (full) | 2 min |
| Quick post ASAP | `/copywrite [platform] [brief] --quick` | 30 sec |
| New strategy document | `/content plan "topic"` (full) | 5-10 min |
| Quick 4-week outline | `/content plan "topic" --quick` | 2 min |

---

## 📁 Output Locations

After running skills, outputs save to:

```
outputs/
├── [brand]-[YYYY-MM]/
│   ├── content-plan.md
│   ├── competitor-audit.md
│   ├── tracking.md
│   └── ai-execution-sop.md
```

Also saves to:
- **Notion:** Content database + tracking
- **Google Drive:** Organized by month
- **GitHub:** Committed and pushed

---

## 🔍 Troubleshooting Quick Commands

### Skill not found?
```bash
# Refresh Claude Code
# Check that skills are in: ~/.claude/skills/
```

### Missing MCP error?
```bash
# Connect MCPs in Claude Code settings:
# - Notion MCP
# - Google Drive MCP
# - Canva MCP
```

### Want to change tool matrix?
```bash
# Edit: .claude/skills/ai-execution/tool-matrix.md
# Then re-run /ai execution
```

### Need new platform specs?
```bash
# Add to: .claude/skills/visual-creative/platform-specs.md
# Then re-run /visual creative
```

---

## 💾 Backup & Sharing

### Backup skills
```bash
# In this repo, always saved
git add .
git commit -m "Updated skills"
git push
```

### Share with team member
```bash
# 1. Share GitHub repo link
# 2. They follow SKILLS-SETUP.md
# 3. Share your brand voice guide
# 4. They have full setup
```

### Export conversation history
```bash
# In Claude Code:
/export
# Saves to: outputs/[date]-[conversation].txt
```

---

## 📈 Metrics to Track

From the tracking template, measure these per channel:

```
Weekly:
- Posts published
- Engagement rate
- Click-through rate (if applicable)
- Video views (for TikTok/YouTube)

Monthly:
- Reach growth
- Follower growth
- Conversions (bookings, signups, etc.)
- ROI (if paid)

Quarterly:
- Content pillar performance (which pillar drives most engagement?)
- Platform performance (which platform has best ROI?)
- Audience sentiment (from comments)
```

---

## 🎯 Example: Full Week for OB/GYN Doctor

**Monday:**
```bash
/platform algorithm facebook
/platform algorithm tiktok
```

**Tuesday:**
```bash
/copywrite facebook "Week 28 pregnancy: what's happening in the womb" --quick
/copywrite facebook "Myth: morning sickness means healthy pregnancy" --quick
/copywrite tiktok "Doctor answers: does spicy food affect baby?" --quick
/copywrite email "Weekly prenatal health tips newsletter" --quick
```

**Wednesday:**
```bash
/visual creative "Infographic: fetal development week 28 for Facebook"
/visual creative "TikTok thumbnail: doctor in clinic answering question"
/visual creative "Email header: pregnancy wellness checklist"
```

**Thursday:**
- Review all outputs
- Schedule on Meta Business Suite (Facebook + Instagram)
- Upload TikTok
- Schedule email newsletter

**Friday:**
- Check engagement
- Note any underperforming content
- Plan adjustments for next week

---

**Last updated:** 2026-05-10  
**For more:** See README.md and SKILLS-SETUP.md
