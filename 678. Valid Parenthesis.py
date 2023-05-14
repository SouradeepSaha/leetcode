class Solution:
    def checkValidString(self, s: str) -> bool:
        # Store the max and min number of left and 
        # right parens possible
        maxLeft, minLeft = 0,0

        for char in s:
            if char == '(':
                maxLeft += 1
                minLeft += 1
            elif char == ')':
                maxLeft -= 1
                minLeft -= 1
            else:
                maxLeft += 1
                minLeft -= 1
            
            # Left paren must be >= 0
            # To handle case ))
            if maxLeft < 0:
                return False

            # To handle case (*)
            if minLeft < 0:
                minLeft = 0
        
        # At the end, minLeft must be 0
        return minLeft == 0
