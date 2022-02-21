import requests
from bs4 import BeautifulSoup
import os
import re


def getHtmlurl(url):  # 获取网址
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
    cookies = 'Hm_lvt_0f461eb489c245a31c209d36e41fcc0f=1644495521,1645355594,1645355909,1645356020; trenvecookieinforecord=%2C19-25472%2C28-23383%2C28-15369%2C; trenvecookieztrecord=%2C6%2C; yjs_js_security_passport=13cb7024aed0fdc2d0b91d9805040212e8953f67_1645356862_js; trenvecookieclassrecord=%2C19%2C4%2C11%2C28%2C22%2C3%2C; Hm_lpvt_0f461eb489c245a31c209d36e41fcc0f=1645357098'
    cookie = {cookie.split("=")[0]: cookie.split("=")[1]
              for cookie in cookies.split(";")}
    try:
        r = requests.get(url, headers=headers, cookies=cookie)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getimgurl(img):
    href = img['href']
    url = "http://www.netbian.com"+href
    # print(url)
    htm = getHtmlurl(url)
    soup = BeautifulSoup(htm, 'html.parser')
    return soup


def getpic(html):  # 获取图片地址并下载
    soup = BeautifulSoup(html, 'html.parser')
    all_img = soup.find('div', class_='list').find('ul').find_all(
        "a", attrs={'href': re.compile('^((?!http).)*$'), 'target': '_blank'})

    for img in all_img:
        title = img['title']

        soup1 = getimgurl(img)
        im1 = soup1.find('div', id='main').find('div', class_='endpage').find(
            'div', class_='pic').find('p').find('a')
        soup2 = getimgurl(im1)
        im2 = soup2.find('div', id='main').find('table').find('a')

        img_url = im2['href']
        # print(img_url)

        if(len(img_url) > 20):
            with open('2.txt', 'a') as f:
                f.write(img_url)
                f.write('\n')


def main():
    for i in range(37, 100):
        if i == 1:
            url = 'http://www.netbian.com/dongman/index.htm'
        else:
            url = 'http://www.netbian.com/dongman/index_' + str(i) + '.htm'
        html = (getHtmlurl(url))
        print(str(i)+" : ")
        print(getpic(html))


main()
