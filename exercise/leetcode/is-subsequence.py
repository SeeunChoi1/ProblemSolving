class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        # t 순회
        # s[index] 있으면 넘어감
        # index랑 s길이 비교

        if not s:
            return True

        for elem in t:
            if elem == s[index]:
                index += 1
            if index == len(s):
                return True
        else:
            return False
