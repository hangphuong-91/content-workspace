#!/usr/bin/env python3
"""
OpenAI Research Helper — Gọi GPT o1/4o cho deep research tasks
Dùng bởi: competitor-research.md, market-intelligence.md
Điều kiện: Environment variable OPENAI_API_KEY phải được set
"""

import os
import json
import sys
from typing import Optional, Dict, Any

def get_openai_client():
    """Tạo OpenAI client từ env var OPENAI_API_KEY"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  OPENAI_API_KEY không được set. Bỏ qua GPT deep analysis.")
        return None

    try:
        from openai import OpenAI
        return OpenAI(api_key=api_key)
    except ImportError:
        print("⚠️  openai package không được cài. Chạy: pip install openai")
        return None


def gpt_competitor_deep_analysis(
    competitor_audit_data: str,
    brand_name: str = "Brand"
) -> Optional[Dict[str, Any]]:
    """
    Phase 5.5: Gửi competitor audit data tới GPT o1 để phân tích sâu

    Args:
        competitor_audit_data: String chứa toàn bộ audit (bảng so sánh, gap analysis, SWOT)
        brand_name: Tên brand đang audit

    Returns:
        Dict gồm: hidden_patterns, viral_factors, quick_wins, risks
        Hoặc None nếu OpenAI không available
    """
    client = get_openai_client()
    if not client:
        return None

    prompt = f"""
You are a strategic analyst for content marketing.
Analyze the following competitor audit data for {brand_name} and provide deep insights.

COMPETITOR AUDIT DATA:
{competitor_audit_data}

Task:
1. Identify 3 hidden patterns in how competitors approach content strategy
2. Analyze 2-3 root causes of why certain content goes viral
3. Recommend 3 quick wins that can be implemented within 2 weeks
4. Highlight 2 key risks if directly copying competitor strategy

Format your response as valid JSON:
{{
  "hidden_patterns": ["pattern1", "pattern2", "pattern3"],
  "viral_factors": [
    {{"factor": "...", "examples": [...], "how_to_leverage": "..."}},
    ...
  ],
  "quick_wins": [
    {{"action": "...", "timeframe": "1-2 weeks", "expected_impact": "..."}},
    ...
  ],
  "risks": ["risk1", "risk2"]
}}

IMPORTANT: Return ONLY valid JSON, no additional text.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Use gpt-4o instead of o1 (faster, still capable)
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=1,  # Required for gpt-4o
            max_tokens=2000
        )

        response_text = response.choices[0].message.content
        # Extract JSON from response
        try:
            analysis = json.loads(response_text)
            return analysis
        except json.JSONDecodeError:
            # Try to extract JSON if there's text wrapper
            import re
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return None

    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return None


def gpt_market_intelligence_synthesis(
    market_data: str,
    brand_name: str = "Brand",
    month: str = "Current"
) -> Optional[Dict[str, Any]]:
    """
    Section 5: Gửi market intelligence data tới GPT o1 để synthesize patterns

    Args:
        market_data: String chứa sections 1-4 (SEO, Algorithm, Competitor Pulse, Recommendations)
        brand_name: Tên brand
        month: Tháng/năm

    Returns:
        Dict gồm: market_patterns, top_3_opportunities, content_adjustments, risk_signals
        Hoặc None nếu OpenAI không available
    """
    client = get_openai_client()
    if not client:
        return None

    prompt = f"""
You are a content strategy analyst with expertise in SEO, social media algorithms, and competitive intelligence.
Synthesize the following market intelligence data for {brand_name} ({month}).

MARKET INTELLIGENCE DATA:
{market_data}

Task:
1. Identify 3 hidden patterns connecting SEO trends → algorithm changes → competitor moves
2. Find 3 best opportunities: high SEO volume + competitor gap + algorithm support
3. Reprioritize the content calendar based on feasibility + ROI from market data
4. Flag 2 risk signals that could impact next week's performance

Format response as JSON:
{{
  "market_patterns": ["pattern1", "pattern2", "pattern3"],
  "top_3_opportunities": [
    {{
      "theme": "...",
      "seo_volume": "high/medium/low",
      "competitor_gap": "...",
      "algorithm_support": "...",
      "recommended_format": "...",
      "estimated_impact": "..."
    }},
    ...
  ],
  "content_adjustments": [
    {{
      "content_piece": "...",
      "action": "promote/deprioritize/adjust_angle",
      "reason": "..."
    }},
    ...
  ],
  "risk_signals": ["signal1", "signal2"]
}}

IMPORTANT: Return ONLY valid JSON, no additional text.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_tokens=2000
        )

        response_text = response.choices[0].message.content
        try:
            synthesis = json.loads(response_text)
            return synthesis
        except json.JSONDecodeError:
            import re
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return None

    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return None


def save_gpt_analysis_to_file(
    analysis: Dict[str, Any],
    output_path: str,
    analysis_type: str = "competitor"
):
    """Lưu GPT analysis result vào file JSON"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, ensure_ascii=False, indent=2)
        print(f"✅ GPT analysis saved to {output_path}")
    except Exception as e:
        print(f"❌ Failed to save analysis: {e}")


if __name__ == "__main__":
    # Test mode
    print("OpenAI Research Helper - Test Mode")
    print(f"OPENAI_API_KEY set: {bool(os.getenv('OPENAI_API_KEY'))}")

    if os.getenv('OPENAI_API_KEY'):
        print("✅ Ready to call OpenAI API")
    else:
        print("⚠️  OPENAI_API_KEY not set")
