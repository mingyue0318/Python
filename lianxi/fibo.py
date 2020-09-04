'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-09-03 18:08:21
LastEditors: sueRimn
LastEditTime: 2020-09-03 18:12:27
'''
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


