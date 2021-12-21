# print((lambda x: x.read(x.namelist()[0]).decode())(__import__('zipfile').ZipFile(__import__('io').BytesIO(bytes.fromhex(
#     ''.join([hex(i >> 4)[2:] for i in __import__('base64').b64decode(open('1.txt', 'rb').read().replace(b'\n', b''))]))))))

# # 1、base64解码；2、解码结果每字节保留十六进制形式高位；3、拼接得到新的十六进制串转字节得到zip压缩包；4、解压得到flag。


# print(int(''.join([i for i in input() if i.isdigit()]))+1)

import base64

import zipfile


str = base64.b64decode(open('1.txt', 'rb').read())
# print(str)

s = bytes.fromhex(''.join([hex(i >> 4)[2:]for i in str]))

# zipfile.ZipFile(s)

f = open('1.zip', "wb")
f.write(s)
f.close

# f = zipfile.ZipFile("1.zip", mode="r")
# # f.write("1.txt")
# f.extractall()
# f.close


