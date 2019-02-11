def get_mul(*args):
    '''
    获取任意个数乘积
    :param args:
    :return:
    '''
    result = 1
    for a in args:
        result *= a
    return result


