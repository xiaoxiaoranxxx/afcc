import time


def func():
    n = 100
    list1 = [233, 22, 32, 34, 525]

    def iii():
        for index, i in enumerate(list1):
            list1[index] = i+5
        list1.sort()
    iii()
    print(list1)


func()

a = 1  # 变量的访问


def funa():
    b = 9
    b = 999

    def ffs():
        global a
        nonlocal b
        c = 22
        c += 1
        b += 1
        a += 1
        print(a, b, c)
    return ffs  # 外部调用内部函数


x = funa()
x()


def generate_count():  # 计数
    container = [0]

    def add_one():
        container[0] = container[0] + 1
        print('当前第{}次访问'.format(container[0]))
    return add_one


counter = generate_count()
counter()
counter()
counter()


def test():  # 巧了  装饰器 函数作为参数
    print('--------->test')


def funs(f):
    print(f)
    f()
    print('------------>func')


funs(test)

print()
print('-----------------------------')


def decorate(funcs):
    a = 100
    print('开始')

    def wrapper():
        funcs()
        print('大房')
    print('结束')
    return wrapper


@decorate
def house():
    print('小房子')
    print()


house()


def ggg(fundd):  # 装饰上效验
    def www(*ss):
        print('正在硝烟中..')
        time.sleep(1)
        print('完成...')
        fundd(*ss)
        fundd(*ss)
    return www


@ggg
def f1(n):
    print('---------->f1', n)


def f2():
    print('---------->f2')


f1(1010)
f2()


def desc(fuf):
    def wrrp(*aa, **bb):
        fuf()
        print('----------->xiu1')
    return wrrp


@desc
def hou():
    print('xiao+++0')


hou()

print()


def outer(a):  # 参数
    def decora(funj):  # 函数
        def wrpp(*ar, **b):  # 函数参数
            funj(*ar)
            print('------>铺地砖{}mm'.format(a))
        return wrpp
    return decora


@outer(10)
def hose(time):
    print('我{}日期老服务if哦...'.format(time))


@outer(100)
def street():
    print('新秀')


hose('xxxxx')
street()
