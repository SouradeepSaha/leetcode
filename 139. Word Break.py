class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        found = dict()
        for word in wordDict:
            found[word] = True
        
        def recurse(s):
            if s in found:
                return found[s]
            for index, char in enumerate(s):
                found[s] = found.get(s[:index+1], False) and recurse(s[index+1:])
                if found[s]:
                    return True
            
            return False
        return recurse(s)
                
