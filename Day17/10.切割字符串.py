"""
split
"""
str00 = "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。"
result = str00.split("。", 1)
print(result)
print(len(result))

import re

result = re.split("。", str00, 1)
print(result)

str00 = "dushine@126.com"
result = re.split("\d", str00)
print(result)

file = open("demo10.txt",encoding="utf-8")
content = file.read()
file.close()

print(content)

result = re.findall("<a .*href=(.*)</a>", content)
print(result)
