#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/20 13:45
# @Author  : sunbcy
# @File    : 2 山脉的个数,攀登者1.py
# @Software: PyCharm

def count_peaks(hill_map):
    count = 0
    for i in range(len(hill_map)):
        if i == 0 and hill_map[i] > hill_map[i+1]:
            count += 1
        if i == len(hill_map) - 1 and hill_map[i] > hill_map[i-1]:
            count += 1
        if i > 0 and i < len(hill_map) - 1 and hill_map[i] > hill_map[i-1] and hill_map[i] > hill_map[i+1]:
            count += 1
    return count

print(count_peaks([0, 1, 2, 4, 3, 1, 0, 0, 1, 2, 3, 1, 2, 1, 0]))
