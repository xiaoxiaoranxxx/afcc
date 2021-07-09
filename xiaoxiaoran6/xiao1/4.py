# 编写函数实现以下程序：
# 输入一个长整型数s，从低位开始取出s中偶数位上的数，依次构成一个新数放在t中
# 如：s:7654321  t:642


def numstr(value):
    return list(map(int, str(value)))

x = int(input())
ll = numstr(x)
for i in range(len(ll)):
    if i % 2 != 0:
        print(ll[i], end="")
