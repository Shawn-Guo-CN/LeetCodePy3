#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 14:59
# @Author  : Shawn
# @File    : 8StringtoInteger.py

import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        try:
            res = re.search('(^[\+\-]?\d+)', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            res = 0
        return res


if __name__ == '__main__':
    sol = Solution()
    input = "    42"
    print(sol.myAtoi(input))
