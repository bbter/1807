'''
递归:
    在函数内部调用本函数



'''


def multiplication_table(n):
    if n < 1:
        return
    multiplication_table(n - 1)
    for m in range(1, n + 1):
        print("%d * %d = %d" % (m, n, m * n), end="\t")
    print()

multiplication_table(9)













