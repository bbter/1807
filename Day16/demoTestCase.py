'''
单元测试
    1.导入模块 unittest
    2.创建测试类Test ,继承unittest,TestCase
    3.编写测试方法
    4.验证目标类中的参数是否正确
'''
import unittest

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def setAge(self,age):
        self.age = age

    def getAge(self):
        return self.age



class Test(unittest.TestCase):
    def test_init(self):
        xiaoming = Person("小明",28)
        self.assertEqual(xiaoming.age,28,"年龄有误")




if __name__ == '__main__':
    unittest








