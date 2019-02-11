'''
type创建带方法的类
    普通方法
        参数列表中至少有一个参数:self
    静态方法
        需要使用@staticmethod修饰,参数列表可以为空
    类方法
        参数列表至少需要一个参数,需要使用@classmethod修饰,
'''



def show09(self):
    print("demo09")

@staticmethod
def show10():
    print("demo10")

@classmethod
def show11(cls):
    print("demo11")


Demo09 = type("Demo09",(object,),{"demo09":show09,"demo10":show10,"demo11":show11})

help(Demo09)

Demo10 = type("Demo10",(object,),{"show10":show10})


# help(Demo10)

Demo10.show10()

demo10 = Demo10()
demo10.show10()


Demo11 = type("Demo11",(object,),{"show11":show11})
Demo11.show11()
# help(Demo11)

