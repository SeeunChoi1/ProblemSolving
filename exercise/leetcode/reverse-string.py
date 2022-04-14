class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        pointer = len(s)
        ans = []
        
        for i in range(1, pointer+1):
            ans.append(s[pointer-i])
            
        for i in range(pointer):
            s[i] = ans[i]

class Solution2(object):
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

class Solution3(object):
    def reverseString(self, s: List[str]) -> None:
        s.revers()