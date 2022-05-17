class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        five_power = 5
        while n // five_power:
            res += n // five_power
            five_power *= 5
        
        return res
