import logging

# 设置显示日志等级
logging.basicConfig(level=logging.INFO)

def get_result(a, b):

    logging.info("a=%d,b=%d" % (a, b))
    c = a + b
    return c

print(get_result(3,5))


logging.basicConfig(level=logging.WARNING)

def get_result(a, b):

    logging.warning("a=%d,b=%d" % (a, b))
    c = a + b
    return c

print(get_result(3,5))











