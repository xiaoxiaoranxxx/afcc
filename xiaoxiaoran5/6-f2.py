import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4381.7 Mobile Safari/537.36'}
url = 'http://www.dianping.com/shop/jAV7cVMNXlIhwjE9'
r = requests.get(url,headers=headers)
index = r.text.find('killwill123')
print(r.text[index-200:index+200])

