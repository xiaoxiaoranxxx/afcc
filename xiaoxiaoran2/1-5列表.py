names = ['a','b','c','d','e','r']
idsss = ['0','1','2','3','4','5']

#print(names[-1])
names[-1] = 'f'  #改
print(names[-3:])
print(names[-1::-1])
print(names[-1::-2])

for i in range(len(names)):  #寻找并改
    if 'e' in names[i]:
        names[i] = 'a'
        break

#del names[1]

i=0    #删除
w = 'a'
l = len(names)
while i < l:
    if w in names:
        del names[i]
        l-=1
        i-=1   #  or continue
    i+=1


print('----')     #输出
for n in names:
    print(n,'\t|')
    print('----')
print(names)

boys = ['aaa','bbb']    #循环输入
while True:
    name = input('请输入:')
    if name == 'quit':
        break
    boys.append(name)    #append追加字符串,extend列表合并 or 直接 +
    print(boys)

boys.insert(0,'xiao')    #指定位置插入
print(boys)






