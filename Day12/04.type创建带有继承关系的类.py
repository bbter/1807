'''
type创建带有继承关系的类
'''


class Demo06(object):
    def __init__(self):
        self.j = "jjj"
        self.k = "kkk"

    def demo06(self):
        print("demo06")


class Demo08(object):
    def __init__(self):
        self.n = "nnn"
        self.o = "ooo"

    def showP(self):
        print("demo08")



Demo07 = type("Demo07",(Demo06,),{"m":"mmm"})

demo07 = Demo07()
print(demo07.j)
print(demo07.k)
print(demo07.m)


Demo09 = type("Demo09",(Demo06,Demo08),{"m":"mmm"})


demo09 = Demo09()
print(demo09.j)
print(demo09.k)
print(demo09.m)
# print(demo09.n)
# print(demo09.o)



