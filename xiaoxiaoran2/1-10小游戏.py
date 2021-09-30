import random
print('''
$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$  --  --  $$$$$$$$$$$$   $$          $$$$$$$$====>       肖萧然最秀
$$$$$$$    *     $$$$$$$$$$$$   $$          $$$$$$$$====>
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$

''')
coin = 1000
weapon_list = [['秀秀金砖', 888]]
while True:
    role = int(input('1.肖萧然 \n2.鲁班 \n3.后羿 \n4.李白 \n5.貂蝉 \n6.诸葛\n请选择游戏人物:'))
    if role == 1:
        role = '肖萧然'
        print('肖萧然自带光环!奖励1000')
        coin += 1000
        break
    elif role == 2:
        role = '鲁班'
        break
    elif role == 3:
        role = '后羿'
        break
    elif role == 4:
        role = '李白'
        break
    elif role == 5:
        role = '貂蝉'
        break
    elif role == 6:
        role = '诸葛'
        break
    else:
        print('输入错误!')
print('')
print('正在进入游戏...')
print('-------===>')
print('欢迎{}来到xxxx,当前金币为{}'.format(role, coin))
print('')
while True:
    choice = int(input('\n1.进入商店\n2.皇家赌场\n3.大杀特杀\n4.查看财产\n5.退出游戏\n请选择:'))
    if choice == 1:
        print('欢迎进入小金库:')
        weapons = [['车', 8800], ['电脑', 4000], ['房子', 103300],
                   ['手机', 7300], ['书', 400], ['山', 200]]
        for weapon in weapons:
            print(weapon[0], '\t', weapon[1], sep='')
        weaponname = input('请输入要买的财产名称:')
        if weaponname not in weapon_list:
            for weapon in weapons:
                if weaponname == weapon[0]:
                    if coin > weapon[1]:
                        print('{}购买财产{}成功!开始了走向人生巅峰的一小步...!'.format(
                            role, weaponname))
                        print('--------===>')
                        coin -= weapon[1]
                        weapon_list.append(weapon)
                        break
                    elif coin < weapon[1]:
                        print('余额不足!!!')
                        break
                    else:
                        print('参数错误!!!')
                        break
            else:
                print('输入错误!')
        elif weaponname in weapon_list:
            print('已拥有该武器!')
        else:
            print('输入错误!')
    elif choice == 2:
        print('$'*30)
        print('\t欢迎来到荣耀皇家赌场')
        print('$'*30)
        money = coin
        answer = input('是否进入游戏(y/n)?')
        if answer == 'y':
            while money < 200:
                n = int(input('金币不足,请充值!(必须100的倍数哦),输入充值金额:'))
                if n % 100 == 0 and n > 0:
                    money = coin
                else:
                    print('参数错误!')
            print('当前剩余游戏为:{},玩一下扣200个游戏币'.format(money))
            print('load...')
            print('load...')
            a = 1
            while a == 1:
                t1 = random.randint(1, 6)
                t2 = random.randint(1, 6)
                money -= 200
                print()
                print('系统洗牌完毕,请猜大小')
                guess = input('输入大(a)或小(b):')
                c = t1+t2
                print('这输出的结果为:', c)
                print('------------->')
                if(c > 6 and guess == 'a') or ((c <= 6 and guess == 'b')):
                    print('恭喜%s猜测正确!!获得400个游戏币' % role)
                    money += 400
                elif(c > 6 and guess == 'b') or ((c <= 6 and guess == 'a')):
                    print('很遗憾,你猜错了')
                elif guess == 'exit':
                    print('正在退出...')
                    print('当前剩余:', money)
                    money += 200
                    coin = money
                    break
                elif money <= 100:
                    print('余额不足!')
                else:
                    print('参数错误')
                    money += 200
                print('当前游戏币为:', money)
    elif choice == 3:
        print('输入正确可以得到100,错则...!加油吧少年...')
        s = '12345678901234567890qwertyuiiopasdfghjklzxcvbnmQWERTYUUIIOASDFGHJKLZXCVBNM'
        while True:
            code = ''
            for i in range(4):
                ran = 0
                ran = random.randint(0, len(s)-1)
                code += s[ran]
            print('验证码', code)
            use = input('请输入验证码:')
            if use.lower() == code.lower():
                print('输入正确,获得100')
                coin += 100
                print('当前金币为:', coin)
                print()
            elif use == 'exit':
                print('已退出...')
                print('当前金币为:', coin)
                print()
                break
            else:
                print('错误!请重新输入...-_-...')
                print('当前金币为:', coin)
                print()
    elif choice == 4:
        print('{}拥有的财产如下:'.format(role))
        for weapon in weapon_list:
            print(weapon, ' ', '|')
    elif choice == 5:
        answer = input('是否退出游戏(y/n)')
        if answer == 'y':
            print('正在退出游戏...')
            break
        if answer == 'n':
            continue
        else:
            print('输入错误...')
    else:
        print('输入错误,请重新输入...')
