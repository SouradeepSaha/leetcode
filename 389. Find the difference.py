class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # Xor solution - the duplicates cancel out, O(1) time
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)
        
        """
        # Hash map solution - O(n) space
        c, d = Counter(s), Counter(t)
        for char in t:
            if char not in d or c[char] != d[char]:
                return char
        """
