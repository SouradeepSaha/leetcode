class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        cur = num
        res = ""
        while cur > 0:
            i = 0
            while cur < ints[i]:
                i += 1
            res += romans[i]
            cur = cur - ints[i]
                

        return res
