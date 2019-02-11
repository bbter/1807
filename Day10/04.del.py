'''
__del__
    析构方法(函数)

    作用
        删除一个对象时会自动调用
'''



class Truck(object):
    def __init__(self,weight,speed):
        self.weight = weight
        self.speed = speed

    def show(self):
        print("刚刚看到一辆卡车,载重%d吨,时速%d" %(self.weight,self.speed))


    def __del__(self):
        print("%s被删除了" % self)


JieFang = Truck(10,100)
JieFang.show()
del JieFang
print("hello")


DongFeng = Truck(30,120)
DongFeng.show()
print("world")




