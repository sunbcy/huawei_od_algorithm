#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 18:59
# @Author  : sunbcy
# @File    : 6 密码输入检测.py
# @Software: PyCharm
input_str = input()

result = ""

is_big = False
is_small = False
is_num = False
is_spec = False

for c in input_str:
    if c == '<':
        result = result[:-1]
    else:
        result += c

for c in result:
    if c.isdigit():
        is_num = True
    elif c.islower():
        is_small = True
    elif c.isupper():
        is_big = True
    else:
        is_spec = True


flag_res = len(result) >= 8 and is_num and is_big and is_small and is_spec

print(result + "," + str(flag_res).lower())
