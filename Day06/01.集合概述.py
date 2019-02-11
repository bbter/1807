'''

创建集合
    集合中的元素是无序的
    集合中的元素不可重复
'''

set00 = {"张三", "全蛋", "王尼玛"}
print(set00)

set01 = {"张三", "全蛋", "王尼玛", "全蛋", "王尼玛"}
print(set01)

set02 = {23,56,12,6543,123,1}
print(set02)

# 通过构造方法创建集合对象,会默认把可迭代对象拆分,去重,组成一个集合
set03 = set("hello")
print(set03)

set04 = set(["helloworld","hello","world"])
print(set04)

set05 = set(("helloworld","hello","world"))
print(set05)

set06 = set(range(10))
print(set06)

set07 = set(x*2 for x in range(10))
print(set07)







