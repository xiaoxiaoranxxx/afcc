import os

count = 0
l = os.listdir('num')   # 要编号的目录,num是目录
for i in l:
    os.rename(f"num/{i}", f"num/{count}.jpg")
    count += 1
