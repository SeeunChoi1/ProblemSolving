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

    '''
    **********************************
    Use Hash Table
    **********************************
    class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        ans = 0
        
        for n in nums:
            if k-n in dic and dic[k-n]>0:
                # k-n이 있다면 n은 dic에 넣을 필요 없음 (넣어도 꺼내서 써야되니까)
                ans += 1
                dic[k-n] -= 1
            elif n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
            print(dic)
        return ans
    '''