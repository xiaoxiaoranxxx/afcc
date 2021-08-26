# 题目描述
# 大家知道，东方国家认为4这个数字不吉利，西方国家认为13这个数字不吉利。有一个外星球的居民同我们地球人类似，认为7这个数字不吉利。
# 基于这个认识，这些外星居民把任何一个含有7的数字都认为是不吉利的，比如：7，17，876，1751，……。
# 现在这些外星居民想知道在任意两个数A，B（A≤B）之间有多少个不吉利的数，但是他们又特别迟钝，因此需要你的帮助。

# 输入
# 输入两个整数A、B，并用空格进行间隔（0≤A≤B≤1050）。
# 输出
# 输出单个整数，表示[A，B]之间不吉利的数的个数。

count = 0


def numstr(value):
    return list(map(int, str(value)))


def xiao(x):
    global count
    for i in range(len(numstr(x))):
        if 7 in numstr(x):
            count += 1
            break


a, b = map(int, input().split())
while a <= b:
    xiao(a)
    a += 1
print(count)
