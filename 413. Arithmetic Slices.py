class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        # Pre compute the difference array
        diff = [0 for i in range(n-1)]
        for i in range(1, n):
            diff[i-1] = nums[i]-nums[i-1]
        
        result, i = 0, 0
        start = 0
        while i < n-1:
            if diff[i] == diff[i-1]:
                result += i-start
            else:
                start = i
            i += 1
            
        return result
