import itertools

result = itertools.permutations("hello")
print(result)
count = 0
for i in result:
    print(i)
    count += 1
print(count)

result = itertools.combinations("abcde", 3)
count = 0
for i in result:
    print(i)
    count += 1
    print(count)
print("*" * 20)

result = itertools.product("abcde", repeat=3)
print(result)
count = 0
for i in result:
    print(i)
    count += 1
print(count)
print("*" * 20)
