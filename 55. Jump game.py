class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        maxdist = 0
        
        for i in range(len(nums)-1):
            if maxdist < i:
                return False
            
            maxdist = max(maxdist, i+nums[i])

            if maxdist >= len(nums)-1:
                return True
