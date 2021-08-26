import requests
import base64
import re  # 正则匹配模块
s = requests.session()  # 建立会话
url = "http://114.67.246.176:19386/"
head = s.get(url).headers  # 获取头部信息
result = head['flag']  # 得到flag的value
result = base64.b64decode(result).decode('utf-8')  # 第一次base64解码
result = re.search('\w+$', result).group(0)  # 正则匹配base64编码的flag
result = base64.b64decode(result).decode('utf-8')  # 第二次解码
payload = {'margin': result}
print(s.post(url, data=payload).text)  # post传输数据且输出返回信息

# flag{4601edb171ed2b30d624f34d6e319b22}
