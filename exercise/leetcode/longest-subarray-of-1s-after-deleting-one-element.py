class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        ans = 0
        zero_cnt = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            if zero_cnt > 1:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            ans = ans if ans > right - left + 1 else right - left + 1

        return ans - 1

        # while right < len(nums):
        #     print(nums[left:right+1], left, right, ans, is_deleted, zero_cnt)
        #     if nums[right] == 0:
        #         zero_cnt += 1
        #         if zero_cnt > 1:
        #             left += 1
        #             right = left
        #             is_deleted = False if nums[left] == 0 else True
        #             zero_cnt = 0 if nums[left] == 0 else 1
        #         else:
        #             if not is_deleted:
        #                 is_deleted = True
        #             else:
        #                 left += 1
        #                 right = left
        #                 is_deleted = True if nums[left] == 0 else False
        #                 zero_cnt = zero_cnt+1 if nums[left] == 0 else zero_cnt
        #     tmp_ans = right-left+1 if not is_deleted else right-left
        #     ans = ans if ans>tmp_ans else tmp_ans
        #     right += 1
        # print('end', nums[left:right+1], left, right, ans, is_deleted, zero_cnt)
        # if not is_deleted:
        #     ans -= 1
        # return ans

