class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        
        for num in nums:
            prev, cur = cur, max(num+prev, cur)
        
        return cur
        
