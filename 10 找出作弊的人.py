#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 22:28
# @Author  : sunbcy
# @File    : 10 找出作弊的人.py
# @Software: PyCharm
n = int(input())

employees = []

for _ in range(n):
    id, score =map(int, input().split())
    employees.append((id, score))

# print(employees)
employees.sort(key=lambda x: x[1])

min_diff = float('inf')

result = []

for i in range(1, n):
    diff = employees[i][1] - employees[i - 1][1]
    if diff < min_diff:
        min_diff = diff
        result = [(employees[i-1][0], employees[i][0])]

# 对结果list 按照员工ID进行排序
result.sort()

# 打印出分差最小的员工ID对
for pair in result:
    print(pair[0], pair[1])
