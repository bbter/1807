import re
str00 = "[\w]{6,20}@126\.com"
result = re.match("[\w]{6,20}@126\.com", "dushine@126.com")
print(result.group())

str00 = "[\w]{6,20}@126\.com$"
result = re.match("^[\w]{6,20}@126\.com$", "dushine@126.com")
print(result.group())

# result = re.match("[\w]{6,20}@126\.com$", "dushine@126.comcom")
# print(result.group())

result = re.match(r".*is", "my name isnpt Lily")
print(result.group())

str00 = "(?=.+[a-zA-Z])(?=.+[0-9])[a-zA-Z0-9]{6,}$"
# username = input()
username = "111haha"
result = re.match(str00, username)
print(result)
pattern = re.compile(str00)
result = re.match(pattern, username)
print(result)


str00 = "[dushine]{6,20}@126.com"
pattern = re.compile(str00)
result = re.match(pattern, "hellodushine@126.com")
print(result)

