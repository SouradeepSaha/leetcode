import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        targetArrival = times[targetFriend][0]
        
        h1, h2, h3 = [], [], [0]
        for time in times:
            heappush(h1, time)    
        while len(h1):
            temp = heappop(h1)
            while len(h2) and h2[0][0] <= temp[0]:
                free = heappop(h2)[1]
                heappush(h3, free) 
                
            minfree = heappop(h3)
            heappush(h2, [temp[1], minfree])
            if not len(h3):
                heappush(h3, minfree+1)
            if temp[0] == targetArrival:
                return minfree
            
