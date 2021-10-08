class Solution:
    def backtrack(self, curSum, arr, candidates):
        if curSum > self.target or len(candidates) == 0:
            return
        if curSum == self.target:
            self.output.append([e for e in arr])
            return
        
        arr.append(candidates[0])
        self.backtrack(curSum+candidates[0], arr, candidates)
        arr.pop()
        self.backtrack(curSum, arr, candidates[1:])
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output, self.target = [], target
        self.backtrack(0, [], candidates)
        return self.output
        
