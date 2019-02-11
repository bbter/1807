'''
删除集合元素
        pop()
            删除集合中的第一个元素
        remove()
            删除集合中指定元素,如果元素不存在报错
        clear()
            清空集合,输出到控制台的是set()
        del
            del 无法删除指定元素可以删除set对象
'''

set00 = set("helloWorld")
set00.pop()
print(set00)
'''
set00.pop()
print(set00)
set00.pop()
print(set00)
set00.pop()
print(set00)
'''

set00.remove("W")
print(set00)
# set00.remove("W")
# print(set00)


# set00.clear()
# print(set00)  #set()


# del set00
# print(set00)