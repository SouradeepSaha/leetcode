class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = dict()
        
        def recurse(i,j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            
            if (i,j) not in cache:
                if s[i] == t[j]:
                    cache[(i,j)] = recurse(i+1, j+1) + recurse(i+1, j)
                else:
                    cache[(i,j)] = recurse(i+1,j)
            
            return cache[(i,j)]
        
        return recurse(0,0)
