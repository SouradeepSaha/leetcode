class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {coin:1 for coin in coins}
        dp[0] = 0
        for i in range(amount+1):
            if i not in dp:
                counts = [1+dp[i-c] for c in coins if i-c in dp]
                if len(counts):
                    dp[i] = min(counts)
        
        return dp[amount] if amount in dp else -1
