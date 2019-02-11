'''
偏函数

'''

def add2num(a,b):
    return a+b


from functools import partial
add2 = partial(add2num,3)


print(add2(9))


print(map(str,[1,2,3,4]))


result = map(str,[1,2,3,4])


from collections import Iterator,Iterable
print(isinstance(result,Iterator))
print(isinstance(result,Iterable))

print(next(result))
print(next(result))
print(next(result))
print(next(result))
# print(next(result))



result = print(map(int,"hello"))
print(result)




def strToNum(chr):
    return {"123":123,"456":456,"789":789}[chr]



print(map(strToNum,["123","456","789"]))
result1 = map(strToNum,["123","456","789"])
print(next(result1))



