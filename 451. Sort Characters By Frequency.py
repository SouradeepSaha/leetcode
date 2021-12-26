import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        c, pq = Counter(s), []
        
        for key, val in c.items():
            heapq.heappush(pq, (-val, key))
        
        output = ""
        while len(pq):
            freq, letter = heapq.heappop(pq)
            output += letter*(-freq)
        
        return output
