# Key idea here is that incrementing 
# n-1 values = decrementing one value.
# Then, just find how many times you need to decrement.

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-len(nums)* min(nums)
