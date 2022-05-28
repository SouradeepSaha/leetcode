class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        listlen = len(original)
        if listlen % m or listlen % n or m*n != listlen:
            return []
        return[[ original[i+j] for j in range(n)] for i in range(0, len(original), n)]
