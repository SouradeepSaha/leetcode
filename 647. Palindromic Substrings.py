# Time O(n^2), space O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def checkPalindrome(string, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        
        for ind, char in enumerate(s):
            res += checkPalindrome(s, ind, ind) # For odd length
            res += checkPalindrome(s, ind, ind+1) # For even length
                
                
        return res
