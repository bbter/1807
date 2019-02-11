import doctest
'''
文档测试
'''
def get_result(a,b,c):
    '''

    :param a:
    :param b:
    :param c:
    :return:

    >>> print(get_result(2,3,5))
    11
    '''
    result = a+b+c
    return result

doctest.testmod()



















