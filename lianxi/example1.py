#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-08-31 11:31:14
LastEditors: sueRimn
LastEditTime: 2020-09-01 17:55:23
'''
# input("按下 enter 键退出，其他任意键显示...\n")

a, b, c = 1, 2, "john"

print(a)
print(b)
print(c)

str = 'abcdefg'

print(str[1:5])

print(str[1:5:3])

list = ['runoob', 786, 2.32, 'john', 70.2]

var = 1
while var == 1:
    num = input('Enter a number :')
    print("You entered:", num)
    # print(1 * 3)
print("GOOD BYE")


def reverseWords(input): 
      
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ") 
  
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1] 
  
    # 重新组合字符串
    output = ' '.join(inputWords) 
      
    return output 
  
if __name__ == "__main__": 
    input = 'I like runoob'
    rw = reverseWords(input) 
    print(rw)

