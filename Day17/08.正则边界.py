"""
字符      功能
^        匹配字符串的开头
$        匹配字符串的结尾
\b       表示匹配一个单词的边界
"""
import re

mail_126 = "dushine@126.com"
mail_qq = "472214395@qq.com"
mail_163 = "dushine2008@163.com"

str00 = "^\w{6,}@(126|163|qq)\.com$"
result = re.match(str00, mail_163)
print(result)

# \bXXX\b
str01 = "\\bis\\b"
result = re.findall(str01, "my name is Lisly")
print(result)
