import base64
str = "TgrbT3nbw2LgT19iuhD0R3f1TZ9gT2bkzK=="


def change(key, str):
    result = ""
    for i in str:
        if (i.islower()):
            if((ord(i)+key) > 122):
                result += chr(ord(i)+key-26)
            else:
                result += chr(ord(i)+key)
        elif(i.isupper()):
            if((ord(i)+key) > 90):
                result += chr(ord(i)+key-26)
            else:
                result += chr(ord(i)+key)
        else:
            result += i
    return result


for i in range(26):
    base_str = change(i, str)
    s = base64.b64decode(base_str)
    try:
        print(s.decode())
    except:
        pass
        # print(s)
