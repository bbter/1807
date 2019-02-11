'''

__init__
    构造方法(函数)
    作用
        初始化参数
    调用方式
        无需调用__init__,只需要在创建对象时使用类名(参数列表),就能完成自动调用
        参数列表中的参数会自动赋值给__init__方法中的形参
    注意
        这个方法是继承父类之后自动拥有,我们是重写这个方法
    重写
        发生在有继承关系的子类中
        子类继承父类,拥有父类非私有的属性和方法,
        如果子类使用继承自父类的方法不能满足自己的需求,
        可以重写父类的方法
            重写的方法和父类的名称保持一直
'''


class Bus(object):

    # 属性
    def __init__(self,wheel,color,speed):
        '''

        :param wheel:
        :param color:
        :param speed:
        '''
        self.wheel = wheel
        self.color = color
        self.speed = speed

    def show(self):
        print("这辆bus有%d个轮子,颜色是%s,能乘坐30人，最高能跑%dKM/H" %(self.wheel,self.color,self.speed))



BYD = Bus(6,"白色",120)
print(BYD)
print(Bus)
print(BYD.wheel)
print(BYD.color)
print(BYD.speed)
BYD.show()


print("*" * 40)

YuTong = Bus(10,"黄色",100)
print(YuTong)
print(Bus)
print(YuTong.wheel)
print(YuTong.color)
print(YuTong.speed)
YuTong.show()


print("*"*20)
# 把BYD在内存中指向的地址赠送给JingHua
JingHua = BYD
print(JingHua)
JingHua.show()
