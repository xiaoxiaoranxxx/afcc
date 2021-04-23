# set 不重复    可快速去除重复的并排序  随机放
s1 = set()
s2 = {1, 2, 3, 4, 5, 6, 8}
print(type(s2))
s2.add('www')  # 添加单个
s2.update(('qq', 'wwwwww'))  # 添加多个
s2.remove('qq')  # 没有会报错
s2.pop()  # 删第一个元素
s2.discard(2)  # 删时没有不会报错
print(s2)
s3 = {1, 3, 6, 'f', 'g'}
print(s2 & s3)  # 交集  intersection()
print(s2 | s3)  # 并集  union()
print(s2 ^ s3)  # 对称差集  symmetric_difference()
