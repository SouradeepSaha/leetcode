class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        lastIndex = {}
        candidates.sort()
        for ind, num in enumerate(candidates):
            lastIndex[num] = ind        

        res = []
        def backtrack(ind, curSum, arr):
            if curSum == target:
                res.append([x for x in arr])
                return
            
            if ind < len(candidates) and curSum < target:
                freq = lastIndex[candidates[ind]]-ind+1
                
                for i in range(freq+1):
                    if i > 0:
                        arr.append(candidates[ind])
                        curSum += candidates[ind]
                    backtrack(ind+freq, curSum, arr)
                
                for i in range(freq):
                    curSum -= candidates[ind]
                    arr.pop()
        
        backtrack(0, 0, [])
        return res
