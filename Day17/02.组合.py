import itertools
result = itertools.combinations("abcde", 3)
count = 0
for i in result:
    print(i)
    count += 1
print(count)
