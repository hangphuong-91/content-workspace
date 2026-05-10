# Skill: /platform algorithm

## Mô tả
Tra cứu thuật toán MỚI NHẤT của các nền tảng mạng xã hội và tìm kiếm. Mỗi lần chạy đều search FRESH từ nguồn chính thống — không dùng kiến thức cũ vì thuật toán thay đổi liên tục. Output được date-stamp và khuyến nghị chạy lại mỗi tháng.

## Cú pháp
```
/platform algorithm [platform]
```

**Platforms hỗ trợ:** `facebook` | `tiktok` | `instagram` | `linkedin` | `youtube` | `google` | `twitter` (X)

**Ví dụ:**
```
/platform algorithm facebook
/platform algorithm tiktok
/platform algorithm google
```

## Claude sẽ làm gì khi chạy
Không hỏi thêm — chạy ngay:
1. WebSearch: `"[platform] algorithm update [year] [month]"`
2. WebSearch: `"[platform] algorithm changes [year] creators"`
3. WebFetch từ official newsroom/blog của platform (xem danh sách nguồn bên dưới)
4. Tổng hợp thành cheat sheet

## Nguồn Chính Thống Per Platform

| Platform | Official Source | URL |
|---|---|---|
| Facebook | Meta Newsroom + Meta for Business | newsroom.fb.com / facebook.com/business/news |
| TikTok | TikTok Newsroom + TikTok for Business | newsroom.tiktok.com / ads.tiktok.com/blog |
| Instagram | Instagram Blog (Meta) | about.instagram.com/blog |
| LinkedIn | LinkedIn Marketing Blog | business.linkedin.com/marketing-solutions/blog |
| YouTube | YouTube Official Blog + Creator Academy | blog.youtube / support.google.com/youtube/creators |
| Google | Google Search Central Blog | developers.google.com/search/blog |
| Twitter/X | X Blog | blog.x.com |

## Output Format
```markdown
# [Platform] Algorithm Cheat Sheet
**Cập nhật:** [Tháng/Năm] | **Nguồn:** [URL]

## Đang được ưu tiên (PUSH nhiều hơn)
- ...

## Đang bị giảm reach / penalized
- ...

## Best practices tháng này
- ...

## Format & tần suất khuyến nghị
- Format tốt nhất: ...
- Thời lượng video tối ưu: ...
- Tần suất khuyến nghị: ...
- Thời điểm đăng tốt: ...
- Hashtag strategy: ...

## Thay đổi lớn gần đây
- ...

## Áp dụng cho content plan
- Kênh này phù hợp nhất cho: [awareness / engagement / conversion]
- Content type ưu tiên đầu tư: ...
```

## Ví dụ Output — Facebook (tháng 5/2026)
```markdown
# Facebook Algorithm Cheat Sheet
**Cập nhật:** 05/2026 | **Nguồn:** newsroom.fb.com

## Đang được ưu tiên
- Reels ngắn 30–60 giây với hook 3 giây đầu mạnh
- Content "meaningful interactions" — post kích thích comment thật, không engagement bait
- Video native (upload thẳng Facebook, không link YouTube)
- Bài viết từ friends/family được ưu tiên hơn pages

## Đang bị giảm reach
- Link bài báo ngoài (giảm ~50% reach)
- Caption quá dài không có line break
- Engagement bait ("tag bạn bè", "thích nếu đồng ý")
- Repost content từ TikTok có watermark

## Best practices tháng này
- Dùng caption dạng "hook câu hỏi" → paragraph ngắn → CTA
- Reply comment trong 1 giờ đầu để boost distribution
- Đăng Stories 5–7 lần/tuần song song với feed post

## Format & tần suất
- Format tốt nhất: Reels (30–60s) + Carousel
- Tần suất: 3–5 post/tuần (không cần nhiều, cần đều)
- Thời điểm: 7h–9h sáng hoặc 8h–10h tối
- Hashtag: 3–5 hashtag liên quan, không spam
```

## Lưu ý
- **Luôn date-stamp output** — thông tin này có hạn sử dụng ~1 tháng
- Chạy lại mỗi tháng hoặc khi thấy reach giảm bất thường
- Thuật toán Google (SEO) thay đổi chậm hơn social — có thể chạy mỗi quý
- Thông tin từ official blog > thông tin từ influencer/creator speculation
