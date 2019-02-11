'''
列表的常用操作
        查看元素
            通过元素下标查看元素,如果下标超出范围报错IndexError

'''
name_list = ["张三", "李四", "王五", "赵六", "钱琪", "天霸"]

print(name_list[3])
# print(name_list[14])

# 修改元素:找到元素,重新赋值
print(id(name_list))
name_list[-1] = "田八"
print(name_list)
print(id(name_list))

str00 = "hello"
# str00[1] = "a"
print(str00)

'''
列表增加元素
    append 追加 默认添加在末尾
'''
name_list = ["张默", "宁财神", "李代沫", "房祖名", "柯震东", "高虎", "宋冬野"]
name_list.append("陈羽凡")
print(name_list)
name_list.append("伊相杰")
print(name_list)

# 插入到指定位置,它之后的所有元素下标都会改变
name_list.insert(1,"满文军")
print(name_list)

# 把可迭代类型的元素拆开放入列表末尾
name_list00 = ["莫少聪","张耀扬"]
name_list.extend(name_list00)
print(name_list.extend(name_list00))
print(name_list)

name_list.extend(range(10))
print(name_list.extend(name_list00))
print(name_list)

# 拷贝
print("*"*30)
name_list_copy = name_list.copy()
print(name_list_copy)

print(id(name_list))
print(id(name_list_copy))

# 列表相加,把两个列表中的元素取出组成一个新的列表
name_list00 = ["莫少聪","张耀扬"]
name_list01 = ["张默", "宁财神", "李代沫"]

name_list = name_list00 + name_list01
print(name_list)
print(id(name_list00))
print(id(name_list01))
print(id(name_list))





































