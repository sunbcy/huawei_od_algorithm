#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/20 14:33
# @Author  : sunbcy
# @File    : 3 构成指定长度字符串的个数,字符串拼接.py
# @Software: PyCharm
from collections import defaultdict

def generate_distinct_strings(s, length, current, result, used):
    """
    用了递归和回溯的思想来生成不同的字符串
    :param s: 可用字符集
    :param length: 目标字符串长度
    :param current: 当前已生成的字符串
    :param result: 已生成的结果集
    :param used: 标记数组--用于查询每个字符是否已被使用
    :return:
    """
    if len(current) == length:
        result.add(current)
        return

    for i in range(len(s)):
        if used[i] or (len(current) > 0 and current[-1] == s[i]):
            continue
        used[i] = True
        generate_distinct_strings(s, length, current + s[i], result, used)
        used[i] = False

def count_distinct_strings(s, length):
    distinct_strings = set()
    used = [False] * len(s)
    generate_distinct_strings(s, length, "", distinct_strings, used)

    return len(distinct_strings)

input_str = input()
parts = input_str.split(" ")
s = parts[0]
length = int(parts[1])

count = count_distinct_strings(s, length)
print(count)
