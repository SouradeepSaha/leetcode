class Solution:
    def sumUp(self, sum, dividend, res, divisor):
        tempRes, temp = 1, divisor
        while dividend-sum > divisor:
            sum += temp
            temp += temp
            res += tempRes
            tempRes += tempRes
        return [sum, res]


    def sumDown(self, sum, dividend, res, divisor):
        tempRes, temp = 1, divisor
        while sum-dividend > 0:
            sum -= temp
            temp += temp
            res -= tempRes
            tempRes += tempRes
        return [sum, res]
    
    def divide(self, dividend: int, divisor: int) -> int:
        pos = True
        if dividend < 0:
            pos = not pos
            dividend = abs(dividend)
        if divisor < 0:
            pos = not pos
            divisor = abs(divisor)

        sum, res = divisor, 1

        cur = self.sumUp(sum, dividend, res, divisor)
        sum, res = cur[0], cur[1]

        while sum-dividend > 0:
            cur = self.sumDown(sum, dividend, res, divisor)
            sum, res = cur[0], cur[1]

            if dividend-sum >= divisor:
                cur = self.sumUp(sum, dividend, res, divisor)
                sum, res = cur[0], cur[1]
                
        if not pos:
            res = 0-res
        
        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        return res
    
