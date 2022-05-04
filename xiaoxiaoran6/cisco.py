import re

str = '''
Switch#conf t
Switch(config)#vlan 2
Switch(config‐vlan)#exit
Switch(config)#vlan 3
Switch(config‐vlan)#exit
Switch(config)#interface fa 0/1
Switch(config‐if)#switchport access vlan 2
Switch(config‐if)#exit
Switch(config)#inter fa 0/2
Switch(config‐if)#switchport access vlan 3
Switch(config‐if)#exit
Switch(config)#inter fa 0/24
Switch(config‐if)#switch mode trunk
Switch(config‐if)#end
Switch#show vlan
'''

for i in str.strip().split("\n"):
    i = re.sub(r'^\S+#', "", i)
    # if("/" in i):
    #     print(i[:i.find("//")])
    # else:
    #     print(i)
    print(i)
