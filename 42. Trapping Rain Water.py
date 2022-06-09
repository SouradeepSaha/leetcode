# O(n) Time, O(1) Memory
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[0], height[-1]
        
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft-height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight-height[r]
        
        return res
