class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return math.log2(n).is_integer() if n>0 else False
