import re

str = '''
R#conf t
Router(config)#inter fa 1/0
Router(config‐if)#ip address 192.168.2.1 255.255.255.0
Router(config‐if)#no shutdown
Router(config‐if)#exit
Router(config)#inter serial 2/0
Router(config‐if)#ip address 192.168.3.2 255.255.255.0
Router(config‐if)#end
'''

for i in str.strip().split("\n"):
    i = re.sub(r'^\S+#', "", i)
    # if("/" in i):
    #     print(i[:i.find("//")])
    # else:
    #     print(i)
    print(i)
