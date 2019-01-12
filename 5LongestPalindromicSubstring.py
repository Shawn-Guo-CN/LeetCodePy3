#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 23:03
# @Author  : Shawn
# @File    : 5LongestPalindromicSubstring.py

class Solution:
    # Manacher algorithm
    # http://en.wikipedia.org/wiki/Longest_palindromic_substring

    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))

        len_T = len(T)
        P = [0] * len_T
        center = right_bound = 0
        for i in range(1, len_T - 1):
            # equals to i' = C - (i-C)
            P[i] = (right_bound > i) and min(right_bound - i, P[2 * center - i])
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past right_bound,
            # adjust center based on expanded palindrome.
            if i + P[i] > right_bound:
                center, right_bound = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]

if __name__ == '__main__':
    s = "bababd"
    solution = Solution()
    ps = solution.longestPalindrome(s)
    print(ps)

