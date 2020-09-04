'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-09-04 11:04:31
LastEditors: sueRimn
LastEditTime: 2020-09-04 11:14:34
'''
class MyClass:
    """ 一个简单的类实例"""
    i = 12345
    def f(self):
        return "hello world"

# 实例化类
x = MyClass()


class Complex:
    def __init__(self, realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0,-4.5)
print(x.r,x.i)