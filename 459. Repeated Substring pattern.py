class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        f = [0] * len(s)
        
        l, r = 0, 1
        
        while r < len(s):
            if s[l] == s[r]:
                f[r] = l+1
                l += 1
                r += 1
            elif l > 0:
                l = f[l-1]
            else:
                f[r] = 0
                r += 1
        
        if f[-1] == 0:
            return False
        return not len(s)%(len(s)-f[-1])
