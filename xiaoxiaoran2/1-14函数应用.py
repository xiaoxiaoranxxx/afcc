# 递归函数   自己调自己 recursion
from functools import reduce
import time


def f1(n):
    if n >= 0:
        print('---------->', n)
        f1(n-1)


f1(5)


def sum(n):  # 求前n项和
    if n == 0:
        return 0
    else:
        return n + sum(n-1)


result = sum(100)
print(result)

islogin = True


def login():
    username = input('username=')
    password = input('password=')
    if username == '1' and password == '1':
        return True
    else:
        return False


def login_require(func):
    def wrapper(*args, **kwargs):
        global islogin
        print('----------->')
        if islogin:
            func(*args, **kwargs)
        else:
            print('没有登录...')
            islogin = login()
            print('结果:', islogin)
    return wrapper


@login_require
def pay(money):
    print('付款金额:{}元'.format(money))
    print('正在付款中....')
    time.sleep(2)
    print('付款完成!')


pay(1000)
pay(100000)
pay(888)


# 变量的作用域
# local  局部变量
# encloseing 嵌套
#global 全局
# built-in 内置


# 匿名函数
def s(a, b): return (a+b)*33+(a-b)/6


rrr = s(222, 44)
print(rrr)

# 匿名函数作为参数


def func(a, b, c):
    print(a, b)
    print(c)
    s = c(a, b)
    print(s)


func(1, 2, lambda x, y: x+y)

# 匿名函数与内置函数
list1 = [{'a': 12, 'b': 13}, {'a': 44, 'b': 22}, {'a': 23, 'b': 2}]
m = max(list1, key=lambda x: x['b'])
print(m)

list2 = [1, 2, 34, 5, 6, 7, 67, 6, 5, 32, 23, 36, 635]
resul = map(lambda x: x+2, list2)
print(list(resul))

def funr(x): return x if x % 2 == 0 else 0


result = funr(4)
print(result)
result1 = map(lambda x: x if x % 2 == 0 else 0, list2)
print(list(result1))

tuple1 = (1, 2, 31, 34, 67, 4)
result2 = reduce(lambda x, y: x+y, tuple1)  # 没有是null
print(result2)  # 和

result = filter(lambda x: x > 10, list2)
print(list(result))



