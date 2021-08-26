# 题目描述
# 给定一个整数 n。输出一个 n 行数字，n行数字中的第 i行包含 n - i + 1 个由空格隔开的整数，
# 其中第一个数为 n - i + 1，之后每一个数都比前一个数小 1
# 输入
# 一个整数n(n < 20)
# 输出
# 递减三角形

def num(x):
    while x != 0:
        print('{} '.format(x), end='')
        x -= 1
    print()
        
x = int(input())

for i in range(x):
    num(x)
    x-=1

input()
