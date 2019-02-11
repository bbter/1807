'''
in / not in
count
index
'''


name_list = ["张默", "宁财神", "李代沫", "房祖名", "柯震东", "高虎", "宋冬野",["伊相杰","伊相杰"]]

is_in = "高虎" in name_list
print(is_in)
is_in = "高虎" not in name_list
print(is_in)

# 查看元素在列表中的下标,返回下标的integer值,如果元素不存在就报错
index = name_list.index("高虎")
print(index)

# index = name_list.index("张三",1 ,10)
# print(index)

# 查看元素在列表中出现的次数,如果没有就返回0
count = name_list.count("伊相杰")
print(count)

count = name_list.count("张默")
print(count)

count = name_list.count("张三")
print(count)


count = name_list.count(["伊相杰","伊相杰"])
print(count)






























