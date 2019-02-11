#
# def leap_year(years):
#     if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0):
#         return True
#     else:
#         return False
#
#
# year_list = [2008,1000,6666,2012,2004,2000,1998,1996]
#
# reslut = filter(leap_year,year_list)
# for i in reslut:
#     print(i)


# print(list(map(lambda x:x ** 2,range(10))))


dict = {"a": 1, "b": 3, "c": 5, "d": 6, "e": 3, "f": 2}

# print(sorted(dict.items(),key=lambda item:item[1]))


def xuanze(list01):
    for i in range(len(list01) - 1, 0, -1):
        # 假设最大元素的下标为0
        max_index = 0
        # print(i)
        # 把最大的元素和所有位排序的元素比较
        for j in range(1, i + 1):
            if list01[max_index] < list01[j]:
                max_index = j
        # print(j)
        list01[max_index], list01[j] = list01[j], list01[max_index]
    return list01
#
# list00 = [45,67,98,34,32,56,243]
# print(xuanze(list00))


# def maopao(list02):
#     for i in range(0, len(list02) - 1):
#         for j in range(0, len(list02) - 1):
#             if list02[j] > list02[j + 1]:
#                 list02[j], list02[j + 1] = list02[j + 1], list02[j]
#     return list02
#
# print(maopao(list00))