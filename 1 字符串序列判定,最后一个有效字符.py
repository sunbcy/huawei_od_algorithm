#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 21:03
# @Author  : sunbcy
# @File    : 1 字符串序列判定,最后一个有效字符.py
# @Software: PyCharm
stringS = input("")
stringL = input("")

indexS = 0
indexL = 0

while indexS < len(stringS) and indexL < len(stringL):
    if stringS[indexS] == stringL[indexL]:
        indexS += 1
    indexL += 1

if indexS == len(stringS):
    print(indexL - 1)
else:
    print(-1)