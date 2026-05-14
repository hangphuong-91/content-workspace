# OpenAI Integration Guide — Research Skills

## Tổng Quan

2 skills được tích hợp OpenAI deep research:
1. **`/competitor-research`** — Phase 5.5: GPT phân tích sâu audit data
2. **`/market-intelligence`** — Section 5: GPT synthesize market patterns

## Cấu Hình Ban Đầu

### 1. Set Environment Variable (Một Lần)

**Windows PowerShell (Admin):**
```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-proj-[YOUR-OPENAI-API-KEY]", "User")
```

**Ở đây `[YOUR-OPENAI-API-KEY]` là key bạn tạo từ https://platform.openai.com/account/api-keys**

**Verify:**
```powershell
$env:OPENAI_API_KEY
```

Nếu thấy `sk-proj-...` → OK ✅

### 2. Install OpenAI Python Package

```bash
pip install openai
```

## Cách Hoạt Động

### Competitor Research — Phase 5.5

**Khi nào:** Sau khi hoàn thành bước 1-4 (SWOT matrix)

**Ghi vào prompt:**
```python
from skills.openai_research_helper import gpt_competitor_deep_analysis, save_gpt_analysis_to_file

# Lấy competitor audit data từ Phase 1-4
audit_data = """
[Toàn bộ content từ bước 1-4]
"""

# Gọi GPT analysis
analysis = gpt_competitor_deep_analysis(audit_data, brand_name="[Brand]")

if analysis:
    # Lưu kết quả
    save_gpt_analysis_to_file(analysis, "outputs/[brand]-[YYYY-MM]/gpt-competitor-analysis.json")
    
    # In kết quả
    print("🧠 GPT Insights:")
    print(f"Hidden Patterns: {analysis['hidden_patterns']}")
    print(f"Quick Wins: {analysis['quick_wins']}")
else:
    print("⚠️  GPT analysis không available")
```

### Market Intelligence — Section 5

**Khi nào:** Sau khi hoàn thành sections 1-4

**Ghi vào prompt:**
```python
from skills.openai_research_helper import gpt_market_intelligence_synthesis, save_gpt_analysis_to_file

# Lấy market data từ sections 1-4
market_data = """
[Toàn bộ content từ sections 1-4]
"""

# Gọi GPT synthesis
synthesis = gpt_market_intelligence_synthesis(market_data, brand_name="[Brand]", month="[Tháng/Năm]")

if synthesis:
    # Lưu kết quả
    save_gpt_analysis_to_file(synthesis, "outputs/[brand]-[YYYY-MM]/gpt-market-synthesis.json")
    
    # In kết quả
    print("🧠 Market Synthesis:")
    print(f"Top Opportunities: {synthesis['top_3_opportunities']}")
    print(f"Risk Signals: {synthesis['risk_signals']}")
else:
    print("⚠️  GPT synthesis không available")
```

## Output Format

### Competitor Analysis (gpt-competitor-analysis.json)
```json
{
  "hidden_patterns": [
    "Pattern 1: Đối thủ ưu tiên video short-form + educational tone",
    "Pattern 2: Caption dài (150+ từ) có engagement cao hơn",
    "Pattern 3: Posting giờ vàng (7-9 AM, 6-8 PM) ảnh hưởng lớn"
  ],
  "viral_factors": [
    {
      "factor": "User-generated testimonials",
      "examples": ["Bài X có 500 shares", "Bài Y có 200 comments"],
      "how_to_leverage": "Tạo series "Câu chuyện bệnh nhân thực" hàng tuần"
    }
  ],
  "quick_wins": [
    {
      "action": "Tạo 2 video TikTok/week thay vì 1",
      "timeframe": "1-2 weeks",
      "expected_impact": "Reach tăng 40% dựa vào competitor data"
    }
  ],
  "risks": [
    "Nếu copy caption style của đối thủ quá gần, có thể bị coi là giảm authenticity"
  ]
}
```

### Market Intelligence Synthesis (gpt-market-synthesis.json)
```json
{
  "market_patterns": [
    "SEO volume cao cho 'thai kỳ tuần X' + TikTok ưu tiên video educational → Cơ hội tạo series tuần thai",
    "Competitors chưa khai thác 'hồi thai không có dấu hiệu' topic → Gap lớn",
    "Algorithm ưu tiên video dài hơn (3-5 min) so với short clips"
  ],
  "top_3_opportunities": [
    {
      "theme": "Series tuần thai — Y khoa + storytelling",
      "seo_volume": "high",
      "competitor_gap": "Chỉ 1 đối thủ có series này, coverage chưa đầy đủ",
      "algorithm_support": "TikTok + YouTube ưu tiên educational video series",
      "recommended_format": "3-5 min video + carousel + blog post",
      "estimated_impact": "500+ reach/bài (từ SEO volume 5K/tháng)"
    }
  ],
  "content_adjustments": [
    {
      "content_piece": "Blog bài 'Chuẩn bị cho sinh'",
      "action": "promote",
      "reason": "SEO volume tăng 30% tháng này, algorithm ưu tiên"
    }
  ],
  "risk_signals": [
    "Facebook reach đang giảm — cân nhắc chuyển resources sang TikTok",
    "Competitor X vừa launch campaign video dài — có thể ảnh hưởng tới reach nếu không adjust strategy"
  ]
}
```

## Fallback Behavior

**Nếu OPENAI_API_KEY không set hoặc OpenAI call fail:**
- ✅ Skills vẫn chạy bình thường (WebSearch mode)
- ℹ️ In warning: `"⚠️  OPENAI_API_KEY không được set. Bỏ qua GPT deep analysis."`
- ❌ Sections 5 (GPT analysis) sẽ bị skip

**Workflow không bị ngắt — chất lượng WebSearch analysis vẫn đầy đủ.**

## Cost Estimate

**OpenAI API Pricing (2026):**
- gpt-4o: $2.50 per 1M input tokens, $10 per 1M output tokens
- Mỗi competitor analysis: ~500-1000 input tokens → **~$0.01-0.03**
- Mỗi market synthesis: ~1000-2000 input tokens → **~$0.03-0.05**

**Hàng tháng (1 brand, 1 competitor audit + 1 market intelligence):**
- ~$0.10-0.20 cost
- **Tiết kiệm 5-10 giờ phân tích manual**

## Troubleshooting

| Issue | Giải pháp |
|---|---|
| `ModuleNotFoundError: No module named 'openai'` | Chạy `pip install openai` |
| `AuthenticationError: Invalid API key` | Check env var: `$env:OPENAI_API_KEY` |
| `RateLimitError: 429` | Wait 1 minute, retry |
| JSON decode error từ GPT | Thử prompt khác hoặc model khác (gpt-4, gpt-3.5-turbo) |

## Next Steps

1. ✅ Set OPENAI_API_KEY env var
2. ✅ Install openai package: `pip install openai`
3. ✅ Run `/competitor research` hoặc `/market-intelligence` — sẽ tự động call GPT nếu có key
4. ✅ Check `gpt-*.json` files trong outputs folder
5. ✅ Feed GPT insights vào `/content plan` → Content Planner dùng để adjust strategy

---

**Created:** 2026-05-14  
**Skills affected:** competitor-research.md, market-intelligence.md  
**Helper:** openai-research-helper.py
