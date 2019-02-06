#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/6 23:03
# @Author  : Shawn
# @File    : 17LetterCombinationsofaPhoneNumber.py
# @Classes :


class Solution:
    def __init__(self):
        self.num2letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        self.results = []

    def combine(self, combination, digits):
        if not digits:
            self.results.append(combination)

        else:
            for char in self.num2letter[digits[0]]:
                self.combine(combination + char, digits[1:])

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits:
            self.combine('', digits)
        return self.results
