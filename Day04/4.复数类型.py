'''
复数类型
        在Python中理解为常量和变量的组合
        在Pyhton中虚数部分只能使用XXj，否则会报错 SyntaxError: invalid syntax，比如k  = 123j + 45


'''

k  = 123j + 45
print(k)

print(k.imag)
print(k.real)




