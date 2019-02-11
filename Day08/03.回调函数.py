'''
    函数当参数使用
'''


def cleanFloor(times):
    print("扫地执行了%d次" % times)


def changeSheets(times):
    print("换床单执行了%d次" % times)


def server(times,func):
    return func(times)

server(2,cleanFloor)

# cleanFloor(2)
# changeSheets(2)



