#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 23:08
# @Author  : Shawn
# @File    : 18FourSum.py
# @Classes :


class Solution:
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        nums.sort()
        self.nums = nums
        results = []
        self.find_N_sum(0, len(self.nums) - 1, target, 4, [], results)
        return results

    def find_N_sum(self, l, r, target, N, result, results):
        if r-l+1 < N or N < 2 or target < self.nums[l]*N or target > self.nums[r]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            while l < r:
                s = self.nums[l] + self.nums[r]
                if s == target:
                    results.append(result + [self.nums[l], self.nums[r]])
                    l += 1
                    while l < r and self.nums[l] == self.nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(l, r+1):
                if i == l or (i > l and self.nums[i-1] != self.nums[i]):
                    self.find_N_sum(i+1, r, target-self.nums[i], N-1, result+[self.nums[i]], results)

