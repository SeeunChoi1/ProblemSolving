class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        word = ''
        s += ' '
        for i in range(len(s)):
            if s[i] == ' ':
                if word:
                    ans.append(word)
                    word = ''
                else:
                    continue
            else:
                word += s[i]

        a = ''
        for i in reversed(range(len(ans))):
            a += ans[i]
            a += '' if i == 0 else ' '

        return a