from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for a in arr:
            cnt = dic.get(a, 0)
            dic[a] = cnt + 1
        values = dic.values()
        return len(values) == len(set(values))


