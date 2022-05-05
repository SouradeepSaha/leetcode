from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        dq = deque()
        for digit in num:
            if not len(dq) or dq[-1] <= digit:
                dq.append(digit)
            else:
                while k > 0 and len(dq) and dq[-1] > digit:
                    dq.pop()
                    k -= 1
                dq.append(digit)
        
        while k > 0 and len(dq):
            dq.pop()
            k -= 1
        
        res = ""
        start = False
        while len(dq):
            t = dq.popleft()
            if t != "0" and not start:
                start = True
            
            if t != "0" or start:
                res += t
        
        return res if res != "" else "0"
