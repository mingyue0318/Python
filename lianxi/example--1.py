'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-09-07 10:14:43
LastEditors: sueRimn
LastEditTime: 2020-09-07 19:03:32
'''
# 二次方程
import cmath
a = 1
b = 5
c = 6

d = (b * 2) - (4 * a * c)
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

#计算三角形的面积
a = 2
b = 3
c = 4
s = (a + b + c) / 2


area = (s*(s-a)*(s-b)*(s-c))**0.5
print('三角形的面积为%0.2f'%area)

# 计算圆的面积

def findArea(r):
    PI = 3.142
    return PI * (r*r)
print("圆的面积为%.6f"%findArea(5))

#随机数生成
import random

print(random.randint(0,9))

#摄氏温度转华氏温度

celsius = float('35.6')

fahrenheit = (celsius *1.8)+32
print('%0.1f 摄氏温度转华氏温度为 %0.1f'%(celsius,fahrenheit))

#交换变量

#1使用临时变量

x = 1
y = 2

temp = x
x = y
y = temp

#不使用临时变量

x,y = y,x



# 判断字符串是否是数字

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(x)
        return Turn
    except (TypeError,ValueError):
        pass
    return False

#奇偶
num = 89
x
if(num%2 ==0):
    x= '偶数'
else:
    x= 'ji shu'

#闰年

year = 1999
# def year(x):
if year%100 == 0:
    if year%400 ==0:
        print('"{0}是一个闰年"'.format(year))
    else:
        print('"{0}bu是一个闰年"'.format(year))
else:
    if year%4 ==0:
        print('"{0}是一个闰年"'.format(year))
    else:
        print('"{0}bu是一个闰年"'.format(year))
# year(1999)

#获取最大值

max(1,2,3,4,5)

# 质数

num = 7
if num>1:
    for i in range(2,num):
        if (num%i) ==0:
            print("不是质数")
            # break
    else:
        print('是质数')
else:
    print('不是质数')


