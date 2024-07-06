from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 1에는 있지만 2에는 없는거
        # 2에는 있지만 1에는 없는거
        set1 = set(nums1)
        set2 = set(nums2)
        return [set1 - set2, set2 - set1]

