class Solution:
    def myAtoi(self, s: str) -> int:
        newStr = s.lstrip(' ')
        if not len(newStr):
            return 0

        sum, firstChar, sign, stop = 0, newStr[0], 1, 0
        strcpy = ""
        if firstChar == '+':
            sign = 1
            newStr = newStr[1:]
        elif firstChar == '-':
            sign = -1
            newStr = newStr[1:]

        strcpy = newStr
        if len(newStr) and newStr[0].isdigit():
            while len(newStr) and newStr[0].isdigit():
                stop += 1
                newStr = newStr[1:]

        if stop:
            res = sign * int(strcpy[0:stop])
            if res < -1 * pow(2, 31):
                return -1 * pow(2, 31)
            elif res > pow(2, 31) - 1:
                return pow(2, 31) - 1
            return res
        else:
            return 0

