class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        diff = [capacity[i]-rocks[i] for i in range(n)]

        diff.sort()
        result = 0
        i = 0
        while i < len(diff):
            additionalRocks -= diff[i]
            if additionalRocks >= 0:
                result += 1
                i += 1
            else: 
                break
        
        return result
            
