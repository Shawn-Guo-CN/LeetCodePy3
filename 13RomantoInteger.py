#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 22:49
# @Author  : Shawn
# @File    : 13RomantoInteger.py


class Solution:

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        roman2decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i, char in enumerate(s):
            if i == 0 or roman2decimal[char] <= roman2decimal[s[i - 1]]:
                result += roman2decimal[char]
            else:
                result += roman2decimal[char] - 2 * roman2decimal[s[i - 1]]

        return result


if __name__ == '__main__':
    sol = Solution()
    x = 'XIII'
    print(sol.romanToInt(x))
