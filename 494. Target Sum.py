# Dynamic Programming, space: O(tn), time: O(tn)
# t = sum of the array, since at max we will have
# 2t different calls

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = dict()
        
        def backtrack(index, t):
            if index == len(nums):
                return 1 if not t else 0
            if (index, t) not in cache:
                cache[(index, t)] = backtrack(index+1, t-nums[index]) + backtrack(index+1, t+nums[index])
            return cache[(index, t)]
            
        return backtrack(0, target)
        
