import urllib.request
import json

r = urllib.request.urlopen('http://httpbin.org/get')
text = r.read()
print(text)
print(r.status,r.reason)
obj = json.loads(text)
print(obj)
#print(r.headers)
for k,v in r.headers._headers:
    print('%s:%s' % (k,v))


