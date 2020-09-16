'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-09-07 10:14:43
LastEditors: sueRimn
LastEditTime: 2020-09-11 15:52:39
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


## 指定范围的素数

lower = 23
upper = 67
for num in range(lower,upper+1):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

### 阶乘

num = 32
factorial = 1
if num<0:
   print('无阶乘')
elif num==0:
    print('1')
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print(factorial)


for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(i,j,i*j),end="")
    print()

### 斐波那切数列
nterms = 9

n1=0
n2=1
count = 2

if nterms<0:
    print('输入一个正在数')
elif nterms == 1:
    print(n1)
else :
    print('斐波那切数列')
    print(n1,',',n2,end=" , ")
    while nterms > count:
        nth = n1 + n2
        print(nth,end=" , ")
        n1 = n2
        n2 = nth
        count +=1

### 阿姆斯特朗数
### 153 = 1**3 + 5**3 + 3**3

num = 153
sum = 0
n = len(str(153))
for i in range(n):
    sum += int(str(num)[i])**n
    print(sum)
print(sum)
if(sum == num):
    print(1)
else:
    print(0)


### 递归斐波那切数列

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
    
nterms = 15

if nterms<=0:
    print('输入正确的数字')
else:
    for i in range(nterms):
        print(recur_fibo(i))


### 文件Io

with open('test.txt',"wt") as out_file:
    out_file.write('该文本会写入到文件中\n看到我了吧！')
with open('test.txt','rt') as in_file:
    text = in_file.read()

print(text) 

### 判断字符串
str = "runoob.com"

print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r


### 字符串 大小写转换

str = "www.runoob.com"

print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())

### 计算每个月的天数
import calendar
monthRange = calendar.monthrange(2020,9)
print(monthRange)

### 获取昨天日期
import datetime

def getYesterday():
    today = datetime.date.today()
    print(today)
    oneday = datetime.timedelta(days=1)
    print(oneday)
    yesterday = today - oneday
    return yesterday

print(getYesterday())


### list 常用操作
#定义
list = ['a','b','mplilgrim','z','example']
#负数索引
# 增加元素
list.append('new')
list.insert('2','new')
list.extend(['two','elements'])
# 搜索
list.index('example');
'c' in list
# 删除元素
list.remove('z')
list.remove('new') # 删除首次出现的一个值
list.remove('iiii') # 报错
list.pop() #删除最有一个元素 并返回
# 运算符
+ += *
# list -> 字符串
join #元素为字符串

# 分割字符串

split(';',1)
#映射解析

list = [1,9,4,5,3]

[i*2 for i in list]

#dictionnary 中的解析

params = {'server'':'mplilgrim','database':'master','uid':'sa','pwd':'secret'}

params.keys()
params.values()
params.items()

[k for k,v in params.items()]


#过滤



### 约瑟夫生者死者小游戏
# 30ren  数1-9 第9个人下 循环  最后剩15个人

people = {}

for i in range(1,31):
    people[i] = 1

i = 1;
j = 0;
check = 0

while i <=31:
    if i == 31:
        i = 1
    elif j == 15:
        break
    else:
        if people[i] ==0:
            i+=1
            continue
        else: 
            check+=1
            if check == 9:
                people[i] = 0
                check = 0
                print('{}号下船了'.format(i))
                j+=1
            else:
                i+=1
                continue

### 五人 分鱼

def main():
    fish = 1
    while True:
        total,enough = fish,True
        for _ in range(5):
            if (total -1)%5 ==0:
                total = (total-1)//5*4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish+=1
if __name__ == "__main__":
    main()

### 实现秒表功能

import time

print("按下回车开始计时，按下 Ctrl + C 停止计时")

while True:
    input('')
    starttime = time.time()
    print('kaishi')
    try:
        while True:
            print('计时：',round(time.time()-starttime,0),'秒',end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime= time.time()
        print('总共的时间为：',round(endtime - starttime,2),'secs')
        break

### 字符串翻转

s = '12345'

''.join(reversed(s))

s[::-1]

### 字符串片段反转

def rotate(s,d):
    head = s[0:d]
    tail = s[d:]
    return tail + head

### 移除字典中的键值对

di = {
    'name':'puppy',
    'age':'30',
    'honor':'dota2'
}

new_di = {key:val for key,val in di.items() if key!='age'}

print(new_di)

del xxx

di.pop()


### 合并字典

dict1 = {
    'name':'sumail'
}

dict2 = {
    'honor':'dota2'
}

dict2.update(dict1)

merge = {**dict1,**dict2}

### 将字符串的时间转换为时间戳

import time

t1 = "2019-5-10 23:40:00"
#时间数组
timeArray = time.strptime(t1,'%Y-%m-%d %H:%M:%S')
print(timeArray)
# 时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

### 获取几天前的时间
import time
import datetime

#时间数组
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
print(threeDayAgo)
#转化为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
print(timeStamp)
#转换为其他格式
otherStyleTime = threeDayAgo.strftime('%Y-%m-%d %H:%M:%S')
print(otherStyleTime)



import time
import datetime
 
#给定时间戳
timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAgo = dateArray - datetime.timedelta(days = 3)
print(threeDayAgo)


