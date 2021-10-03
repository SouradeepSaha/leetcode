class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            for str in strs:
                if i >= len(str) or str[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans
