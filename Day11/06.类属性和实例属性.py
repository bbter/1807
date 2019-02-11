'''
类属性
    类所拥有的属性
    调用
        类属性可以被类直接调用
        实例对象可以调用类属性
    修改
        类对象不能修改实例属性
        类对象可以修改类属性
实例属性
    属于实例对象的属性
    调用
        不能直接被类调用
        实例对象可以调用实例属性
    修改
        实例对象可以修改实例属性
        实例对象不能修改类属性

    如果实例属性和类属性重名
        实例对象在调用时优先使用实例属性
        类对象在调用时优先使用类属性
'''

class People(object):
    # 类属性
    country = "中国"
    province = "浙江"

    def __init__(self):
        # 实例属性
        self.city = "杭州"
        self.area = "江干区"
        self.province = "北京"




print(People.country)
# print(People.city)

print("*" * 30)

MaYun = People()
print(MaYun.country)
print(MaYun.province)
print(MaYun.city)


print("*" * 20)


MaYun.area  = "西湖区"
print(MaYun.area)

# 实例对象修改类属性

MaYun.province = "上海"
print(MaYun.province)
print(People.province)

print("*"*30)

# 类对象修改实例属性
People.city = "江干区"
print(People.city)
print(MaYun.area)


People.province = "上海"
print(People.province)
print(MaYun.province)



DingLei = People()
print(DingLei.province)
print(People.province)










