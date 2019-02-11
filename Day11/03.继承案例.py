class School(object):
    # 定义学校人数
    schoolNum = 0
    def __init__(self,name):
        self.name = name
        # 学校总人数增加1
        School.schoolNum += 1
        print("新来一个成员:%s,学校目前有:%d人" % (self.name,School.schoolNum))

    def say_hello(self):
        print("大家好,我是新来的渣渣辉")


class Stu(School):
    def __init__(self,name,score):
        School.__init__(self,name)
        self.score = score

    def say_hello(self):
        print("我是新来的学员%s,现在的成绩是%d" % (self.name,self.score))


class Teacher(School):
    pass


sto01 = Stu("张三",100)
sto01.say_hello()




