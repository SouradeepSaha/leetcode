from collections import deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dq = deque()
        visited = set()
        lastIndex = {}
        for ind, letter in enumerate(s):
            lastIndex[letter] = ind
        
        
        for ind, letter in enumerate(s):
            
            if letter not in visited:
                while len(dq) and dq[-1] > letter and lastIndex[dq[-1]] > ind:
                    visited.remove(dq.pop())
                
                dq.append(letter)
                visited.add(letter)
        
        res = ""
        while len(dq):
            res += dq.popleft()
        return res
