'''

查找集合元素
    集合没有自带的查找方法
    我们可以通过系统自带的in/not 判断元素是否在集合中
'''


set00 = set("helloWorld")
is_in = "h" in set00
is_not_in = "h" not in set00

print(is_in)
print(is_not_in)