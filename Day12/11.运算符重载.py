class Person01(object):
    def __init__(self,num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num


    def __str__(self):
        return "str=" + str(self.num)



per1 = Person01(1)
per2 = Person01(2)

print(per1)
print(per2)

print(per1+per2)
