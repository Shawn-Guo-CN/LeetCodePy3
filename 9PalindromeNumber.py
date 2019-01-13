#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 21:23
# @Author  : Shawn
# @File    : 9PalindromeNumber.py


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        original_num = x
        reverse_num = 0

        while not original_num == 0:
            reverse_num *= 10
            reverse_num += original_num % 10
            original_num //= 10

        return reverse_num == x


if __name__ == '__main__':
    sol = Solution()
    x = 121
    print(sol.isPalindrome(x))
