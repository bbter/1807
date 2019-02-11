import re

# 匹配任意字符
str00 = "."
result = re.match(str00, "<1abcd")
print(result)
print(result.group())

# 匹配方括号中有的内容，只匹配一个
str01 = "[abcd]"
result = re.match(str01, "babcd")
print(result)
print(result.group())

# \d       匹配数字（0~9）
str02 = "\d"
result = re.match(str02, "1babcd")
print(result)
print(result.group())

# \D       匹配非数字，即不是数字
str03 = "\D"
result = re.match(str03, "babcd")
print(result)
print(result.group())

# \s       匹配空白格   空格  tab
str04 = "\s"
result = re.match(str04, " babcd")
print(result)
print(result.group())

# \S       匹配非空格
str05 = "\S"
result = re.match(str05, "babcd")
print(result)
print(result.group())

# \w       匹配单词字符，a~z A~Z 0~9 _
str06 = "\w"
result = re.match(str06, "_1babcd")
print(result)
print(result.group())

# \W       匹配非单词字符
str07 = "\W"
result = re.match(str07, " ?_1babcd")
print(result)
print(result.group())

# 匹配方括号中有的内容，只匹配一个
# str08 = "[a-z0-9A-Z]"
str08 = "[a-z0-9A-Z]"
result = re.match(str08, "Ababcd")
print(result)
print(result.group())

ret = re.match("嫦娥1号", "嫦娥1号发射成功")
print(ret.group())
ret = re.match("嫦娥2号", "嫦娥2号发射成功")
print(ret.group())
ret = re.match("嫦娥3号", "嫦娥3号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号", "嫦娥3号发射成功")
print(ret.group())
