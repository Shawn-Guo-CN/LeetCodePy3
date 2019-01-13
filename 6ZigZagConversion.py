#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 14:16
# @Author  : Shawn
# @File    : 6ZigZagConversion.py

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        step = 1
        pos = 1
        lines = {}

        for c in s:
            if pos in lines:
                lines[pos] += c
            else:
                lines[pos] = c

            pos += step

            if pos == 1 or pos == numRows:
                step *= -1

        result = ""
        for i in range(1, numRows + 1):
            try:
                result += lines[i]
            except:
                return result

        return result
