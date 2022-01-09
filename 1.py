
str = '''1: < ZWAXJGDLUBVIQHKYPNTCRMOSFE <
2: < KPBELNACZDTRXMJQOYHGVSFUWI <
3: < BDMAIZVRNSJUWFHTEQGYXPLOCK <
4: < RPLNDVHGFCUKTEBSXQYIZMJWAO <
5: < IHFRLABEUOTSGJVDKCPMNZQWXY <
6: < AMKGHIWPNYCJBFZDRUSLOQXVET <
7: < GWTHSPYBXIZULVKMRAFDCEONJQ <
8: < NOZUTWDCVRJLXKISEFAPMYGHBQ <
9: < XPLTDSRFHENYVUBMCQWAOIKZGJ <
10: < UDNAJFBOWTGVRSCZQKELMXYIHP <
11： < MNBVCXZQWERTPOIUYALSKDJFHG <
12： < LVNCMXZPQOWEIURYTASBKJDFHG <
13： < JZQAWSXCDERFVBGTYHNUMKILOP <'''
# 密钥为：2, 3, 7, 5, 13, 12, 9, 1, 8, 10, 4, 11, 6
# 密文为：NFQKSEVOQOFNP'''

l = "2,3,7,5,13,12,9,1,8,10,4,11,6".split(",")
ll = str.split("\n")
#print(l, ll)


lll = []
for i in l:
    lll.append(ll[int(i)-1][5:-2].replace(" ", ""))
#print(lll)


str = "NFQKSEVOQOFNP"
index = 0
for i in lll:
    temp = i.find(str[index])
    index += 1
    print((i[temp:]+i[:temp])[17].lower(), end="")
