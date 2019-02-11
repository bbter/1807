'''
元组的元素有下标,可以通过下标访问指定位置的元素，
元素可迭代,可以使用for或者while遍历

'''


tuple00 = (123, "list", True, [1, 2, 3])

print(tuple00[0])

for i in tuple00:
    print(i)

i = 0
while i < len(tuple00):
    print(tuple00[i])
    i += 1









