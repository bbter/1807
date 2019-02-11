def get_result(*args):
    '''
    :param args:
    :return:
    '''
    result = 0
    for a in args:
        result += a
    return result


# 调用测试的代码,只能在本模块中运行时会执行if中的内容,如果是其他模块调用本模块,if条件不成立
if __name__ == '__main__':
    print(get_result(1,2,3,4,5))