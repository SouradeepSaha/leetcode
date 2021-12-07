class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []
        cache = {word: True for word in wordDict}
        
        def recurse(cur, arr):
            if cur == "" and len(arr):
                output.append(" ".join(arr))
                return
            
            temp = ""
            for ind, c in enumerate(cur):
                temp += c
                if temp in cache:
                    arr.append(temp)
                    recurse(cur[ind+1:], arr)
                    arr.pop()

            return output
        
        recurse(s, [])
        return output
    
