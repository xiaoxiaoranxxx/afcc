a = 'qiq'
name = 'qqzmsdd'
r = a in name 
print(r)

s = 'xiaoxiaoranzuixiu'
print(s[0:5])
print(s[0:])
print(s[:4])
print(s[0:-1])
print(s[::-1])


s= 'xiaoxiaoran xiu xiu xiu'
#第一个字母大写
xiao = s.capitalize()
#每个单词首字母大写
xiao = s.title()
#判断是否为title()函数格式
xiao = s.istitle
#大写小写  lower()
xiao = s.upper()
print(xiao)



#查找

x = 'xiaoxiaoranzuizuixiu xiu xiu'
a = x.find('i')
print(a)
url = 'https://www.bilibili.com/video/BV1pr4y1F7S3?p=50'
p = url.rfind('/')   #rfind 从右侧开始找  lfind 左
print(p)
aa = url[p+1:]
print(aa)


#替换
x = 'xiaoxiaoranzhuixxxxxxxxxxxxxxxxx'
s = x.replace('x','xxr')
s = x.replace('x','xxr',2)  #替换的最大次数 同理可加方向  r l  右左
print(s)

#编码  解码decode 

m = '肖萧然最秀'
msf = m.encode('utf-8')
print(msf)


#判断开头结尾 startswith() endswith() True False
#判断   isalpha()字母  isdigit()数字

f = 'a.doc'
r = f.endswith('txt')
print(r)

#1xx2xx3xx4 添加
a = 'xx'.join('1234')
print(a)

#split切割
s = 'xxx xia odjewwe fwfe ruigo'
r = s.split(' ')
print(r)






