class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ban = max(piles)
        ans = math.inf
        low, high = 1, max_ban
        
        while low <= high:
            mid = (low+high) // 2
            
            time = 0
            for x in piles:
                time += math.ceil(x/mid)
            
            if time > h:
                low = mid+1
            else:
                ans = min(ans, mid)
                high = mid-1
            
        
        return ans
