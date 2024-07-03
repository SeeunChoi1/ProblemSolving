from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 1
        ans = sum(nums[0:0 + k]) / k
        avg = sum(nums[0:0 + k]) / k
        while left + k <= len(nums):
            avg = avg - (nums[left - 1] / k) + (nums[left + k - 1] / k)
            ans = avg if avg > ans else ans
            left += 1
        return ans
