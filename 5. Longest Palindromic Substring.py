# 5. Longest Palindromic Substring
# Time Complexity: O(n^2)

class Solution:
    def expand_centre(self, string, start, end) -> str:
        res = ""
        while start >= 0 and end < len(string) and string[start] == string[end]:
            res = string[start:end+1]
            start -= 1
            end += 1

        return res

    def longestPalindrome(self, s: str) -> str:
        cur_max = ""
        for i in range(len(s)):
            p1 = self.expand_centre(s, i, i)
            p2 = self.expand_centre(s, i, i+1)
            if len(p1) > len(cur_max):
                cur_max = p1
            if len(p2) > len(cur_max):
                cur_max = p2

        return cur_max


s = Solution()
print(s.longestPalindrome("babad"))
