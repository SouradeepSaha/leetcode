class Solution:
    def singleNumber2(self, nums: List[int]) -> int:
        # Bit manipulation trick:
        one, two = 0, 0 # Appears 1 or 2 times
        for num in nums:
            one = (num ^ one) & ~two
            two = (num ^ two) & ~one
        
        return one
    
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        r = 0
        while r < len(nums):
            if r == len(nums)-1 or nums[r] != nums[r+1]:
                return nums[r]
            r = r+3
