print('------>')
bata = []
user ={}
while True:
    usename = input('请输入用户名')
    user['username']= usename
    password = input('请输入密码:')
    repassword = input('请确认密码:')
    if password == repassword:
        user['password']=password
    else:
        print('请重新输入:')
        continue
    bata.append(user)
    break
print(bata)  