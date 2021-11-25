# Digital Root - repeated sum of all digits
# This is equal to the number % 9
# Trick math problem

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num % 9 == 0:
            return 9
        
        return num % 9
