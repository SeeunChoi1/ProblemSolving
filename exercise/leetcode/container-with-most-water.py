class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        **********************************
        Brute force -> Time Limit Exceeded
        **********************************
        area = 0
        for i in range(len(height)):
            for j in range(1,len(height)):
                w = j-i
                h = (min(height[i],height[j]))
                area = max(area,w*h)
        return area
        """
        ### two-pointer ###
        left, right = 0, len(height) - 1
        area = 0

        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            # Always move the pointer that points to the lower line
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return area

