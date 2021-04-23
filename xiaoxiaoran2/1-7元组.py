# tuple  () 里面只有一个是 = 没有  元组有只读属性
import random
ll = []
for i in range(10):
    ran = random.randint(1, 1000)
    ll.append(ran)
print(ll)
s = tuple(ll)
print(s)
print(s[1:3])  # 报前不包后
print(sum(s))
# print(s.count(2))  #下标位置
# print(s.index(2))  #个数
t1 = (1, 2, 3)  # 拆包和装包
a, s, q = t1  # 必须一一对应,不然报错
print(a)
t1 = (1, 2, 3, 4, 5, 6, 7)
a, *e = t1
print(a, e)  # 单e转列表
print(a, *e)  # 直转
