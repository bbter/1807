from functools import partial

def productGlass(x,time):
    total_time = x * time
    return str(total_time) + "小时"



p2 = partial(productGlass,time=2.5)
print(p2(2))



def builtWheels(name):
    return "%s在造轮子" % name

def bultaCarBody(name):
    return "%s在造车身" % name


def leader(func,name):

    return func(name)


print(leader(builtWheels,"bbt"))




def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n-1)

print(sum2(101))


# import os
#
# q = []
#
#
# def get_all_files(path,sp=""):
#     files_list = os.listdir(path)
#     sp += "  "
#     for files in files_list:
#         abspath = os.path.join(path,files)
#         if os.path.isdir(abspath):
#             get_all_files(abspath)
#         q.append(path)
#
# get_all_files(r"E:\培训记录")
# lenth = len(q)
#
# for i in range(lenth):
#     print(q.pop(0)
















#
def sum_recu(n,result):
    if n > 1:
        if n % 2 == 0:
            result += n
        return sum_recu(n-1,result)
    else:
        print("reslut",result)
        return result

print(sum_recu(5,0))


#
# def sum_recu(n):
#     if n>0:
#         if n % 2 == 0:
#            return n +sum_recu(n-1)
#         else:
#             return sum_recu(n-1)
#     else:
#        return 0

# print(sum_recu(100))