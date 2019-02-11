'''
元组有一个特征:一旦确定不可更改--------元组和元组元素id不可变
增
    没有提供增加元素的方法
删
    没有提供删除的方法TypeError
    可以使用del tuple删除整个对象
改
    元组不可更改,否则报错TypeError
查
    count
        查看指定元素在元组中的个数，如果没有返回0
    index
        查看指定元素在元组中第一次出现的位置下标,如果没有就报错
排序
    没有提供排序的方法
    可以使用sorted进行排序，但是可以使用sorted生成一个新的列表4
相加
    元组可以相加,得到一个包含两个元组内容的新元组
'''

tuple00 = (1, 2, 5, 30,1, 2, 5, 3)
# tuple00[0] = 10
# print(tuple00[0])

# del tuple00
# print(tuple00)
print(tuple00.count(1))

# print(tuple00.index(301))


print(max(tuple00))
print(min(tuple00))



print(sorted(tuple00))

tuple01 = (123,"hello",[1,2,3])
print(id(tuple01[2]))
tuple01[2].append(4)
print(tuple01)
print(id(tuple01[2]))


# tuple01[0] += "woed"
# print(tuple01)


tuple02 = (456,789)
tuple03 = tuple01 + tuple02
print(tuple03)


print(id(tuple02))
tuple02 += tuple01
print(tuple02)
print(id(tuple02))


'''
in   /  not in
'''
tuple01 = (123,"hello",[1,2,3])
is_in = 123 in tuple01
is_not_in = 123 not in tuple01
print(is_in)
print(is_not_in)

tuple01 = (123,"hello",[1,2,3])
is_in = [1,2,3] in tuple01
is_not_in = [1,2,3] not in tuple01
print(is_in)
print(is_not_in)



# join
list00 = ["a","b.txt","c","d","e","f","g"]
print("\t".join(list00))

# print(".".join(tuple01))

