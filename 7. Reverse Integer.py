class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = x if x >= 0 else -1*x

        power, res, i = 1, 0, 0
        while int(x / power):
            power *= 10
        power = int(power / 10)
        while x:
            if (i == 10 and int(x / power) > 2) or res >= pow(2,31)-1-(int(x / power) * pow(10, i)):
                return 0
            res += int(x / power) * pow(10, i)
            i += 1
            x = x % power
            power = int(power / 10)

        return res * sign


s = Solution()
print(s.reverse(100))
