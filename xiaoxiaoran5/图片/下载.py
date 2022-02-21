import requests

count = 3000

with open('dongwu.txt', 'r') as f:
    for i in f.readlines():
        #print(i.strip())
        r = requests.get(i.strip())
        with open(f"p/{count}.jpg", 'wb') as ff:
            ff.write(r.content)
            ff.close()
            print(f"{count}.jpg文件保存成功")

        count += 1
