class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        dp = {}
        
        def backtrack(n, k):
            if k == 1:
                return n
            if k == n or k == 0:
                return 1
            
            if (k, n) not in dp:
                dp[(k,n)] = backtrack(n-1, k-1) + backtrack(n-1, k)
            
            return dp[(k,n)]
        
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(backtrack(i, j))
            res.append(temp)
        
        return res
