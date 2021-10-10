class Solution:
    def backtrack(self, visited, cur, rem):
        if not rem:
            self.res.append(cur.copy())
            return 
        
        for ind, num in enumerate(self.nums):
            if not visited[ind]:
                visited[ind] = True
                cur.append(num)
                self.backtrack(visited, cur, rem-1)
                cur.pop()
                visited[ind] = False
        
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res, self.nums = [], nums
        visited = [False for num in nums]
        self.backtrack(visited, [], len(nums))
        return self.res
