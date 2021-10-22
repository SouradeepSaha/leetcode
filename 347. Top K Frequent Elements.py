from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
        for num in c.keys():
            buckets[c[num]].append(num)
        
        ind, output = len(nums), []
        while k and ind > 0:
            if len(buckets[ind]):
                k -= len(buckets[ind])
                output.extend(buckets[ind])
            ind -= 1
                
        return output 
