class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums)-1
        ans = 0
        while left<right:
            target = nums[right]+nums[left]
            if target < k:
                left += 1
            elif target > k:
                right-=1
            elif target == k:
                ans += 1
                left += 1
                right -= 1
        return ans