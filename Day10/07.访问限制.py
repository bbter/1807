'''
访问限制
    保护数据的安全性
    不让用户随意访问我们的敏感数据
    对数据进行判断识别
操作方法
    私有化变量---有保护价值的变量私有化
    暴露一个公开的方法,外部可以通过这个方法访问和修改私有变量
    公开的方法要对操作数据的行为进行判断,防止肆意修改
    一般使用set和get方法对数据进行修改和访问
'''


class Bank(object):
    def __init__(self):
        self.__left = 10

    def save(self,money):
        self.__left += money


    def take(self,money):
        if self.__left >= money:
            self.__left -= money
        else:
            print("余额不足")

    def __str__(self):
        return "您的余额还有%s元" % self.__left

Lily = Bank()
# 并没有修改我们的数据,而是新建了一个新的变量,跟对象中原来的__left没有任何关系除了名字相同
Lily.__left = 1000
print(Lily)
print("*"*30)
Lily.save(1000)
print(Lily)
Lily.take(10000)
print(Lily)
