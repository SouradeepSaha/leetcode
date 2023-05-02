class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelCount = 0
        for i in range(k):
            if s[i] in 'aieou':
                vowelCount += 1
        
        maxVowelCount = vowelCount
        for i in range(k, len(s)):
            if s[i] in 'aeiou':
                vowelCount += 1
            if s[i-k] in 'aieou':
                vowelCount -= 1
            
            maxVowelCount = max(vowelCount, maxVowelCount)
        
        return maxVowelCount
