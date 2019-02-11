class ShortInputException(Exception):
    def __init__(self,length):
        self.length = length
        self.atleast = 6


    def __str__(self):
        return "ShortInputException:最小长度要求是6,您输入的是%d" % self.length



try:
    pwd = input("请输入密码:")
    if len(pwd) < 6:
        # raise 抛出异常
        raise ShortInputException(len(pwd))
except ShortInputException as e:
    print(e)
else:
    print("密码长度合法")



































