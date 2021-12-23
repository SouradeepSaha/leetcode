import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)
        
        while len(pq) > 1:
            a = heapq.heappop(pq)
            b = heapq.heappop(pq)
            
            heapq.heappush(pq, -abs(a-b))
        
        return 0 if not len(pq) else -heapq.heappop(pq)
