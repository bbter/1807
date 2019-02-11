'''
添加元素
    add(element)
        把指定元素添加到集合中,会自动去重
        不可变类型
    update
        把新的元素添加进入到集合中,会自动去重
        可变类型
'''

set00 = set(range(5))
print(set00)

# 把指定元素添加到集合中,会自动去重
set00.add(3)
set00.add("hello")
set00.add(True)
# 可变类型数据无法放入集合
set00.add((1,2,3))
print(set00)

# update 把新的元素添加进入到集合中,会自动去重
set00.update([1,3,5,7,9])
print(set00)

set00.update("hello")
print(set00)
set00.add("world")
print(set00)

set01 = {2,4,6,8,10}
set00.update(set01)
print(set00)

# set00.add(set01)










