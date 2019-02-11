import itertools
result = itertools.product(range(7), repeat=6)

count = 0
for i in result:

    str00 = ""
    for j in i:
        str00 += str(j)
    print(str00)
    count += 1
print(count)

