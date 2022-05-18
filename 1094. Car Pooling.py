from heapq import heappop, heappush

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        heap = []
        passengers = 0
        
        for trip in trips:
            #print(heap)
            while len(heap) and heap[0][0] <= trip[1]:
                passengers -= heappop(heap)[1]
            
            #print(heap)
            if passengers + trip[0] <= capacity:
                heappush(heap, [trip[2], trip[0]])
                passengers += trip[0]
            else:
                return False
        
        return True
