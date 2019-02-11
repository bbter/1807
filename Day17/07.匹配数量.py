"""
*      表示匹配前一个字符出现0次或者无限次，即可有可无
+      表示匹配前一个字符出现1次或者无限次，即至少一次
？     表示匹配前一个字符出现1次或则0次,即，要么一次，要么没有

{m}    表示匹配前一个字符出现m次
{m,}   表示前一个字符至少出现m次
{m,n}   表示匹配字符出现从m到n次
"""
import re

str00 = "\w"
result = re.match(str00, "abcdefg")
print(result.group())

# *      表示匹配前一个字符出现0次或者无限次，即可有可无
str01 = "\w*"
result = re.match(str01, "abcdefg")
print(result.group())

# +      表示匹配前一个字符出现1次或者无限次，即至少一次
str02 = "\w+"
result = re.match(str02, "abcd")
print(result.group())

# ？     表示匹配前一个字符出现1次或则0次,即，要么一次，要么没有
str03 = "\w?"
result = re.match(str03, "?abcd")
print(result.group())
"""
{m}    表示匹配前一个字符出现m次
{m,}   表示前一个字符至少出现m次
{m,n}   表示匹配字符出现从m到n次
"""
str04 = "\w{3}"
result = re.match(str04, "abcd")
print(result.group())

str04 = "\w{3,}"
result = re.match(str04, "abcd")
print(result.group())

str05 = "\w{3,5}"
result = re.match(str05, "abcd")
print(result.group())

"""
案例：
需求：一个字符串第一个字母为大写字符，后面都是小写并且这些小写字母可有可无
"""

str06 = "[A-Z][a-z]*"
result = re.match(str06, "AaaA")
print(result.group())

