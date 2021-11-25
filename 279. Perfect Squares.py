# Dynamic programming problem
# Reduced to coin change
# O(n) space, O(n) time

class Solution:
    def numSquares(self, n: int) -> int:
        squares, dp = [], dict()
        for i in range(1, int(sqrt(n))+1):
            squares.append(i*i)
            dp[i*i] = 1
        
        # Coin change problem
        for i in range(1, n+1):
            if i not in dp:
                sums = [dp[i-sq]+1 for sq in squares if i-sq in dp]
                if len(sums):
                    dp[i] = min(sums)
        
        return n if n not in dp else dp[n]
                 
            
            
        
        
        
