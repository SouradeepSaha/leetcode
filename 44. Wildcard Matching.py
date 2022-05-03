class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = {}
        def recurse(sInd, pInd):
            if sInd >= len(s) and pInd >= len(p):
                dp[(sInd, pInd)] = True
            
            elif pInd >= len(p):
                dp[(sInd, pInd)] = False
            
            elif (sInd, pInd) not in dp:
                if sInd < len(s) and (s[sInd] == p[pInd] or p[pInd] == '?'):
                    dp[(sInd, pInd)] = recurse(sInd+1, pInd+1)
                elif p[pInd] == '*':
                    if sInd >= len(s):
                        dp[(sInd, pInd)] = recurse(sInd, pInd+1)
                    else:
                        dp[(sInd, pInd)] =  recurse(sInd+1, pInd) or recurse(sInd, pInd+1)
                else:
                    dp[(sInd, pInd)] = False
            
            return dp[(sInd, pInd)]
        
        return recurse(0,0)
                    
