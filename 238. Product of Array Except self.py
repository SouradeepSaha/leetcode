class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [nums[-1] for i in nums]
        
        # Store reverse sum in output arr
        for i in range(len(nums)-2, -1,-1):
            output[i] = output[i+1]*nums[i]
            
        cur = 1
        for i in range(len(nums)-1):
            output[i] = output[i+1] * cur
            cur *= nums[i]
        
        output[len(nums)-1] = cur
        
        return output
