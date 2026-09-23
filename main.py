import json
import os
import datetime

preview_date_str = os.environ.get("PREVIEW_DATE", "").strip()
if preview_date_str:
    today = datetime.date.fromisoformat(preview_date_str)
else:
    today = datetime.date.today()

# 读取双语json
with open("tips_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
tips_list = data["tips_list"]

idx = today.toordinal() % len(tips_list)
item = tips_list[idx]

generate_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>📖每日学习小Tips｜매일 학습 팁</title>
<style>
body{{font-family:system-ui,sans-serif;max-width:640px;margin:40px auto;padding:0 20px;}}
.card{{background:#f4faff;padding:34px;border-radius:14px;border:1px solid #cde2f5;}}
h1{{color:#204b87;font-size:24px;}}
.zh{{color:#194075;font-size:17px;line-height:1.7;margin:8px 0;}}
.kr{{color:#334155;font-size:16px;line-height:1.7;margin:8px 0;}}
.title-zh{{font-size:22px;font-weight:bold;color:#194075;margin:12px 0 4px;}}
.title-kr{{font-size:20px;color:#2c3e50;margin:0 0 16px;}}
.info{{font-size:13px;color:#666;margin-top:24px;}}
hr{{margin:24px 0;border:0;border-top:1px solid #cbd5e1;}}
</style>
</head>
<body>
<div class="card">
    <h1>📖 每日学习小Tips / 매일 학습 팁</h1>
    <p>📅 날짜/日期：{today}</p>

    <div class="title-zh">{item['title_zh']}</div>
    <div class="title-kr">{item['title_kr']}</div>

    <div class="zh">💡 {item['content_zh']}</div>
    <div class="kr">💡 {item['content_kr']}</div>

    <div class="zh">✨小建议：{item['suggest_zh']}</div>
    <div class="kr">✨제안：{item['suggest_kr']}</div>

    <hr/>
    <p class="info">페이지 생성 시간 / 页面生成时间：{generate_time}</p>
</div>
</body>
</html>
'''

with open("index.html","w",encoding="utf-8") as fp:
    fp.write(html)

print("中韩双语网页生成完毕")
