'''
// Exceeds Memory Limit
class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        
        for i in range(2,n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]+1
            else:
                dp[i] = min(dp[i-1], 1+dp[(i+1)//2])+1
        
        return dp[n]
'''
class Solution:
    def integerReplacement(self, n: int) -> int:
        def helper(n, cache={}):
            if n < 1:
                return float('inf')
            if n == 1:
                return 0
            if n in cache:
                return cache[n]
            if n % 2 == 0:
                cache[n] = 1 + helper(n // 2)
                return cache[n]
            else:
                cache[n] =  1 + min(helper(n+1), helper(n-1))  
                return cache[n]
        
        return helper(n)
