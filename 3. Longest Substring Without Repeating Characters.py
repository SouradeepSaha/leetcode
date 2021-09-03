# 3. Longest Substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_len = 0, 0, 0
        visited = set()

        while right < len(s):
            if s[right] in visited:
                visited.remove(s[left])
                left += 1

            else:
                visited.add(s[right])
                right += 1
                max_len = max(len(visited), max_len)

        return max_len

