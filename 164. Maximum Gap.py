from math import ceil
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        maxNum, minNum = max(nums), min(nums)
        if maxNum == minNum:
            return 0
        
        intervalSize = ceil((maxNum - minNum)/len(nums))
        intervals = ((maxNum - minNum)//intervalSize)+1
        buckets = [() for i in range(intervals)]
        
        for num in nums:
            bucketIndex = (num-minNum)//intervalSize
            if buckets[bucketIndex] == ():
                buckets[bucketIndex] = (num, num)
            else:
                prev = buckets[bucketIndex]
                buckets[bucketIndex] = (min(prev[0], num), max(prev[1], num))
        
        maxdiff, l, r= 0, 0, 1
        while r < len(buckets):
            if len(buckets[r]) != 0:
                while len(buckets[l]) == 0:
                    l += 1
                maxdiff = max(buckets[r][0] - buckets[l][1], maxdiff)
                l += 1
            r += 1
            
        
        return maxdiff
        
