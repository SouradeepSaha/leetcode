from collections import defaultdict
class Solution:
    
    def longestSubstring(self, s: str, k: int) -> int:
        count, breaks = defaultdict(int), set()
        
        for char in s:
            count[char] += 1
            if count[char] < k:
                breaks.add(char)
            elif char in breaks:
                breaks.remove(char)
                    
        if len(breaks) == 0 or len(s) == 0:
            return len(s)
        
        left, maxlen = 0, 0
        for i in range(len(s)+1):
            if i == len(s) or s[i] in breaks:
                print(s[left:i])
                temp = self.longestSubstring(s[left:i], k)
                print(temp)
                maxlen = max(temp, maxlen)
                left = i+1                
                
        return maxlen
