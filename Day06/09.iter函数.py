'''

iter()函数
'''

# iter()
num00 = 12345
str00 = "hello"
list00 = [1,2,3,4,5]
tuple00 = (1,2,3,4,5)
dict00 = {1:1,2:2,3:3}
set00 = {1,2,3,4,5}
print(str00)
str01 = iter(str00)
print(str01)
print(next(str01))
print(next(str01))
print(next(str01))



from collections import Iterator,Iterable

print(isinstance(str01,Iterable))
print(isinstance(str01,Iterator))

# num01 = iter(num00)
# print(num01)


