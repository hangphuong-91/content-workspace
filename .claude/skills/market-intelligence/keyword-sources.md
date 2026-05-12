# Nguồn Dữ Liệu — Nghiên Cứu Từ Khóa & Xu Hướng

## Nguồn Miễn Phí

### Google Trends
- URL: https://trends.google.com/trends/
- Cách dùng: Nhập từ khóa → xem Interest over time → Related queries
- Tốt cho: Xu hướng tìm kiếm, so sánh từ khóa, seasonality

### Google Search Console
- URL: https://search.google.com/search-console/
- Cần: Xác minh website trước
- Tốt cho: Từ khóa thực tế người dùng dùng để tìm website bạn

### Answer the Public (Giới hạn miễn phí)
- URL: https://answerthepublic.com/
- Tốt cho: Câu hỏi người dùng đặt ra về chủ đề

### Google Keyword Planner
- URL: https://ads.google.com/home/tools/keyword-planner/
- Cần: Google Ads account (miễn phí, không cần chạy quảng cáo)
- Tốt cho: Search volume, CPC ước tính

### Reddit & Quora
- Tìm: subreddit liên quan hoặc Quora topic
- Tốt cho: Câu hỏi thực tế người dùng đang hỏi → content ideas

---

## Nguồn Trả Phí (API)

### Ahrefs
- API docs: https://docs.ahrefs.com/
- Endpoint chính: `/v3/keywords-explorer/overview`
- Params: `select=volume,difficulty,cpc&country=vn`
- Giá: Từ $99/tháng

### SEMrush
- API docs: https://developer.semrush.com/
- Endpoint: `https://api.semrush.com/?type=phrase_organic`
- Database: `vn` cho Việt Nam
- Giá: Từ $119/tháng

### Ubersuggest (rẻ hơn)
- URL: https://app.neilpatel.com/
- Có API limit nhất định ở gói thấp
- Giá: Từ $29/tháng

---

## Nguồn Platform-Specific

### Facebook Trending
- Facebook Ads Library: https://www.facebook.com/ads/library/
- Xem: Quảng cáo đang chạy trong ngành → biết ai đang promote gì

### TikTok Creative Center
- URL: https://ads.tiktok.com/business/creativecenter/
- Xem: Trending songs, hashtags, creatives theo ngành
- Miễn phí

### YouTube Trending
- URL: https://www.youtube.com/feed/trending
- Lọc theo country: VN
- Xem top videos trong ngành

---

## Cách Dùng Trong /market-intelligence

```
Ưu tiên sử dụng:
1. Google Trends (miễn phí, đủ cho pulse check)
2. Ahrefs/SEMrush nếu có API key
3. TikTok Creative Center cho TikTok content
4. WebSearch bổ sung với query: "[từ khóa] xu hướng [tháng năm] Việt Nam"
```
