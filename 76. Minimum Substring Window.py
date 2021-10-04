class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output, min_len, count = "", float("inf"), dict()
        
        for c in t:
            count[c] = 1 if c not in count else count[c] + 1
            
        full, req = 0, len(count)
        
        left, right = 0, 0
        while right < len(s):
            cur = s[right]
            if cur in count:
                count[cur] -= 1
                if count[cur] == 0:
                    full += 1
            
            while full == req and left <= right:
                if right-left+1 < min_len:
                    min_len = right-left+1
                    output = s[left:right+1]
                    
                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] > 0:
                        full -= 1
                left += 1
                
            right += 1
                    
        return output
