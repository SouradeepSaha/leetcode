class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ht_s, ht_t = dict(), dict()
        for ind, char in enumerate(s):
            if char not in ht_s:
                if t[ind] in ht_t:
                    return False
                ht_s[char] = t[ind]
                ht_t[t[ind]] = char
            elif char in ht_s and ht_s[char] != t[ind]:
                return False
        
        return True
        
