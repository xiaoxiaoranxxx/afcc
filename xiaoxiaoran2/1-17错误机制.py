# : 未加
# 用成中文
# 全局变量  global


def func():
    try:
        p1 = int(input('x= '))
        p2 = int(input('y= '))
        per = input('请输入运算符(+ - * /): ')
        if per == '+':
            print('x+y=',p1+p2)
        elif per == '-':
            print(p1-p2)
        elif per == '*':
            print(p1*p2)
        elif per == '/':
            print(p1/p2)
        else:
            print('输入错误...')
    except ZeroDivisionError:
        print('0不能...')
    except ValueError:
        print('输入的值错误...')
    except Exception as err:
        print('出现未知错误...',err)
    finally:
        print('--------------+---------+++++++++++++++++++')
func()


def register():
    username = input('6位以上数字或字母..')
    if len(username) < 6:
        raise Exception('66666666666')
    else:
        print('输入的是',username)
try:
    register()
except Exception as err:
    print(err)
else:
    print('ok')
