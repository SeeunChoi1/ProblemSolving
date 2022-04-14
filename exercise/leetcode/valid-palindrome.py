class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower().replace(" ", "")
        newS = ''.join(char for char in s if char.isalnum())
        reverseS = newS[::-1]
        print(newS)
        print(reverseS)
        
        return newS==reverseS