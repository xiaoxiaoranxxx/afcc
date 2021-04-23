# import requests
# import os
# from urllib.parse import urlparse

# from bs4 import BeautifulSoup
# r = requests.get('https://www.xiachufang.com/')
# soup = BeautifulSoup(r.text,features="lxml")
# img_list = []
# for img in soup.select('img'):
#     if img.has_attr('data-src'):
#         img_list.append(img.attrs['data-src'])
#     else:
#         img_list.append(img.attrs['src'])
# image_dir = os.path.join(os.curdir,'images')
# if not os.path.isdir(image_dir):
#     os.mkdir(image_dir)
# for img in img_list:
#     o = urlparse(img)
#     filename = o.path[1:].split('@')[0]
#     filepath = os.path.join(image_dir,filename)
#     print(filepath)
#     resp = requests.get(img)
#     with open(filepath,'wb') as f:
#         for chunk in resp.iter_content(1024):
#             f.write(chunk)

# import re
# from io import BytesIO
# from pycurl import Curl

# buffer = BytesIO()
# c = Curl()
# c.setopt(c.URL,'https://www.xiachufang.com/')
# c.setopt(c.WRITEDATA,buffer)
# c.perform()
# c.close()

# body = buffer.getvalue()
# text = body.decode('utf-8')
# print(text)

# img_list = re.findall(r'src=\"(http://i2\.chuimg\.com/\w+\.jpg)',text)
# image_dir = os.path.join(os.curdir,'images')

# for img in img_list[::-1]:
#     o = urlparse(img)
#     filename = o.path[1:].split('@')[0]
#     filepath = os.path.join(image_dir,filename)
#     if not os.path.isdir(os.path.dirname(filepath)):
#         os.mkdir(os.path.dirname(filepath))
#     url = '%s://%s/%s' % (o.scheme,o.netloc,filename)
#     print(url)
#     resp = requests.get(img)
#     with open(filepath,'wb') as f:
#         c = Curl()
#         c.setopt(c.URL,url)
#         c.setopt(c.WRITEDATE,f)
#         c.perform()
#         c.close



