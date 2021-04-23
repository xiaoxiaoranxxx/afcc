# 私有化 封装
import random


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.__socre = 99

    def __str__(self):
        return '姓名:{},年龄:{},分数:{}xiuxiuxiu'.format(self.name, self.__age, self.__socre)

    # def setAge(self, age):  # 赋值
    #     if age > 0 and age <= 120:
    #         self.__age = age
    #     else:
    #         print('xxxxx')

    # def getAge(self):  # 取值
    #     return
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print('xxxxxxx')


xiaoxiaoran = Student('肖萧然', 18)
print(xiaoxiaoran)

xiaoxiaoran.name = '肖萧然最秀'
# xiaoxiaoran.setAge(66)
xiaoxiaoran.age = 66
print(xiaoxiaoran)


xiao = Student('xiao', 9)
print(xiao)

# 关联


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}速度行驶{}小时'.format(
            self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌,速度{}'.format(self.brand, self.speed)


r = Road('进展高速', 12244)
audi = Car('audi', 120)
print(audi)
audi.get_time(r)

# 继承


class Person:  # 父类 同类代码
    def __init__(self, name, age):
        self.name = name  # '<<_^$^_>>'
        self.age = 119

    def eat(self):
        print(self.name + 'eating')

    def run(self):
        print(self.name + 'runing')


class Students(Person):  # 子类
    def __init__(self, name, age, clazz):
        super().__init__(name, age)  # 父类对象
        self.clazz = clazz

    def study(self, couse):
        print('{}正在学习{}课程...'.format(self.name, couse))

    def eat(self, food):
        super().eat()
        print(self.name + 'eating高级加餐...'+food)


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


s = Students('ss', 18, 'python1班')
s.run()
s.study('pythonjijijiji')
s.eat('食物')


e = Employee('ee', 23, 10000, 'king')
e.run()
e.eat()

lists = ['a', 's', 'd', 'f']
d = Doctor('dd', 30, lists)

# 多重继承


class Persons:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('eat1111')

    def eat(self, food):  # 重名后会覆盖前面的
        print('eat222', food)


p = Persons('xiaoxiao')
p.eat('cc')


class A:
    def test(self):
        print('A')


class B:
    def test1(self):
        print('B')


class C(A, B):
    def test2(self):
        print('C')


c = C()  # 先本身,在AB 经典类 从左到右,深度优先 # 新式类
c.test()
c.test1()
c.test2()

# 多态
# class Person:
#     def feed_pet(self,Pet):
#         isinstance(pet,Pet)
#         pass
#     def Pet:
#         pass

#单例模式  单个对象  共享
class SingLetion:
    __instance = None
    name = 'xiaoxiaoran'
    def __new__(cls):
        print('new')
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def show(self,n):
        print('show',SingLetion.name,n)

s = SingLetion()
s1 = SingLetion()
print(s)
print(s1)
s.show(2)
s1.show(3)


