import re
"""
正则表达式，又称规则表达式。
（英语：Regular Expression，在代码中常简写为regex、regexp或RE），计算机科学的一个概念。
正则表达式通常被用来检索、替换那些符合某个模式(规则)的文本。

正则表达式是对字符串（包括普通字符（例如，a 到 z 之间的字母）和特殊字符（称为“元字符”））
操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，
这个“规则字符串”用来表达对字符串的一种过滤逻辑。
正则表达式是一种文本模式，模式描述在搜索文本时要匹配的一个或多个字符串
"""
# help(re)

str00 = "qianfenge"
result = re.match(str00, "qianqianfengedu")
print(result.group())
print(result.end())
