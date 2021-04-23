import requests

r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(r.reason)
#print(r.text)

r = requests.post('http://httpbin.org/post',data={'a':'1'})
#print(r.json())

ua = 'Mozilla/5.0'
headers = {'user-agent' : ua}
r = requests.get('http://httpbin.org/headers',headers=headers)
#print(r.json())

cookies = dict(userid='123456',toen='qwertyuiop')
r = requests.get('http://httpbin.org/cookies',cookies=cookies)
#print(r.json())

r = requests.get('http://httpbin.org/basic-auth/xiao/123456',auth=('xiao','123456'))
#print(r.json())

bad_r = requests.get('http://httpbin.org/status/404')
#print(bad_r.status_code)

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/xiao/1111')
# r = s.get('http://httpbin.org/cookies')
# print(r.json())

#print(requests.get('http://httpbin.org/ip').json())
#print(requests.get('http://httpbin.org/ip',proxies={'http':'http://iguye.com:41801'}).json())


