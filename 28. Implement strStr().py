class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        f = [0] * len(needle)
        l, r = 0, 1
        while r < len(needle):
            if needle[l] == needle[r]:
                f[r] = l + 1
                l = l+1
                r = r+1
            elif l > 0:
                l = f[l-1]
            else:
                f[r] = 0
                r = r+1
        
        i, j = 0, 0
        while j < len(haystack):
            if needle[i] == haystack[j]:
                if i == len(needle)-1:
                    return j-(len(needle)-1)
                i += 1
                j += 1
            elif i > 0:
                i = f[i-1]
            else:
                j = j+1
        
        return -1
