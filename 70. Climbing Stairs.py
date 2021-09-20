class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        left, right = 1, 2
        for cur in range(3, n+1):
            left, right = right, left+right
        return right
            
