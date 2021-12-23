class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not len(digits):
            return [1]
        
        if digits[-1] + 1 < 10:
            digits[-1] += 1
            return digits
        
        index = len(digits)-1
        while digits[index] == 9 and index >= 0:
            digits[index] = 0
            index -= 1
        
        if index == -1:
            digits.insert(0, 1)
        else:
            digits[index] += 1
        
        return digits
            
