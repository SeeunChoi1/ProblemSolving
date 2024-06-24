import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smaller = sys.maxint
        middle = sys.maxint
        # larger = sys.maxint

        for i in range(len(nums)):
            # print(i,smaller,middle,larger)
            if smaller >= nums[i]:
                smaller = nums[i]
            elif middle >= nums[i]:
                middle = nums[i]
            # elif larger > nums[i] :
            #     larger = nums[i]
            else:
                return True
        # if smaller < middle < larger:
        #     print(smaller,middle,larger)
        #     return True
        return False



