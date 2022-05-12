class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        # Trick: add $ to avoid overlap 
        newStr = s+"$"+s[::-1]
        f = [0 for _ in newStr]
        
        left, right = 0, 1
        
        while right < len(f):
            if newStr[left] == newStr[right]:
                f[right] = left+1
                left += 1
                right += 1
            elif left > 0:
                left = f[left-1]
            else:
                f[right] = 0
                right += 1
        
        header = newStr[len(s)+1: len(newStr)-f[-1]]
        return header + s
                
