#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/6 23:00
# @Author  : Shawn
# @File    : 16ThreeSumClosest.py
# @Classes :

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []

        nums.sort()
        closest = None
        closest_distance = float('inf')

        for i in range(len(nums[:-2])):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                elif current_sum == target:
                    return target

                current_distance = abs(current_sum - target)
                if current_distance < closest_distance:
                    closest = current_sum
                    closest_distance = current_distance

        return closest