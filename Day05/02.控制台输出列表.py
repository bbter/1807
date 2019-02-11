'''

输出列表到控制台
      1.print直接输出
      2.for循环遍历
      3.while循环遍历
'''

name_list = ['张三','李四','王五','赵六','无啦']

for name in name_list:
    print(name)


i = 0
while i < len(name_list):
    print(i,name_list[i])
    i += 1


test_list1 = [2*x for x in range(51)]
print(test_list1)


# 生成器
test_list = (2*x for x in range(51))
print(test_list)
print(next(test_list))
print(next(test_list))
print(next(test_list))
print(next(test_list))



print(sum(x for x in range(1,101)))

for i in range(10):print(i)















