class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        last = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == last:
                nums[i] = None
            else:
                last = nums[i]
                
        l, r = 1, 2
        while r < len(nums):
            if nums[l] is not None:
                l += 1
            if nums[l] is None and nums[r] is not None:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            
            r += 1

        return l if nums[l] is None else l+1
        
