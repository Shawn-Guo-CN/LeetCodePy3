#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 21:43
# @Author  : Shawn
# @File    : 10RegularExpressionMatching.py


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*' and i >= 2:
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or (
                                dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return dp[len(s)][len(p)]


if __name__ == '__main__':
    sol = Solution()
    s = "aa"
    p = "a"
    print(sol.isMatch(s, p))
