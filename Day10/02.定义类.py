'''
定义类:
    class 类名():
        参数列表
        方法列表

    类名使用大驼峰命名法
'''

class Car(object):
    '''
    @:param wheel 轮子
    @:param color 颜色
    @:return None
    '''
    wheel = 4
    color = "white"

    def run(self):
        print("这辆车有%d个轮子,跑的时候四驱" % self.wheel)


QQ = Car()
print(QQ.wheel)
print(QQ.color)
print(id(QQ.color))
QQ.run()

# 创建对象的新属性
QQ.color = "黑色"
QQ.wheel = 6
print(QQ.wheel)
print(QQ.color)
print(id(QQ.color))
QQ.run()



Q7 = Car()
print(Q7.wheel)
print(Q7.color)
Q7.run()




