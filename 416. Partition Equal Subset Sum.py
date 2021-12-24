class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        dp = {}
        def recurse(index, cur):
            if index >= len(nums):
                return cur == s // 2
            
            if cur == s // 2:
                return True
            
            if cur not in dp:
                dp[cur] = recurse(index+1, cur+nums[index]) or recurse(index+1, cur)
            
            return dp[cur]
        
        return recurse(0,0)
