a = 123
b = 1.1234
c = '肖萧然最秀'
N = 'ssss'
# 大写的字母是常量

print(type(a), type(b), type(c), sep='**')
print('xiao\nxiao\nxiao')
print('xiao', end='55')
print(a)
print(N)
print(r'hello\pf\th')
print()
print()

# 得到不转
xiao = '''
qqq
qqqq
qqqqqq
'''
# '''xxx'''保证样式输出
print(xiao)
print('没错!'+c)
#使用加号格式必须相同

print('第一:%s,第二:%s' % (a, c))
print('小小:%.2f' % b)
# %s是占位的 字符串   %d是数字取整
# %f   %.1f  保留小数位

print(str(a)+c)
# 格式强制转化

xiao1 = '''
aaaaa: %s
bbbbbb:%d
cccccccccc:%.3f
''' % (a, b, b)
print(xiao1)

xiao2 = '肖萧然今年{}睡{}了'.format(a, c)
print(xiao2)
# 字符串调用

print('dddd')
