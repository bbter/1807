from functools import reduce

result = map(str, [1, 2, 3, 4])
for i in result:
    print(i, type(i))

print((str([1, 2, 3])))

result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

print(result)

result = filter(lambda x: x % 2 == 0, range(101))

print(result)
# for i in result:
#     print(i)

list01 = [1, 34, 57654, 5, 235]

for i in range(len(list01)-1, 0, -1):
    max_index = 0
    for j in range(1, i + 1):
        if list01[max_index] < list01[j]:
            max_index = j
    list01[max_index], list01[j] = list01[j], list01[max_index]

print(list01)


list01 = [1, 34, 57654, 5, 235]
for i in range(len(list01)-1):
    for j in range(0, len(list01)-1-i):
        if list01[j] > list01[j+1]:
            list01[j], list01[j+1] = list01[j+1], list01[j]


print(list01)
