#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 22:02
# @Author  : sunbcy
# @File    : 9 整数对最小和.py
# @Software: PyCharm
array1 = list(map(int, input().split()))[1:]

array2 = list(map(int, input().split()))[1:]

k = int(input())

pairsSum = []

for value1 in array1:
    for value2 in array2:
        pairsSum.append(value1 + value2)

pairsSum.sort()

minSum = sum(pairsSum[:k])

print(minSum)
