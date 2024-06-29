class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zero_cnt = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            if zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt-=1
                left += 1
            ans = ans if ans>right-left+1 else right-left+1
        return ans

        """
        wrong answer
        - resize가 가능하기 때문에 최대 size를 저장하게 했어야함
        - k가 없을 때, left만 하나 증가하면 됨
        """
        # while left+size<len(nums)-1:
        #     if nums[left+size] == 1:  # next idx
        #         size += 1
        #     elif nums[left+size] == 0 and k > 0:  # use k
        #         k -= 1
        #         size += 1
        #         zero_index = left+size-1
        #     elif nums[left+size] == 0 and k == 0:  # run out of k
        #         left = zero_index
        #         k += 1
        #         size -= 1
        #     print(nums[left:left+size], k, size, zero_index)
        # return size
