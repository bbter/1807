import datetime
import time
# help(datetime)
now = datetime.datetime.now()

print(datetime.datetime.time(now))
print(datetime.datetime.ctime(now))

# 获取当前时间
print(datetime.datetime.now())
print(type(now))

# 获取当前时间
print(datetime.datetime.today())
# 格林尼治天文时间，和我们时间差8个小时
print(datetime.datetime.utcnow())