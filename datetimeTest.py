from datetime import datetime
import time


SECOND_PER_DAY = 24 * 3600

def fun1():
    d1 = datetime.now()
    d2 = datetime(2020, 2, 16, 23, 15, 0)
    d3 = (d1 - d2).seconds
    print(d3)

    span = time.mktime(d1.timetuple())     #转时间戳
    print(span)

def fun2() :
    d = datetime(2022, 2, 16, 23, 15, 0)
    d1 = d.year
    d2 = d.month
    d3 = d.day
    d4 = d.hour
    d5 = d.minute
    d6 = d.second
    print("year:{}, mon:{}, day:{}, hour:{}, min:{}, sec:{}", d1, d2, d3, d4, d5, d6)

def fun3():
    t = time.time()
    print(t)  # 原始时间数据
    print(int(t))  # 秒级时间戳
    print(int(round(t * 1000)))  # 毫秒级时间戳

if __name__ == "__main__":
    fun1()