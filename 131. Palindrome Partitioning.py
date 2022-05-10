class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(word):
            #print(word)
            if len(word) <= 1:
                return True
            l, r = 0, len(word)-1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        
        def backtrack(word, arr):
            #print(word, arr)
            if word == "":
                if len(arr):
                    res.append([_ for _ in arr])
                return
            
            for i in range(1, len(word)+1):
                if isPalindrome(word[0:i]):
                    arr.append(word[0:i])
                    backtrack(word[i:], arr)
                    arr.pop()
        
        backtrack(s, [])
        return res
                
            
