class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letterToWord = {}
        wordToLetter = {}

        n = len(pattern)
        wordList = s.split()
        
        if len(wordList) != n:
            return False
        
        
        for i in range(n):
            if pattern[i] not in letterToWord and wordList[i] not in wordToLetter:
                letterToWord[pattern[i]] = wordList[i]
                wordToLetter[wordList[i]] = pattern[i]
            
            elif pattern[i] in letterToWord and wordList[i] in wordToLetter:
                if letterToWord[pattern[i]] != wordList[i] or wordToLetter[wordList[i]] != pattern[i]:
                    return False
                
            else:
                return False
        
        return True
