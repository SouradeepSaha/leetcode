class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = 0, -math.inf
        
        for i, num in enumerate(nums):
            if curSum + num >= 0:
                curSum += num
                maxSum = max(maxSum, curSum)
            else:
                maxSum = max(maxSum, num)
                curSum = 0

        return maxSum
