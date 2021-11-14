# Dynamic programming O(n) time, O(1) space. 
# Similar to Fibonacci sequence solution

class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == '0':
            return 0
        
        oneless, twoless, cur = 1, 1, 0
        for i in range(1,len(s)):
            if s[i] != '0':
                cur = oneless
            if s[i-1] == '1' or s[i-1] == '2' and s[i] <= '6':
                cur += twoless
            
            oneless, twoless, cur = cur, oneless, 0
        
        return oneless
