# 自定义模块 可以自己写
#  import 模块名    name.a  name.def  name.class
#  from name import a,def/def/class   导入一部分
#  from name import *   # __all__ = ['a','b']限制
#  from bag.name import name
# __init__.py可以初始化函数   结合__all__
# 循环导入...

import sys
#print(sys.path)
print(sys.version)
print(sys.argv)
print(sys.version_info)
print()

import time
print(time.time())
print(time.ctime(time.time()))
print(time.localtime())
print(time.localtime().tm_year)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
#print(time.strptime('2019/02/22'))
time.sleep(1)
print()

import datetime
print(datetime.time.hour)
d = datetime.date(2020,12,12)
print(datetime.date.ctime(d))
print(datetime.date.today())
print()

import random
print(random.random())
print(random.randrange(1,10))
print(random.randrange(1,10,2))
print(random.randint(1,10))
list1 = ['a','s','d','f','e','ee']
print(random.choice(list1))
print(random.shuffle(list1))
print()

import hashlib
print((hashlib.md5('肖萧然最秀'.encode('utf-8'))).hexdigest())
print((hashlib.sha1('肖萧然最秀'.encode('utf-8'))).hexdigest())
print((hashlib.sha256('肖萧然最秀'.encode('utf-8'))).hexdigest())
s = '肖萧然'
md5 = hashlib.md5(s.encode('utf-8'))
print(md5.hexdigest())

import re
msg = 'xiaoxiaoranzuixiu'
# pattern = re.compile('xiao')
# result = pattern.match(msg)
# print(result)
print(re.match('xiao',msg))  #从头开始匹配
print(re.search('ran',msg))  #匹配整个字符串
print(re.search('ran',msg).span())  #返回位置
print(re.search('ran',msg).group())  #
print(re.search('ran',msg).groups())  #
msf = 'rtyuuifghjryuwiugfuiw123456789qwertyui8asdfghjkzxcvb'
print(re.search('[0-9][a-z][a-z]',msf))
print(re.findall('[0-9][a-z][a-z][a-z]',msf))
print(re.findall('[a-z][0-9]+[a-z]',msf))
print(re.match('[a-z]{1,}',msf))
print(re.match('[a-zA-Z][0-9a-zA-Z]{1,}',msf))
print(re.match('[a-zA-Z]\w{1,}',msf))
n = '100'
print(re.match(r'[1-9]?\d?$|100$',n))
n = '2222222222@qq.com'
print(re.match(r'\w{5,20}@(163|qq|126)\.com',n))
msf = '<html><h1>abc</h1></html>'
print(re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msf))
print(re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msf).group(1))
print(re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msf).group(2))
print(re.sub(r'\d+','90','a=1,b=2,c=3'))
print(re.split(r'[,:]','a:shd,d:dd:ff:Gg'))
msf = '12345678901'
print(re.match(r'1\d{9}[0-35-689]$',msf))   #不以4,7结尾
print(re.match(r'1\d{9}[0-35-689]$',msf).group())
msf = '010-12345678'
print(re.match(r'(\d{3})-(\d{8})$',msf))
print(re.match(r'(\d{3})-(\d{8})$',msf).group(2))
#匹配默认是贪婪的  后面加?可解决

import itertools
for val in itertools.permutations('1834'):
    print(val)
for val in itertools.permutations('1834',2):
    print(val)


