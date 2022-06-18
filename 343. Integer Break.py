class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {1:1}
        
        def recurse(k):
            if k not in cache:
                cache[k] = 0
                for i in range(1, k//2+1):
                    cache[k] = max(cache[k], max(i, recurse(i))*max(k-i, recurse(k-i)))
                
            return cache[k]
        
        return recurse(n)
            
        
