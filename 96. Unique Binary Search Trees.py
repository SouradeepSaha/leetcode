class Solution:
    def numTrees(self, n: int) -> int:
        cache = {0:1, 1:1}
        
        for i in range(2,n+1):
            cache[i] = 0
            for j in range(i):
                cache[i] += cache[j]*cache[i-j-1]
        
        return cache[n]
