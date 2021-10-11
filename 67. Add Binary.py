class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, res = 0, 0
        a_right, b_right = len(a)-1, len(b)-1
        output = ""
        
        while a_right >= 0 or b_right >= 0:
            a_int, b_int = 0, 0
            if a_right >= 0:
                a_int = int(a[a_right])
                a_right -= 1
            
            if b_right >= 0:
                b_int = int(b[b_right])
                b_right -= 1
            
            if a_int + b_int + carry == 3:
                res, carry = 1, 1
            elif a_int + b_int + carry == 2:
                res, carry = 0, 1
            else:
                res, carry = a_int + b_int + carry, 0
            
            output += str(res)
        if carry:
            output += str(carry)
        
        return output[::-1]
