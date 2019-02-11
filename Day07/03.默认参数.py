'''
默认参数----》缺省参数
'''
def show(name,age=18):
    print("刚刚来报道的这个学生名字是%s,年龄是%d" % (name,age))

show("张三",age=19)


show("李斯")



# 如果参数列表中同时存在默认参数和普通形参,默认参数必须定义在普通形参之后
def sing(name,voice=60):
    print("%s唱歌的时候音量大概是%d分贝" % (name,voice))


sing("Lucy")