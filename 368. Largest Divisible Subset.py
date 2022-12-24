class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1 for i in range(n)]
        parent = [-1 for i in range(n)]

        maxVal = -1
        maxInd = -1

        nums.sort()
        for i in range (n):
            for j in range(i):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1+dp[j]
                        parent[i] = j
            
            if dp[i] > maxVal:
                maxVal = dp[i]
                maxInd = i
        
        result = []
        while maxInd >= 0:
            result.append(nums[maxInd])
            maxInd = parent[maxInd]
        
        return result
