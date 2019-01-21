#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 23:06
# @Author  : Shawn
# @File    : 14LongestCommonPrefix.py


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = min(strs, key=len)

        for i, char in enumerate(prefix):
            for string in strs:
                if not string[i] == char:
                    return prefix[:i]

        return prefix

