class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n <= 1:
            return True
        
        allUpper, allLower = False, False

        if word[0].isupper() and word[1].isupper():
            allUpper = True
        else:
            allLower = True
        
        for i in range(1, n):
            if allUpper and word[i].islower():
                return False
            elif allLower and word[i].isupper():
                return False
        
        return True
