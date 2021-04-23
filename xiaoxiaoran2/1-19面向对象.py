class Student:
    name = 'xifao'  # 类属性
    age = 22


xiao = Student()
xiao.age = 18
print(xiao.age)
print(xiao.name)

xiaoxiao = Student()
print(xiaoxiao.name)
xiaoxiao.name = 'xiaoxiao'
print(xiaoxiao.name)
print(xiaoxiao.age)

Student.name = 'xiuxiu'  # 改类属性
print(xiao.name)
print()


class Phone:
    brand = 'huawei'
    price = 4999
    type = 'mate 88'

    def call(self):
        print('正在打电话...')
        print('<*>', self.note)

    def __init__(self):
        print('      ^<>^ ')


phone1 = Phone()
phone1.note = '111111'
phone1.price = '59999'
print(phone1.price)
print(phone1.brand)
phone1.call()
print()
phone2 = Phone()
phone2.note = '2222272'
print(phone2.price)
phone2.call()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('{}正在吃肉...'.format(self.name))

    def run(self):
        print('{}....>>{}>>>'.format(self.name, self.age))


p = Person('肖萧然', 666)
p.eat()
p.run()

# 类方法 只能用类不能用于对象


class Personr:
    __age = 18

    def show(self):
        print('.............>', Personr.age)

    @classmethod
    def update_age(cls):
        cls.__age = 20
        print('类方法..')

    @classmethod
    def show_age(cls):
        print('<>>><<<>0:', cls.__age)


Personr.update_age()
Personr.show_age()


class Cat:
    type = '猫'

    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def eat(self, food):
        print('{}喜欢吃{}'.format(self.nickname, food))

    def catch_mouse(self, color, weight):
        print('{}抓了{}的老鼠,有{}重...'.format(self.nickname, color, weight))

    def sleep(self, hour):
        if hour < 5:
            print('鞠旭睡...')
        else:
            print('起床..')

    def show(self):
        print('猫的详细信息...')
        print(self.nickname, self.age, self.color)


cat1 = Cat('花花', 2, '黄')
cat1.catch_mouse('黑', '2斤')
cat1.sleep(8)
cat1.eat('小金鱼..')
cat1.show()

# 魔术方法__init__初始化  __new__


class Pes:
    def __init__(self, name):
        self.name = name
        print('init')
    # def __new__(cls,*arg,**kwargs):
    #     print('new')
    #     position = object.__new__(cls,*arg,**kwargs)
    #     return position
    # def __call__(self,name):
        # print('call')
        # print(name)
    # def __del__(self):#删除对地址的引用
        # print('del')

    def __str__(self):
        return 'a' + self.name + 'b'


p = Pes('uu')
print(p)
