class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        s1len, s2len = len(s1), len(s2)
        dp = [[False for i in range(s2len+1)] for i in range(s1len+1)]
        
        dp[0][0] = True 
        
        for i in range(0, len(s1)+1):
            for j in range(0, len(s2)+1):
                if i > 0 and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = dp[i-1][j]
                if j > 0 and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
                elif i or j: 
                    dp[i][j] = dp[i][j] or False
        return dp[len(s1)][len(s2)]
        
