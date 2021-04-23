def register():
    print('开始注册...')
    username = input('username : ')
    password = input('password : ')
    repassword = input('repassword')
    if password == repassword:
        with open(r'xiaoxiaoran2\user.txt','a') as wstream:
            wstream.write('{} {} \n'.format(username,password))
            print('注册成功...')
    else:
        print('失败,请重新注册...')
        register()

def login():
    print('开始登录...')
    username = input('username : ')
    password = input('password : ')
    if username and password:
        with open(r'xiaoxiaoran2\user.txt') as rstream:
            while True:
                user = rstream.readline()
                if not user:
                    print('密码有误...')
                    answer = input('是否注册(y/n)')
                    if answer == 'y':
                        register()
                        login()
                        break
                    elif answer == 'n':
                        break
                    else:
                        print('输入错误..')
                        continue
                input_user = '{} {} \n'.format(username,password)
                if input_user == user:
                    print('登录成功...')
                    break

def show_book():
    print('欢迎进入图书馆...')
    with open(r'xiaoxiaoran2\book.txt','r') as wstream:
        books = wstream.readlines()
        for book in books:
            print(book,end='')   

login()
show_book()



