from heapq import heappush, heappop, heapify
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for ind, num in enumerate(nums1):
            heappush(heap, [num+nums2[0], ind, 0])
        
        res = []
        while k > 0 and len(heap):
            x = heappop(heap)
            #print(x)
            res.append([nums1[x[1]], nums2[x[2]]])
            if x[2]+1 < len(nums2):
                heappush(heap, [nums1[x[1]]+nums2[x[2]+1], x[1], x[2]+1])
            
            k -= 1
        
        return res
