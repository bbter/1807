import itertools

# help(itertools)
result = itertools.permutations([1, 2, 3, 4])
print(result)
count = 0
for i in result:
    print(i)
    count += 1
print(count)

result = itertools.permutations("abcd", 1)
count = 0
for i in result:
    print(i)
    count += 1
print(count)
