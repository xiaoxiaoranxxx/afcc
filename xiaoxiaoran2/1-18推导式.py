#列表
names = ['1wwww', 'e', 'rrrddd', 'eee', 'etwf', 'wef']
print([name for name in names if len(name) > 3])
print([name.capitalize() for name in names if len(name) > 3])
print([i+1 for i in range(1, 20) if i % 3 == 0])
list2 = [i for i in range(1, 11)]
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 != 0])
dict1 = {'a':'a1','salary':11234}
dict2 = {'a':'a2','salary':12234}
dict3 = {'a':'a3','salary':12344}
dict4 = {'a':'a4','salary':1234}
list1 = [dict1,dict2,dict3,dict4]
print([employee['salary']-10000 if employee['salary'] > 5000 else employee['salary']+22222 for employee in list1])
#集合
print({x for x in list2 if x > 5})

#生成器  generator
g = (x*3 for x in range(20))  #多调会报错...
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(next(g))
print()

rg = (x*3 for x in range(10))  
while True:
    try:
        e = next(rg)
        print(e)
    except:
        break

def func():
    n=0
    while True:
        n +=1
        yield n   #关键字类似return 并暂停
g = func()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('-------->')
#兔子数列
def fib(length):
    a,b = 0,1
    n=0
    while n <length:
        #print(b)
        yield b
        a,b = b,a+b
        n +=1
    return '------------ddd'
g = fib(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def gen():
    i=0
    while i<6:
        temp = yield i
        print('temp',temp)
        i+=1
g = gen()
print(g.send(None))
n1 = g.send('ee')
print('n1',n1)
n2 = g.send('dd')
print('n2',n2)
#多线程
def task1(n):
    for i in range(n):
        print('>>>>>>>>{}'.format(i))
        yield None
def task2(n):
    for i in range(n):
        print('<<<<<<<<{}'.format(i))
        yield None

g1 = task1(5)
g2 = task2(5)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break

from collections import Iterable
print(isinstance(list2,Iterable))
list2 = iter(list2)  #转换成迭代器
print(next(list2))
print(next(list2))


