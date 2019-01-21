#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 23:29
# @Author  : Shawn
# @File    : 15ThreeSum.py


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        nums.sort()

        if nums is None or len(nums) == 0 or nums[-1] < 0 or nums[0] > 0:
            return []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            residual = 0 - num
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == residual:
                    results.append([num, nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < residual:
                    j += 1
                else:
                    k -= 1

        return results


if __name__ == '__main__':
    sol = Solution()
    x = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(x))
