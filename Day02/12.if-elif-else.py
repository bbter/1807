'''

假设是学校的课程表
'''

# day = int(input("今天星期几?"))
'''
if day == 1:
    print("体育课")
if day == 2:
    print("编程课")
if day == 3:
    print("上机课")
if day == 4:
    print("今天休息")
if day == 5:
    print("影视鉴赏")
if day == 6 or day == 7:
    print("玩去吧")
'''
# if day == 1:
#     print("体育课")
# elif day == 2:
#     print("编程课")
# elif day == 3:
#     print("上机课")
# elif day == 4:
#     print("今天休息")
# elif day == 5:
#     print("影视鉴赏")
# elif day == 6 or day == 7:
#     print("玩去吧")
# else:
#     print("您的输入有误")


'''
优秀 > 90
良好 > 80
一般 > 70
及格 > 60
不及格 <60

'''

grade = int(input("请输入你的成绩:"))
if grade < 0:
    print("您的输入有误")
elif grade < 60 :
    print("不及格")
elif grade < 70:
    print("及格")
elif grade < 80:
    print("一般")
elif grade < 90:
    print("良好")
elif grade <= 120:
    print("优秀")
else:
    print("您的输入有误")








