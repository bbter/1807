'''
查找字典元素
    get(key)
        查找key对应的value,如果不存在返回None
    dict01.keys())
        获取字典所有的键的集合
    dict01.values()
        获取字典所有的值的集合
    dict01.items()
        获取字典所有的键值对的集合
    update(dict00)
        更新参数字典中的数据,如果没有则添加，如果存在则覆盖
'''

dict01 = {"username": "bbter",
          "password": 123456,
          "address": "杭州",
          "is_on_work": True,
          "city": ["北京", "深圳", "上海", "湖南"],}

print(dict01.get("city"))
print(dict01.get("city00"))

print(dict01.copy())

print(dict01.keys())

# for key in dict01.keys():
#     print(key)

print(dict01.values())

print(dict01.items())

for item in enumerate(dict01.items(),1):
    print(item)


dict02 = {"email":"dushine@126.com","username":"bbt"}
dict01.update(dict02)
print(dict01)


for key,value in dict01.items():
    print("%s:%s" %(key,value))