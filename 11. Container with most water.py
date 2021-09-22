# 11. Container with most water.py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, stop = 0, len(height)-1
        max_vol = 0
        while start < stop:
            max_vol = max(max_vol, (stop-start) * min(height[start], height[stop]))
            if height[start] <= height[stop]:
                start += 1
            else:
                stop -= 1
        return max_vol
