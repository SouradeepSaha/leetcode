# Time Complexity: O(n)

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cur, new, steps = 0, nums[0], 0
        
        for ind, val in enumerate(nums):
            new = max(new, val+ind)
            if new >= len(nums)-1:
                return steps+1
                
            if ind == cur:
                cur, new = new, -1
                steps += 1
