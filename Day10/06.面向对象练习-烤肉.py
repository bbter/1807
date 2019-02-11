class CookBeef(object):
    def __init__(self):
        # 几成熟
        self.cook_level = 0
        # 文字描述
        self.cook_string = "生的"
        # 佐料
        self.condiments = []

    # 烤制的方法，可以传入时间,每一分钟相当于一成熟
    def cook(self,cook_time):
        self.cook_level += cook_time
        # 根据cook_level的数值,改变cook_string的描述信息
        if self.cook_level <= 3:
            self.cook_string = "还在滴血,特别新鲜"
        elif self.cook_level <= 5:
            self.cook_string = "表明熟啦,里面还是生的"
        elif self.cook_level <= 8:
            self.cook_string = "可以吃了,烤制的刚刚好"
        elif self.cook_level < 10:
            self.cook_string = "马上就烤焦了"
        else:
            self.cook_string = "扔了吧,都焦了"

    # 添加佐料的方法
    def add_condiments(self,condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return "已经烤制了%s分钟,现在是%s,添加的佐料有%s" % (self.cook_level,self.cook_string,self.condiments)


# 创建对象
hui_ling_dun = CookBeef()
print(hui_ling_dun)

# 添加佐料
hui_ling_dun.add_condiments("黄油")
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.add_condiments("盐")
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)