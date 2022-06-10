from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        numbers = []
        freq = Counter(nums)
        for key, val in freq.items():
            numbers.append(key)
        
        res = []
        def backtrack(ind, arr):
            if ind >= len(numbers):
                res.append([x for x in arr])
                return
            
            curFreq = freq[numbers[ind]]
            for i in range(curFreq+1):
                if i>0:
                    arr.append(numbers[ind])
                backtrack(ind+1, arr)
            
            for i in range(curFreq):
                arr.pop()
        
        backtrack(0, [])
        return res
