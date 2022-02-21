import hashlib

x = 112
str = f"123{x*x}123{x*3}{x}2"

m = hashlib.md5(str.encode('utf-8')).hexdigest()

print(str)
print(m)
