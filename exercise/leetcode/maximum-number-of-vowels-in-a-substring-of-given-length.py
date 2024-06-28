class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = 'aeiou'
        left = 0
        right = k
        before = 0
        for elem in s[left:right]:
            if elem in vowels:
                before += 1
        max_ans = before
        for i in range(1, len(s) - k + 1):
            after = before
            if s[left + i - 1] in vowels:
                after -= 1
            if s[right + i - 1] in vowels:
                after += 1
            before = after
            max_ans = after if after > max_ans else max_ans
        return max_ans
