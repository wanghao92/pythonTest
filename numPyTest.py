import numpy as np
from matplotlib import pyplot as plt

def fun1():
    print(np.arange(15))    #0~14的一维数组
    print(np.arange(5, 16))     #5~15的一维数组
    print(np.arange(10, 30, 3)) #10<= <30，间隔3的一维数组
    print(np.linspace(0, 2))    #0~2的等差数组，默认50个点
    a = np.arange(15).reshape(3, 5)
    print(a)
    print(a.shape)
    print(a.size)
    print(a.ndim)
    print(a.dtype)
    print(type(a))
    print(np.floor(1.5))
    print(np.random.random((2, 5)))
    np.set_printoptions(threshold=np.inf)

#数组堆叠
#vstack,hstack,column_stack,row_stack
def fun2():
    a = np.array([2, 4, 6])
    b = np.array([3, 5, 7])
    print("vstack:\n{}".format(np.vstack((a, b))))
    print("hstack:\n{}".format(np.hstack((a, b))))
    print("column_stack:\n{}".format(np.column_stack((a, b))))
    print("row_stack:\n{}".format(np.row_stack((a, b))))

    a = np.array([[2, 4, 6],
                 [8, 10, 12]])
    b = np.array([[3, 5, 7],
                 [9, 11, 13]])
    print("vstack:\n{}".format(np.vstack((a,b))))
    print("hstack:\n{}".format(np.hstack((a,b))))
    print("column_stack:\n{}".format(np.column_stack((a, b))))
    print("row_stack:\n{}".format(np.row_stack((a, b))))

#数组分割
#hsplit,vsplit
def fun3():
    a = np.floor(10 * np.random.random((2, 12)))
    print(a)
    print("hsplit:\n{}".format(np.hsplit(a, 3)))  # Split a into 3
    print("hsplit:\n{}".format(np.hsplit(a, (3, 4))))  # Split a after the third and the fourth column

#拷贝
# = view copy
def fun4():
    a= np.array([[3, 4, 5],
                [6, 7, 8]])

    b = a
    print("a id:{}, b id:{} b is a:{}".format(id(a), id(b), b is a))
    print("a.reshape id:{},b.resharpe id:{}".format(id(a.reshape(1, 6)), id(b.reshape(1,6 ))))

    c = a.view()
    print("a id:{}, c id:{} c is a:{}".format(id(a), id(c), c is a))
    print("a id:{}, c.base id:{} c.base is a:{}".format(id(a), id(c.base), c.base is a))
    print("a.reshape id:{},c.resharpe id:{}".format(id(a.reshape(1, 6)), id(c.reshape(1, 6))))

    c[0,0] = 0
    print(a)

    d = a.copy()
    print("a id:{}, d id:{} c is a:{}".format(id(a), id(d), d is a))
    print("a id:{}, d.base id:{} c.base is a:{}".format(id(a), id(d.base), d.base is a))
    print("a.reshape id:{},d.resharpe id:{}".format(id(a.reshape(1, 6)), id(d.reshape(1, 6))))

    d[1, 0] = 0
    print(a)

#使用索引数组进行索引
def fun5():
    a = np.arange(-5, 15, 1)
    print(a)
    b = np.array([1, 3, 5 ,6])
    print("a[b]:\n{}".format(a[b]))
    c = np.array([[1, 3], [9, 10]])
    print("a[c]:\n{}".format(a[c]))

    #当索引数组是多维的时，单个索引数组指的是第一个维度
    d = np.array([[1,2,3,4],
                  [-1,-2,-3,4],
                  [5,6,7,8],
                  [-5,-6,-7,-8]])

    e = np.array([[0,0,3,2,1],
                 [3,3,2,0,1]])
    print("f[e]:\n{}".format(d[e]))

    #为多个维度提供索引。每个维度的索引数组必须具有相同的形状
    f = np.array([[1,1,2,3,1],
                 [1,2,3,0,1]])
    print("f[e, f]:\n{}".format(d[e,f]))

#使用布尔数组进行索引
def fun6():
    a = np.arange(15).reshape(3, 5)
    b = a > 4
    print(b)
    print()

    print(a[b])
    print()

    a[b] = 0
    print(a)


def mandelbrot( h,w, maxit=20 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]

    c = x+y*1j
    # print(c)
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)


    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2            # who is diverging
        div_now = diverge & (divtime==maxit)  # who is diverging now
        divtime[div_now] = i                  # note when
        z[diverge] = 2                        # avoid diverging too much

    return divtime

def fun7():
    plt.imshow(mandelbrot(400, 400))
    plt.show()

#ix_()
def fun8():
    a = np.array([1,2,3])
    ax, ay, az, aa = np.ix_(a, a, a, a)
    print(ax)
    print(ay)
    print(az)
    print(aa)

#newaxis
def fun9():
    a = np.arange(15).reshape(3, 5)
    print(a)
    b = a[:,np.newaxis,:]
    print(b)
    c = a[np.newaxis, :, :]
    print(c)
    d = a[:, :, np.newaxis]
    print(d)

    x = np.arange(5)

    y = x[:, np.newaxis]
    z = x[np.newaxis, :]
    print("X.shape:{}, y.shape:{}, z.shape:{}".format(x.shape, y.shape, z.shape))

    xx =  y + z
    print(xx.shape)
    print(xx)
if __name__ == "__main__" :

    fun1()