'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-09-05 19:47:54
LastEditors: sueRimn
LastEditTime: 2020-09-16 23:34:33
'''
#1
print("Hello world")

#2
num1 = input('请输入第一个数字')
num2 = input('请输入第二个数字')

sum = float(num1) + float(num2)

print('第一个数字为{0}第二个数字为{1}和为{2}'.format(num1,num2,sum))

# 平方根

num = 16
print(2**31 -1)




### 进制转换
num = 10

bin(num)
oct(num)
hex(num)

### ASCII 码 与字符的相互转化
str = 'a'
ascii = 97
ord('a')
chr(ascii)

###  最大公约数
def hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf = i
    return hcf

print(hcf(20,240))


### 最小公倍数

def lcm(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while True:
        if greater%x == 0 and greater%y ==0:
            lcm = greater
            break
        greater+=1
    return lcm

print(lcm(4,6))

#实现简单的计算器

# 参数
# 算式

def jsq(x,y,f):
    if type(f) != int or f>4 or f<1:
        return '算式错误'
    if type(x) or type(y):
        return '数字不合法'
    if f ==1:
        print(x+y)
    elif f==2:
        print(x-y)
    elif f==3:
        print(x*y)
    elif f==4:
        print(x/y)


### 生成日历
import calendar

yy = 1990
mm = 3

print(calendar.month(yy,mm))


### n个自然数的立方和

def sumOfSeries(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**3
    return sum

n = 6

print(sumOfSeries(n))

###计算数组元素之和

arr = [1,2,3,4,5]

def _sum(arr,n):
    return sum(arr)
n = len(arr)
print(_sum(arr,n))

### 对调前部分和后部分
arr = [1,2,3,4,5,6]
d = 3
n = len(arr)
def leftRotate(arr,d,n):
    head = arr[0:d]
    tail = arr[d:]
    _arr = tail+head
    return _arr
print(leftRotate(arr,d,n))

### 对调收尾元素
arr = [1,2,3,4,5]

def swapList(arr):
    head = arr[0:1]
    tail = arr[-1:]
    _arr = arr[1:-1]
    return tail+_arr+head

print(swapList(arr))

### 对调指定元素
arr = [1,2,3,4,5]

def swapPosition(arr,i,target):
    get = arr[i-1],arr[target-1]
    arr[target-1],arr[i-1] = get
    return arr
print(swapPosition(arr,2,4))

### 翻转列表

li = [1,2,3,4,5]

def Reverse(lst):
    return lst[::-1]

print(Reverse(li))

### 元素是否在list中

if 4 in li:
    print('zai')

li = [1,2,3,4,5]
for i in li:    
    print(i)
    if(i==4):
        print('zai')


from bisect import bisect_left
bisect_left(li,4)


if 4 in set(li):
    print('zai')
### 清空list
li = [1,2,3,4]

li.clear()

### 复制list
li = [1,2,3,4,5]
li1 = li[:]
li2 = []
li2.extend(li)
li3 = list(li)
li4 = li.copy()

### 元素出现的次数

li = [1,2,3,3,2,1,1,2,4]

li.count(3)


li = [3,2,1]
li.sort()
print(*li[:1])

### 移除字符串中指定元素
test_str = "Runoob"
  
# 输出原始字符串
print ("原始字符串为 : " + test_str) 
  
# 移除第三个字符 n
new_str = "" 
  
for i in range(0, len(test_str)): 
    if i != 2: 
        new_str = new_str + test_str[i] 

print ("字符串移除后为 : " + new_str) 
###判断字符串是否存在子字符串

s = '12345'
s1 = '123'

s.find(s1)


### 插入排序
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

### 快速排序

def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low,high):
        #当前元素小于或等于pivot
        if arr[j]<=pivot:
            i = i+1
            arr[i] ,arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[j],arr[i]
    return (i+1)
### 选择排序
A = [5,3,2,1,6,4]
for i in range(len(A)):
    min_idx = i
    for j in range(i+1,len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i],A[min_idx] = A[min_idx],A[i]


### 冒泡排序
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

### 归并排序

### 堆排序

### 计数排序

### 希尔排序

### 拓扑排序





