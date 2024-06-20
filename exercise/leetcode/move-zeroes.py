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
                    print('while >>', pointer)
                    pointer += 1
                nums[index] = nums[pointer]
                nums[pointer] = 0
            index += 1
            pointer += 1
