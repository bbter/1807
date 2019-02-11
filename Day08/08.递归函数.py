'''
递归
    函数内部调用自己
'''

# def show():
#     print("放飞自我")
#     show()
#
# show()

'''
5! = 5 * 4 * 3 * 2 * 1
   = 5 * 4!
   = 5 * 4 * 3!
   = 5 * 4 * 3 * 2!
   = 5 * 4 * 3 * 2  * 1!
=
   = f(n) * f(n-1)!
'''


result = 1
num = 5
while num > 0:
    result *= num
    num -= 1

print(result)


def get_mul(num):
    if num >=1:
        result = num * get_mul(num-1)
    else:
        result = 1
    return result

print(get_mul(5))


