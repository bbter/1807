'''
property
    属性--》保护属性

'''

class Demo20(object):
    def __init__(self):
        self.__age = 0

    def setAge(self,age):
        if (age > 0) and (age < 130):
            self.__age = age
        else:
            self.__age = -1

    def getAge(self):
        return self.__age


demo20 = Demo20()
demo20.setAge(18)
print(demo20.getAge())

# 这种方式相当于动态的创建了一个属性,和__age没有任何关系

demo20.age = 200
print(demo20.age)


class Demo21(object):
    def __init__(self):
        self.__count = 0


    @property
    def count(self):
        print("property执行了")
        return self.__count


    @count.setter
    def count(self,value):
        print("setter执行了")
        if (value > 0) and (value < 130):
            self.__count = value
        else:
            self.__count = -1

    @count.getter
    def count(self):
        print("getter执行了")
        return self.__count



demo21 = Demo21()
print(demo21.count)
demo21.count = 100
print(demo21.count)
demo21.count = 130
print(demo21.count)