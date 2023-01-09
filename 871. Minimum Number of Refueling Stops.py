import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        # Greedy Solution: TC: O(nlogn), Space: O(n)
        # Approach: Traverse each station in a loop
        # At each station, store prev station to calcuate how far travelled
        # Also add all previous stations to a max heap
        # If we run out of fuel at a station, use the heap to 
        #   Extract the station with most fuel
        # Continue until all stations have been traversed

        heap = []
        fuelRem = startFuel
        prev = 0
        result = 0

        for pos,fuel in stations + [[target,0]]:
            fuelRem -= pos-prev
            while fuelRem < 0 and len(heap):
                fuelRem += -heapq.heappop(heap)
                result += 1
            
            if fuelRem < 0:
                return -1
            
            heapq.heappush(heap, -fuel)
            prev = pos

        return result
