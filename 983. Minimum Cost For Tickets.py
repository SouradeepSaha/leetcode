class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
      # Time complexity: O(n^2)
      # Space Complexity: O(n)
      
      # For each day we are travelling, check if cost can be minimized
      # By using previous day
      
        n = len(days)
        dp = [9999 for i in range(n+1)]
        dp[0] = 0
        
        for i in range(1,n+1):
            dp[i] = min(dp[i], dp[i-1]+costs[0])
            for j in range(i):
                if days[i-1]-days[j] < 7:
                    dp[i] = min(dp[i], dp[j]+costs[1])
                
                if days[i-1]-days[j] < 30:
                    dp[i] = min(dp[i], dp[j]+costs[2])
            
        return dp[n]
      
     
    
