#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 22:08
# @Author  : Shawn
# @File    : 12IntegertoRoman.py


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        decimals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        for i in range(len(romans)):
            while num >= decimals[i]:
                num -= decimals[i]
                result += romans[i]
        return result


if __name__ == '__main__':
    sol = Solution()
    x = 1234
    print(sol.intToRoman(x))
