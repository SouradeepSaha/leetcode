class Number:
    def __init__(self, num):
        self.num = str(num)
    
    def __lt__(self, other):
        if len(self.num) == len(other.num):
            return self.num < other.num
        
        return self.num+other.num < other.num+self.num
        
    def __repr__(self):
        return self.num


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numbers = []
        for num in nums:
            numbers.append(Number(num))
        
        res = ""
        numbers.sort(reverse=True)
        for number in numbers:
            res += number.num
        
        return "0" if int(res) == 0 else res
