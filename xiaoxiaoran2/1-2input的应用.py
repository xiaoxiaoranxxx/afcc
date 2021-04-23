

print('''
*********************
    xiaoxiaoran
*********************
''')
print('欢迎来到王者荣耀!')
username = input('请输入账号:')
password = input('输入密码:')
print('登录成功')
role = input('输入角色:')
equipment = input('拥有装备')
upgrade_equipment = input('升级装备')
pay = input('付款:')

equipment = upgrade_equipment
print('{}拥有{}装备,花了{}mm'.format(role, equipment, pay))
