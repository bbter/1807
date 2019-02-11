'''
type创建带有__init__()的类
'''

def __init__(self,r):
    self.r = r
    self.s = "sss"


Demo12 = type("Demo12",(object,),{"__init__":__init__})

demo12 = Demo12("RRR")
print(demo12.r)





