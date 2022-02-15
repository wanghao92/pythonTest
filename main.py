# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import math
import json
import glob
import doctest
import array

def print_hi(n):
    result = []
    a, b = 1, 2
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return  result

def f(n = 3) :
    n += 1
    print(n)

def fl(a, list = 'ab'):
    list += 'c'
    print(list)

def fun(*arguments, **keywords):
    for ar in arguments:
        print(ar)
    for key in keywords:
        print(key + ":" + keywords[key])

def combined_example(pos_only, /, standard, *cc, kwd_only):
    print(pos_only)
    print(standard)
    print(kwd_only)
    for c in cc:
        print(c)

def funJson() :
    f = open("ccc", 'w')
    p = {"a":"cc", "cc":123}
    print(p)
    print(json.dumps(p))
    json.dump(p, f)
    f.close()
    str = json.load(open("ccc", 'r'))
    print(str)

class ll:
    def __init__(self, data):
        self.data = data
        self.len = len(data)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.len == 0:
            raise Exception("data len is 0")
        elif self.index == self.len:
            raise StopIteration
        else :
            data = self.data[self.index]
            self.index += 1
            return data

def funOs():
    print(os.getcwd())
    print(dir())
    os.chdir('../')
    print(os.getcwd())
    print(os.system('dir'))

if __name__ == '__main__':
    funOs()
    l1 = ll('zxcvb')

    it = iter(l1)
    print(next(it))
    print('----------------')
    for ch in l1:
        print(ch)

    funJson()

    print(dir(os))
    print(str(1/7))
    print(repr(1/7))
    print("pi is {math.pi:.5f}")
    c1 = {'asdf':1, 'xddf':2}
    c2 = dict([('xx',1), ('as',2)])
    c3 = dict({'vvv':1, 'vvd':2})
    c4 = dict(asd= 1, cds = 2)
    print("xxx{asdf},{xddf}".format(**c1))
    for k, v in c1.items() :
        print(k , v)

    print("---------------")
    b1 = set('abcdef')
    b2 = {'asd', 'vvv'}
    print(b1)
    print(b2)
    for index, v in enumerate(b2):
        print(index, v)

    print("------------")
    a1 = [i for i in range(5)]
    a2 = [[i + j for i in range(4)] for j in range(5)]
    print(a1)
    print(a2)
    printF = print_hi
    print(printF(10))
    # fun("sss", "as", "xdfg", a="vxx", b="xsdf", c="xxx")

    combined_example(1, 2, 4, 4, 4, kwd_only = 3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
