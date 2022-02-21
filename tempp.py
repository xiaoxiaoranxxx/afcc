import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
cookies = 'Hm_lvt_0f461eb489c245a31c209d36e41fcc0f=1644495521,1645355594,1645355909,1645356020; trenvecookieinforecord=%2C19-25472%2C28-23383%2C28-15369%2C; trenvecookieztrecord=%2C6%2C; yjs_js_security_passport=13cb7024aed0fdc2d0b91d9805040212e8953f67_1645356862_js; trenvecookieclassrecord=%2C19%2C4%2C11%2C28%2C22%2C3%2C; Hm_lpvt_0f461eb489c245a31c209d36e41fcc0f=1645357098'
cookie = {cookie.split("=")[0]: cookie.split("=")[1]
          for cookie in cookies.split(";")}

r = requests.get('http://www.netbian.com/weimei/index.htm', headers=headers,cookies=cookie)
r.encoding = "gbk"
print(r.text)
