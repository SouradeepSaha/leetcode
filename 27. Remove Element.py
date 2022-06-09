class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)
        
        while left < right:
            if nums[left] != val:
                left += 1
            else:
                nums[left]=nums[right-1]
                right -= 1
        
        return right
