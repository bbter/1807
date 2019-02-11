'''
算术运算符
+   -   *   /    %     **     //
加  减  乘  除   取模  求幂   取整
'''

a = 10
b = 20
res1 = a + b
print(res1)

c = "hello"
d = "world"
res2 = c + d
print(res2)

# 不同类型的数据可能无法相加
res3 = str(a) + c
print(res3)

print(a - b)
print(a * b)
print(a / b)


e = 5
f = 2

print(e / f)
print(e // f)
print(e % f)
print(e ** f)


g = "1234"
print("这个数字的长度是%d" % len(g))
g = int(g)
ge = g % 10
shi = g // 10 % 10
bai = g // 100 % 10
qian = g // 1000
print(qian,bai,shi,ge)










































