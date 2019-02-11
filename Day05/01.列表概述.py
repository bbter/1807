import keyword
print(keyword.kwlist)
print(type(keyword.kwlist))
key_list = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(len(key_list))

'''
定义列表：
        列表名称 = [元素1，元素2，元素3, ......]
        列表长度可以看做是无限制
        列表中存放的元素可以是不同类型
'''
# name_list
# nameList
# NameList

name_list = ['张三','李四','王五','赵六','无啦']
num_list = [1,22,33,44,555]
bool_list = [True,False,True]

print(name_list)
print(num_list)
print(bool_list)

test_list = ['张三',18,False]
print(test_list)

test_list = [num_list,num_list,bool_list]
print(test_list)

test_list = [None]
print(test_list)
print(len(test_list))











