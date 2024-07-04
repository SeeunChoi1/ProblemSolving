class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev = 0
        ans = 0
        for alt in range(len(gain)):
            next = prev + gain[alt]
            ans = next if next > ans else ans
            prev = next
        return ans

