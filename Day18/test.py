# class Singleton(object):
#     __instance = None
#     __first_init = False
#
#     def __init__(self,name,age):
#         if not Singleton.__first_init:
#             self.name = name
#             self.age = age
#             Singleton.__first_init = True
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#
# a = Singleton("bbt",18)
# print(id(a))
# b = Singleton("iu",26)
# print(id(b))
#
# import math
# for i in range(-99, 100000):
#     if (math.sqrt(i+100)) % 1 == 0 and (math.sqrt(i+268)) % 1 ==0:
#         print(i)






# lista = [1,2,3]
# listb = lista + [4]
# print(listb)


# a = [1, 2, ['a', 'b']]
# b = a
# c = a.copy()
# a.insert(0, 3)
# a[-1].append(3)
#
#
#
# print(b)
# print(c)



# nums = [i for i in range(10) if i % 2]
# print(nums)





# s='abcdefg'
#
#
# print('*'.join(list(s)[:3]))


# import os
#
# os.getcwd()
# d = {'a':1,'b':2}
# b = {}
# for k,v in d.items():
#
#     d[v] = k#     print(d)









# nums = [0, 1, 'user_input', '2x', '2', '3', '3', '2', '6', '7', '9', '9']

# nums = list(set(nums))
# sum = 0
# for i in nums:
#     i = str(i)
#     if i.isdigit():
#         i = int(i)
#         sum += i
# print(sum)


# def show(self):
#     print("this is show %s" % self.name)
#
# @staticmethod
# def study():
#     print("i am study")
#
# @classmethod
# def play_game(cls):
#     print("%s正在玩游戏" % cls.name)
#
# Student = type("Student",(object,),{'name':'bbt','age':20,'show':show,'study':study,'play_game':play_game})
#
# a = Student()
# print(a.name)
# print(a.age)
# a.show()
# a.study()
# Student.study()
# a.play_game()
# Student.play_game()




#
#
# import os
# def getAll(path,sp = ""):
#     listFile = os.listdir(path)
#     sp += "  "
#     for name in listFile:
#         abspath = os.path.join(path,name)
#         if os.path.isdir(abspath):
#             print(sp + "目录",name)
#             getAll(abspath,sp)
#         else:
#             print(sp + "文件",name)
#
#
#
# print(os.getcwd())
#
#
# getAll('F:\QF1807\Day18')

#
# list00 = [45,67,98,34,32,56,243]
#
#
# for i in range(0,len(list00)-1):
#     for j in range(0,len(list00)-1):
#         if list00[j] > list00[j+1]:
#             list00[j], list00[j + 1] = list00[j + 1], list00[j]
#
#
# print(list00)
# import re
# str04 = r'''
#         ·人民网-图片http://www.people.com.cn/GB/tupian/
#         ·中国新闻图片网http://www.cnsphoto.com/
#         ·全景图片网http://www.quanjing.com/
#         ·八目妖http://www.haha168.com/
#         ·美图http://www.6to23.com/pic/
#         ·新华网-图片频道http://www.xinhuanet.com/photo/
#         ·国内新闻精彩图片集http://news.sina.com.cn/photo/c/index.shtml
#         ·中国花卉图片网http://www.fpcn.net/
#         ·超景图片库http://www.gettyimages.cn/
#         ·精美扫图http://www.enet.com.cn/eschool/includes/zhuanti/cg/index.shtml
# '''
#
#
# urlStr = re.findall(r'http?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str04)
#
# print(urlStr)




# d={1: 'a', 2: 'b'}
# b = {}
# for k,v in d.items():
#     b[v] = k
#
# d = b
# print(d)


print(eval("3+6+7+9"))

