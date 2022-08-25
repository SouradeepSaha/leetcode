class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        def backtrack(left, right):
            if left >= right:
                return 0
            if dp[left][right] == 0:
                for i in range(left, right):
                    coins = backtrack(left, i) + backtrack(i+1, right) + nums[i]*nums[left-1]*nums[right]
                    dp[left][right] = max(dp[left][right], coins)
            return dp[left][right]
        
        x=backtrack(1, len(nums)-1)
        return x

# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         nums=[1]+nums+[1] 
#         n=len(nums)
#         dp=[[0] * n for _ in range(n)]
#         for gap in range(2,n):
#             for i in range(n-gap):
#                 j=i+gap
#                 for k in range(i+1,j):
#                     dp[i][j]=max(dp[i][j],nums[i]*nums[k]*nums[j]+dp[i][k]+dp[k][j])
#         return dp[0][n-1]
