'''

不定长参数**kwargs
    传入参数时,先满足name，剩余正常格式的参数给*args,关键字参数给**kwargs

    定义不定长参数时,需要把arg放在前面 *args 放在第二位, **kwargs放最后
'''

def show(name,*args,**kwargs):
    print(name)
    print(args)
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,":",v)


show("张三",18,13868864676,"zhangsan@163.com",x=1)



'''
姓名
**性别
**年龄
*名族
*政治面貌
**学历
**毕业院校
**手机号码
**邮箱
'''
show('白炳钿',"汉族","团员",学历="专科",毕业院校="浙江邮电职业技术学院",手机号码=13868864676,email='1035675608@qq.com')









