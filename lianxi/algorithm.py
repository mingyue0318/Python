'''
Descripttion: 
version: 
Author: sueRimn
Date: 2020-09-11 15:52:29
LastEditors: sueRimn
LastEditTime: 2020-09-25 09:38:31
'''

### 二分查找
arr=[1,2,3,4,5,6,7,8,9,10]

def binarySearch(arr,l,r,x):
    if r>=l:
        mid = int(l+ (r-l)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
        else:
            return binarySearch(arr,mid+1,r,x)

    else:
        return -1




### 线性查找

def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


### 插入排序
arr = [5,2,3,6,9,4]
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key< arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    
insertionSort(arr)
print(arr)
# $????
### 快速排序

def partition(arr,low,high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low,high):
        # 当前元素小于或等于pivot
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)