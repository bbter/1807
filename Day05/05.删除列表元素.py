'''
clear()  清空列表
del()    清除列表
del L[index] 删除指定位置的元素
pop()    可以删除指定位置的元素,默认删除最后一个,如果下标超出范围,报错:IndexError
remove()  删除指定元素,如果元素不存在,报错:ValueError

'''

name_list = ["张默", "宁财神", "李代沫", "房祖名", "柯震东", "高虎", "宋冬野",["伊相杰","伊相杰"]]

print(name_list.pop())
print(name_list)

print(name_list.pop())
print(name_list)

print(name_list.pop(2))
print(name_list)

# print(name_list.pop(10))
# print(name_list)

name_list.remove('张默')
print(name_list)

# name_list.remove('张默')
# print(name_list)

# name_list.clear()
# print(name_list)

# delete

del name_list[0]
print(name_list)

# 从内存中抹除
# del name_list
# print(name_list)




