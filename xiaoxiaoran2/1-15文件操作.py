import os
s = open(r'C:\Users\Administrator\Desktop\code\1.txt')
print(s.read())  # 读取文件,图片不能使用默认的方式
print(s.readable())  # 判断文件是否可读
print(s.readline())  # 读一行,前面不能有读过

s = open(r'C:\Users\Administrator\Desktop\code\1.txt', 'w')  # 写,会覆盖
w = '''
xiaoxiaoran
xiaoxiao
xiao
xiao
xiaoxiao
xiaoxiaoran
'''
s.write(w)
s.write('eeeeee\n')
s.writelines(['a\n', 'b\n', 'c\n'])
s.close()

# 复制文件
with open(r'C:\Users\Administrator\Desktop\code\1.txt','rb') as stream:
    container = stream.read()
    with open(r'C:\Users\Administrator\Desktop\code\2.txt','wb') as wstream:
        wstream.write(container)
print('复制成功...')
os.remove(r'C:\Users\Administrator\Desktop\code\2.txt')
print('删除成功...')

# 复制到当前文件夹
with open(r'C:\Users\Administrator\Desktop\code\1.txt','rb') as stream:
    container = stream.read()
    file = stream.name
    filename = file[file.rfind('\\')+1:]
    path = os.path.dirname(__file__)
    pate = os.path.join(path,filename)
    with open(pate,'wb') as wstream:
        wstream.write(container)
os.remove(r'c:\Users\Administrator\Desktop\code\vscode-py\xiaoxiaoran2\1.txt')

print(os.path.isabs(r'C:\Users\Administrator\Desktop\code\1.txt'))
print(os.path.isabs('xiaoxiaora1/xiao.py'))
print(os.path.isabs('../../xiaoxiaora1/xiao.py'))
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.getcwd())
print(os.listdir(r'c:\Users\Administrator\Desktop\code\vscode-py\xiaoxiaoran1'))






