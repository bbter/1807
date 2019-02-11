'''

可以交换的调试模块
'''

import pdb

def add2num(a,b):
    pdb.set_trace()
    c = a + b
    return c

add2num(3,5)






