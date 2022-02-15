from datetime import datetime

def fun1():
    d1 = datetime.now()
    d2 = datetime(2022, 2, 16, 23, 15, 0)
    d3 = (d1 - d2).seconds

    print(d3)

if __name__ == "__main__":
    fun1()