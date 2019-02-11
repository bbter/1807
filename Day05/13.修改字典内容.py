'''
修改字典内容
        dic[key] = value
        如果key存在就修改原来可以对应value的值
        如果key不存在就直接添加一个键值对
'''

dict01 = {"username": "bbter",
          "password": 123456,
          "address": "杭州",
          "is_on_work": True,
          "city": ["北京", "深圳", "上海", "湖南"], }

dict01["password"] = 1000000
print(dict01)
print(id(dict01))


dict01["phone_num"] = "13868864676"
print(dict01)
print(id(dict01))
















