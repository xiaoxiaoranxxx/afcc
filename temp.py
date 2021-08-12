import base64

# st = 'hello world!'.encode()  # 默认以utf8编码
# res = base64.b64encode(st)
# print(res.decode())  # 默认以utf8解码

#QWIHBLGZZXJSXZNVBZW

res = 'aGVs bG8g d29y bGQh'
res = base64.b64decode(res)
print(res.decode())  # 默认以utf8解码

s = 'QWIH BLGZ ZXJS XZNV BZW'
print(s)



