# Approach 1: Iterative - faster
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
        
# Approach 2: Recursive - slower

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def recurse(i,j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i,j) not in cache:
                if text1[i] == text2[j]:
                    cache[(i,j)] = 1 + recurse(i+1,j+1)
                else:
                    cache[(i,j)] = max(recurse(i, j+1), recurse(i+1, j))
            
            return cache[(i,j)]
        
        return recurse(0,0)
