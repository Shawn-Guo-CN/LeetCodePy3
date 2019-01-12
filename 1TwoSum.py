#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 17:52
# @Author  : Shawn
# @File    : 1TwoSum.py


class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}

        for index, num in enumerate(nums):
            if target - num in map:
                return [map[target - num], index]
            map[num] = index
