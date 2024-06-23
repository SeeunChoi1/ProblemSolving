class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1 for _ in range(len(nums))]
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            ans[i] *= prefix[i]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
            ans[i] *= suffix[i]

        return ans
