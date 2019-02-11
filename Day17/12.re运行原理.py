import re

"""
dushine@126.com
"""
pattern = re.compile("^\w{6,}@(126|163|qq)\.com$")

result = pattern.match("dushine@126.com")

print(result)