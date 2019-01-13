#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 22:04
# @Author  : Shawn
# @File    : 11ContainerWithMostWater.py


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, max_area = 0, len(height) - 1, 0

        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
