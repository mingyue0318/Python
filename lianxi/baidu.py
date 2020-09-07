'''
Description: 
version: 
Author: sueRim
Date: 2020-09-04 23:48:09
LastEditors: sueRim
LastEditTime: 2020-09-04 23:48:32
'''
    n, m, k = map(int, input().strip().split())
    gifts = []
    for _ in range(n):
        gift = list(map(int, input().strip().split()))
        gifts.append(gift)
    gifts = sorted(gifts, key=lambda x: (-x[2], x[0]))
    print(gifts)
    count = 0
    prices = 0
    weights = 0
    for gift in gifts:
        price, weight, v = gift
        if prices + price <= k and weights + weight <= m:
            count += 1
            prices += price
            weights += weight
        else:
            break
    print(count)