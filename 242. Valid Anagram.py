class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s, freq_t = defaultdict(int), defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            freq_s[s[i]] += 1
            freq_t[t[i]] += 1
        
        return freq_s == freq_t
