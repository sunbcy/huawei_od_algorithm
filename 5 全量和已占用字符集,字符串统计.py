#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/20 17:02
# @Author  : sunbcy
# @File    : 5 全量和已占用字符集,字符串统计.py
# @Software: PyCharm

"""

"""
import sys

input = sys.stdin.readline().strip()

splitInput = input.split('@')
fullCharacterSet = splitInput[0]
ocupiedCharacterSet = splitInput[1]

characterList = []
fullCharacterSetSplit = fullCharacterSet.split(',')
