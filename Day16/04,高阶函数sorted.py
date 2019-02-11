list00 = [1,2,3,4,5,6,2,4,8,9,8]

print(sorted(list00))


class Student(object):
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    # def __str__(self):
    #     return "%s,%s,%s" % (self.name,self.age,self.hobby)

    def __repr__(self):
        return repr((self.name,self.age,self.hobby,))


students_list = [Student("John",18,"抽烟"),Student("David",38,"喝酒"),Student("Jone",17,"抽烟")]

print(sorted(students_list,key=lambda s:s.age))











