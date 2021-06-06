# findall   返回包含所有匹配项的列表
# search	匹配整个字符串中的任意位置，返回第一个成功的匹配对象
# split     返回一个能够匹配的子串将字符串分割的列表
# sub       用字符串替换一个或多个匹配项


# https://www.cnblogs.com/leejack/p/9189796.html


# 字符匹配
# 在正则表达式中，如果直接给出字符，就是精确匹配。
# \d 匹配一个数字
# \D 匹配一个非数字
# \w 匹配一个字母、数字或下划线_
# \W 匹配任何非单词字符, 等价于“[ ^ A-Za-z0-9_]"
# \s 匹配任何空白字符，包括空格、制表符、换页符等等, 等价于[f\n\r\t\v]
# \S 匹配任何非空白字符
# \n 匹配一个换行符
# \r 匹配一个回车符
# \t 匹配一个制表符

# 数量匹配
# .匹配除“\n"之外的任何单个字符
# *匹配前面的子表达式零次或多次
# +匹配前面的子表达式一次或多次
# ?匹配前面的子表达式零次或一次
# {n}，n是一个非负整数，匹配确定的n次
# {n, m}，m和n均为非负整数，其中n <= m，最少匹配n次且最多匹配m次
# {n, }，n是一个非负整数，至少匹配n次
# {, m} 匹配前面的正则表达式最多m次

# 范围匹配
# x | y 匹配x或y
# [xyz] 字符集合, 匹配所包含的任意一个字符
# [ ^ xyz] 负值字符集合, 匹配未包含的任意字符
# [a-z] 字符范围, 匹配指定范围内的任意字符
# [ ^ a-z] 负值字符范围, 匹配任何不在指定范围内的任意字符


# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
# A | B可以匹配A或B，所以(P | p)ython可以匹配'Python'或者'python'。
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束。


import re

str = "The rain i2389rydf fbwsgdy82ny723xt78 3xn2zjiug23uy8t2g3r2 3ur23vuysayeqwasdawr23qwertyuusdfghjxn Spain"
x = re.findall("f", str)    # findall返回包含所有匹配项的列表  ['f', 'f', 'f']
x = re.findall("7ee", str)  # 该列表按照找到的顺序包含匹配项。如果未找到匹配项，则返回空列表： []
x = re.search("s", str)     # search()函数在字符串中搜索匹配项，如果匹配则返回Match对象：
x = re.split("\s", str)     # split()函数返回一个列表，其字符串在每次匹配时被拆分：
x = re.split("\s", str, 1)  # 仅在第一次出现时分割字符串：
x = re.sub("\s", ">.<", str)  # 用>.<替换每个空格字符：
x = re.sub("\s", ">.<", str, 1)  # count
# print(x)

x = re.search(r"\bS\w+", str)
# .span()返回包含匹配的开始和结束位置的元组。
# .string返回传递给函数的字符串
# .group()返回匹配的字符串部分

# \d{3,4}\s+\d{3,8}  3-4个数字 至少一个空格 3-8个数字

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
result = re.match(r'\d{3,4}\-\d{3,8}$', '020-12345')
# print(result.string)

email = 'lee.jack3@netec.com.cn'
pattern = r'^[a-z]{1,}\.[a-z]+\d*@netec.com.cn$'
result = re.match(pattern, email)

str = "32 ddd ewe e       e"
str = "3;2 dd,d e,w,e ,e     \  e"
pattern = r'[\s\,\;]+'
result =re.split(pattern,str)  #无论多少个空格都可以正常分割

print(result)
