class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        ptr = 2
        for index in range(2, len(nums)):
            if nums[index] != nums[ptr-2]:
                nums[ptr] = nums[index]
                ptr += 1
        
        return ptr
