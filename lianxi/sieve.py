'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-08-31 17:07:14
LastEditors: sueRimn
LastEditTime: 2020-08-31 17:29:32
'''
sieve = [True] *101
for i in range(2,100):
    if sieve[i]:
        print(i)
        for j in range(i*i,100,i):
            sieve[j] = False



