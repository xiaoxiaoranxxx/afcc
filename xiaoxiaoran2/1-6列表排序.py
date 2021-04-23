import random
random_list = []
i=0
while i<10 :
    ran = random.randint(1,1000)
    if ran not in random_list:
        random_list.append(ran)
        i+=1
print(random_list)
print('这最小的是:',min(random_list))
maxx = random_list[0]
for v in random_list:
    if v > maxx:
        maxx = v
print('这最大的是:',maxx)
print(sorted(random_list))  #升序
print(sorted(random_list,reverse=True))
s = 'x' * 10
ss = list(s)
ss.remove('x')   #删除第一次出现的,找不到会报错
ss.pop()   #默认删除最后一个,可以根据下标删
print(ss)   #clear 清楚列表









