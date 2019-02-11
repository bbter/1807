'''
运行中删除属性的方法
    del x.y
    delattr(o,str)   ===> del x,y


'''

class Demo19(object):
    pass
    def show19(self):
        print("show19")

def __init__(self):
    self.a = 110
    self.b = 120
    self.c = 119

# help(Demo19)


Demo19.__init__ = __init__
help(Demo19)


demo19 = Demo19()
print(demo19.a)
print(demo19.b)
print(demo19.c)


demo19.d = 12315
print(demo19.d)


del demo19.d
# print(demo19.d)
# print(Demo19.d)

#
delattr(demo19,"a")
# print(demo19.a)


demo19.show19()


# del Demo19.show19


# demo19.show19()


# delattr(Demo19,"show19")
# demo19.show19()



