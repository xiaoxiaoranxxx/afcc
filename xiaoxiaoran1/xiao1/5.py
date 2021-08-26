# 请编写函数fun，函数的功能是 ：移动一维数组中的内容；若数组中有10个整数，要求把下标从0到p（含p，p小于10）的数组元素平移到数组的最后。呢。。
# 如：数组中原始内容为：1、2、3、4、5、6、7、8、9、10；p = 3。
# 移动后数组中为5、6、7、8、9、10、1、2、3、4.

str = input()
A = str.split(' ')


def numstr(value):
    return list(map(int, str(value)))


a = int(input())
a = len(A)-a-1
for i in range(a):  # 右移
    A.insert(0, A.pop())

for i in range(len(A)):
    print('{} '.format(A[i]), end='')
