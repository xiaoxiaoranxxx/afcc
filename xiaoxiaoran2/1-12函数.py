import random


def sss():  # 生成随机数
    for i in range(9):
        ra = random.randint(1, 20)
        ran.append(ra)
    print('产生9个1-20的随机数:', ran)


ran = []
sss()


def ss(n):
    for i in range(n):
        raq = random.randint(1, 20)
        xiao.append(raq)
    print('产生', n, '个随机数为:', xiao)


xiao = []
ss(2)


def s(a, b):
    ee = a+b
    print('这两个数的和为:', ee)


s(1, 22)
print(sss)


def gg(name, *msf):  # 可变参数与不可变
    sum = 0
    if len(msf) > 0:
        for i in msf:
            sum += i
        print('合为:', sum)
        print('max = ', max(msf))
        print(name)
    else:
        print('none')


gg('肖萧然最秀', 123, 111, 3344, 5436, 745, 2)


def rrr(a, b=10):  # 关键字参数
    print(a+b)


rrr(4)
rrr(4, 1)
rrr(1, b=1)
print('------------>')


def fff(**dddp):  # 转字典  拆包
    print(dddp)


fff(a=1, b=2, c=3)
print('----------->')


def ww(a, b, *c, **d):  # 关键字
    print(a, b, c, d)


ww(1, 2)
ww(1, 2, 3, 4)
ww(1, 2, 3, 4, 5, 6, c='eee')


def fun1(name, *xxx):
    for i in xxx:
        print('{}准备{}秀'.format(name, i))


couse = ['q1', 'q2', 'q3']
fun1('肖萧然', couse)
fun1('肖萧然', *couse)


def aaad(a, b):
    syy = a + b
    print(syy)         # 利用函数中的的值,不返回外部是不能够用的,print仅仅在终端上
    return 'syy', '1', '2'  # 函数的返回值


aaad(1, 2)
xiu = aaad(222, 3)  # 返回值必须接
print(xiu)

# 相套套调用函数
islogin = False


def add_shopping(goodsname):  # 添加刀购物车
    global islogin
    if islogin:
        if goodsname:
            print('成功将{}加入'.format(goodsname))
        else:
            print('没有选中商品')
    else:
        print('没有登录')
        answer = input('是否登录(y/n)')
        if answer == 'y':
            islogin = login('xaio', 'xiao')  # 调别的
            add_shopping('xiaoxiaoxiao')  # 调自己
        else:
            print('未能添加...')


def login(usersname, password):
    if usersname == 'xaio' and password == 'xiao':
        print('ok')
        return True
    else:
        print('nono')
        return False


#a = input('username')
#b = input('password')
a = 'xaio'
b = 'xiao'

islogin = login(a, b)
add_shopping('xiaoxiaoxiao')


def grr_checkcode(n):
    s = '12345678asdfghjklzxcvbnmwertyu90asdfghjkl'
    code2 = ''
    for i in range(n):
        ran1 = random.randint(0, len(s)-1)
        code2 += s[ran1]
    return code2


def login1():
    username = input('username:')
    password = input('password:')
    code = grr_checkcode(5)
    print('check-------->', code)
    cdde = input('cccccccc:')
    if code.lower() == cdde.lower():
        print('ok')
        if username == '1' and password == '1':
            print('okok')
        else:
            print('vvvvvvvvv')
    else:
        print('ooooooooo')


# login1()









