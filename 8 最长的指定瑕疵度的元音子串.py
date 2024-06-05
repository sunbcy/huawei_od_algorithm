#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 21:45
# @Author  : sunbcy
# @File    : 8 最长的指定瑕疵度的元音子串.py
# @Software: PyCharm
from typing import List
vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

def findLongestVowelSubstring(flaw: int, s:str) -> int:
    vowelIdxs = [i for i in range(len(s)) if s[i] in vowels]
    left, right = 0, 0
    lengths = []
    while right < len(vowelIdxs):
        lengthDiff = vowelIdxs[right] - vowelIdxs[left] - (right - left)
        if lengthDiff > flaw:
            left += 1
        else:
            if lengthDiff == flaw:
                lengths.append(vowelIdxs[right] - vowelIdxs[left] + 1)
            right += 1
    if not lengths:
        return 0
    return max(lengths)

flaw = int(input())
s = input()
print(findLongestVowelSubstring(flaw, s))
