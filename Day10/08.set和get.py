class Person(object):
    def __init__(self,name):
        self.name = name
        self.__age = 0


    def setAge(self,age):
        if age >0 and age < 130:
            self.__age = age
        else:
            self.__age = -1


    def getAge(self):
        return self.__age


    def __str__(self):
        return "这个人的名字是%s，年龄是%d" %(self.name,self.__age)

LaoWang = Person("老王")
LaoWang.setAge(110)
print(LaoWang)

print(LaoWang.getAge())