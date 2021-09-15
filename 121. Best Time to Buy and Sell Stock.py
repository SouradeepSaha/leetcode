class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        maxprof = 0
        left, right = 0, 1
        while right <len(prices):
            if prices[right] < prices[left]:
                left += 1
            else:
                if prices[right] - prices[left] > maxprof:
                    maxprof = prices[right] - prices[left]
                right += 1
        return maxprof
        
