#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/20 16:15
# @Author  : sunbcy
# @File    : 4 用连续自然数之和来表达整数.py
# @Software: PyCharm


target = int(input())
print(target, '=', target, sep='')

expressions = []

for i in range(1, target):
    sum = 0
    ss = ''
    for j in range(i, target):
        sum += j
        ss += str(j) + "+"
        if sum == target:
            expressions.append(str(target) + "=" + ss[: -1])
            break

expressions.sort(key=lambda s: len(s))

for expression in expressions:
    print(expression, sep='')

print("Result:", len(expressions) + 1, sep='')
