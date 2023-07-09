class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxm = 0
        p1, p2 = 0, len(height) - 1
        while p1 != p2:
            maxm = max(maxm, min(height[p1], height[p2]) * (p2 - p1))
            if height[p1] < height[p2]:
                p1+=1
            else:
                p2-=1
        return maxm