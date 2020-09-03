# coding = utf-8
'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-09-02 10:19:51
LastEditors: sueRimn
LastEditTime: 2020-09-02 15:30:33
'''
# 迭代器


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    # def __next__(self):
    def next(self):
        x = self.a
        self.a += 1
        return x


myClass = MyNumbers()
myiter = iter(myClass)

print('1', next(myiter))
print('1', next(myiter))
print('1', next(myiter))
print('1', next(myiter))
print('1', next(myiter))
print('1', next(myiter))


class MyNumbers1:
    def __iter__(self):
        self.a = 1
        return self

    #def __next__(self):
    def next(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myClass = MyNumbers1()
print(myClass)
myiter1 = iter(myClass)

for x in myiter1:
    print(x)

import sys


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = a, a + b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()

def printinfo(arg1 , **vardict):
    print('输出：')
    print(arg1)
    print(vardict)

printinfo(1,a=2,b=3)


def f(a,b,*,c):
    return a+b+c

f(1,2,3)

f(1,2,c=3)
# 列表->堆栈
stack = [3,4,5]
stack.append(6)
stack.append(7)

print(stack)

stack.pop()

print(stack)
# 列表->队列
from collections import deque

queue = deque(["Eric","John","Michael"])

print(queue)

queue.append('Terry')
print(queue)
queue.append('Graham')
print(queue)

queue.popleft()

print(queue)

# 列表推导式

vec = [2,4,6]

vec1 = [3*x for x in vec]
print(vec1)

vec2 = [[x,x**2] for x in vec]
print(vec2)

freshfruit = ['   banana','    loganberry ','passion fruit    '];

_freshfruit = [weapon.strip() for weapon in freshfruit]
print(_freshfruit)


# 嵌套列表解析
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

for row in matrix:
    print(row)


[[row[i] for row in matrix]for i in range(4)]


# 方式二
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
transposed = []
for i in range(4):
    transposed_row  = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)


