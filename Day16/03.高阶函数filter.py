result = filter(None,[True,False])
print(result)
print(next(result))


def get_reslut(i):
    if i % 2 == 0:
        return True
    else:
        return False

# result = filter(get_reslut,range(101))
# for i in result:
#     print(i,end="\t")

result = filter(lambda x:x % 2 == 0,range(101))
for i in result:
    print(i,end="\t")


# dict_student = [{"张三":20},{"张四":12},{"张五":22},{"张六":60}]

# filter(lambda x)















