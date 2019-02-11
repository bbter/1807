"""
分组
    (a|b|c)
断言
    向后无宽度断言，(?=rex)

"""
import re

# username = input("请输入用户名:")
username = "lala111"
str00 = "^(?=.+[a-zA-Z])(?=.+[0-9])[a-z0-9A-Z]{6,}$"
result = re.match(str00, username)
if result:
    print(result)
    print("注册成功")
else:
    print("注册失败")

print("%s" % username)

str01 = """<head><title>Python基础笔记_Day17_Python排列组合、破解密码、Python正则表达式</title></head>"""
print(type(str01))
str00 = "<head><title>(.*)</title></head>"
result = re.match(str00, str01)
print(result.group())

str00 = "<head><title>(.*)</title></head>"
result = re.search(str00, str01)
print(result.group())

str00 = "<title>(.*)</title>"
result = re.findall(str00, str01)
print(result)

print("*" * 20)

str00 = "<title>(.*)</title>"
result = re.findall(str00, str01)
print(result)
