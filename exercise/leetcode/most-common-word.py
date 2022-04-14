import collections, re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split() 
                    if word not in banned]
        
        counts = collections.Counter(words)
        
        return counts.most_common(1)[0][0]