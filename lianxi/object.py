'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-09-04 11:04:31
LastEditors: sueRimn
LastEditTime: 2020-09-05 18:29:15
'''


class MyClass:
    """ 一个简单的类实例"""
    i = 12345

    def f(self):
        return "hello world"


# 实例化类
x = MyClass()


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性
    __weight = 0

    # 定义构造函数
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说：我 %d 岁。" % (self.name, self.age))


# 继承


#单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        #调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    #覆写父类的方法
    def speak(self):
        print("%s说：我%d岁了，我再读%d年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()


#另一个类，多重继承之前的准备
class speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


#多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample('Tim', 25, 80, 4, 'Python')
test.speak()

#方法重写


class Parent:
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):
    def myMethod(self):
        print('调用子类方法')


c = Child()
c.myMethod()
super(Child, c).myMethod()

# 类属性与方法
# 类的私有属性


class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(11, counter.publicCount)
print(22, counter.__secretCount)  #实例不可以访问私有变量


class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name:', self.name)
        print('url:', self.__url)

    def __foo(self):
        print('私有方法')

    def foo(self):
        print('共有方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()
x.foo()
x.__foo()


# ********
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        print(1)
        return 'Vector(%d,%d)' % (self.a, self.b)

    def __add__(self, other):
        print(2)
        print(3, self)
        print(4, other)
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1)
print(v2)
print(v1 + v2)

a = 10


def test1():
    global a
    a = a + 1
    print(a)


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
      
