import requests

headers = {
    #User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4381.7 Mobile Safari/537.36
    'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4381.7 Mobile Safari/537.36"
    
}

r = requests.get('https://i.maoyan.com/asgard/movie/1241385',headers=headers)
print(r.text)
