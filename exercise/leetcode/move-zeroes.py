class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        pointer = 0

        while index < len(nums) and pointer <= len(nums)-1:
            if nums[index] == 0 and index != len(nums)-1:
                while nums[pointer] == 0:
                    if pointer == len(nums)-1:  # no more non-zero
                        break
                    pointer += 1
                nums[index] = nums[pointer]
                nums[pointer] = 0
            index += 1
            pointer += 1

        '''
        1. 0이면 변경하기 -> 바꿀 숫자를 찾아야함
        2. 숫자면 변경하기 -> 0과 바꾸면  (1:1로 변경이라 다른 숫자 신경X)
        '''
        # non_zero = 0  # Pointer for non-zero elements
        #
        # # Move all non-zero elements to the front
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[i], nums[non_zero] = nums[non_zero], nums[i]
        #         non_zero += 1
        #     print(nums, non_zero)
