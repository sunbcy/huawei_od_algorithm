#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 21:03
# @Author  : sunbcy
# @File    : 7 查找众数及中位数.py
# @Software: PyCharm
# 处理输入
input_str = input()
numbers = list(map(int, input_str.split()))

# 统计数字出现次数及出现最大次数
count_map = {}
for number in numbers:
    if number in count_map:
        count_map[number] += 1
    else:
        count_map[number] = 1
max_count = max(count_map.values())

# 获取出现最大次数的数字并排序
max_count_numbers = [number for number, count in count_map.items() if count == max_count]
max_count_numbers.sort()

if len(max_count_numbers) % 2 != 0:
    index = (len(max_count_numbers) + 1) // 2 - 1
    print(max_count_numbers[index])
else:
    index1 = len(max_count_numbers) // 2 - 1
    index2 = len(max_count_numbers) // 2
    print(max_count_numbers[index1] + max_count_numbers[index2] // 2)


