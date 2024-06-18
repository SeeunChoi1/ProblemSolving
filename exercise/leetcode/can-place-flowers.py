class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        i = 0
        while i < len(flowerbed):
            prev = flowerbed[i - 1] if i > 0 else 0
            next = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
            if prev == 0 and next == 0:
                if flowerbed[i] == 0:
                    n -= 1
                    i += 2
                    if n == 0:
                        return True
                else:
                    i += 1
            else:
                i += 1
        return False






