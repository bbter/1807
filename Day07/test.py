import time
# stus = [
# 	{"name": "张三", "age": 18},
# 	{"name": "李四", "age": 35},
# 	{"name": "王五", "age": 22}]
#
# stus.sort(key=lambda x:x["age"])
# print(stus)

# dic1 = {}
# with open("b.txt","r",encoding="utf-8") as f:
#         list00 = f.readlines()
#         for i in list00:
#             list01 = i.split("]")
#             list02 = list01[1].split("[")
#             time = list02[1]
#             list03 = i.split("\n")
#             list04 = list03[0].split("]",)
#             content = list04[2]
#             dic1[time] = content
#
# print(dic1)


# def timetotal(func):
# 	def wrapper():
# 		start_time = time.time()
# 		func()
# 		end_time = time.time()
# 		total_time = end_time - start_time
# 		print(total_time)
# 	return wrapper
#
# @timetotal
# def sercet():
# 	print("把大象放入箱子里秘籍")
# 	time.sleep(1)
# 	print("第一步:把箱子打开")
# 	time.sleep(1)
# 	print("第二步:把大象放进去")
# 	time.sleep(1)
# 	print("第三步:把箱子关上")
#
# sercet()



com1 = {"生活用品":{"商品":"牙刷","日期":"2018-12-19","物流码":10086}}

print(com1)
# 添加商品
def addCom(com):
	type = input("请输入你想添加类型:")
	name = input("请输入商品名字")
	date = input("请输入日期")
	num = input("请输入物流码")
	com[type] = {"商品":name,"日期":date,"物流码":num}
	print(com)

# 删除商品
def delCom(com):
	type = input("请输入你想要删除类型:")
	if type in com.keys():
		del com[type]
		print(com)
	else:
		print("不存在")

# 修改商品
def changeCom(com):
	type = input("请输入你想要修改的类型:")
	if type in com1.keys():
		typedic = com[type]
		print(typedic)
		msg = input("请输入你想要修改的信息")
		if msg in typedic.keys():
			print(typedic[msg])
			content = input("请输入你修改的内容")
			typedic[msg] = content
			print(com)
		else:
			print("不存在")
	else:
		print("不存在")

# 查询商品
def searchCom(com):
	type = input("请输入你想要查询的类型:")
	if type in com1.keys():
		typedic = com[type]
		print(typedic)
	else:
		print("不存在")
# 
# 
# 
# addCom()
# delCom()


# def demo(a, *args, b=1200):
#     print('a：', a)
#     print('b：', b)
#     print('args：', args)
#
#
# demo(600, 10, 10, 30)



while True:
    print("欢迎使用天狗商品管理系统:1.添加、2.删除、3.修改、4.查询（单个查询/显示所有）、0.退出")
    select = input("请输入你需要的服务:")
    if select.isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            print("欢迎使用添加功能")
            addCom(com1)
        elif select == 2:
            print("欢迎使用删除功能")
            delCom(com1)
        elif select == 3:
            print("欢迎使用修改功能")
            changeCom(com1)
        elif select == 4:
            print("欢迎使用查询功能")
            searchCom(com1)
        else:
            print("输入有误")
    else:
        print("输入有误,请重新输入")
