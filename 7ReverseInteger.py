#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 22:12
# @Author  : Shawn
# @File    : 7Reverse Integer.py


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0

        if x < 0:
            x = -int(str(x).strip('-')[::-1])
        else:
            x = int(str(x)[::-1])

        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        else:
            return x


if __name__ == '__main__':
    sol = Solution()
    input = 1534236469
    print(sol.reverse(input))
