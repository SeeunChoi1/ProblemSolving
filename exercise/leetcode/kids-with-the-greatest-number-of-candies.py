class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # 한번 순회하면서 최댓값 구하기
        max = 0
        for c in candies:
            if c >= max:
                max = c
        # 더해서 최댓값 이상이면 true, 아니면 false
        ans = []
        for c in candies:
            if c + extraCandies >= max:
                ans.append(True)
            else:
                ans.append(False)
        return ans
