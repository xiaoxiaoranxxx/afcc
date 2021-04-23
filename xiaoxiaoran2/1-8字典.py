# dictionary  {}  dict
dict1 = {}
dict2 = {'a': 'dsdefw', 'b': '333333', 'c': 'eeee'}
tuple1 = ((626, 33), (226, 425), (111, 33))
list1 = [[11, 11], [111, 33], [333, 999]]
dict3 = dict(tuple1)  # 转化必须成对出现
print(dict(list1))
print(dict3)
dict1['xiao'] = 'ran'  # 添加
print(dict1)
dict1['xiao'] = 'xiao'  # 同名则覆盖
print(dict1)
dict1['ddd'] = 'eee'
dict1['ttwe'] = 'fuwe'
print(dict1)
for i in dict2:
    print(i)
for i in dict2.items():
    print(i)
for key, value in dict2.items():
    print(key, value)
m = dict2.values()
n = dict2.keys()
print(m, '\n', n)
print('a' in dict2)   # 只能查key
print('eeee' in dict2)
print(dict2.get('a'))  # 找不到不会报错,可以自定义显示
print(dict2.get('a', 'xx'))
print(dict2.get('aa', 'xx'))
print(dict3.pop(111))  # 删除  根据key,
print(dict3.pop('dd', '999'))  # 找不到不会报错,可以自定义显示
print(dict3)
s = dict1.popitem()  # 删除末尾
s = dict1.clear()  # 清空
s = dict1.update(dict2)  # 合并
list2 = [1, 1, 1, 1, 1]
s = dict1.fromkeys(list2)  # 列表转换成字典
s = dict1.fromkeys(list2, 10,)
print(s)
