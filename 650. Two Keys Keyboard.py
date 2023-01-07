class Solution:
    def minSteps(self, n: int) -> int: 
        # TC: O(n^2)
        # Space: O(n)
        
        dp = [9999 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1):
            for j in range(1,i):
                if not i % j:
                    dp[i] = min(dp[i], dp[j]+i//j)

        return dp[n]
