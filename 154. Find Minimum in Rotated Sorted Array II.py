class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            if nums[left] < nums[-1]:
                return nums[left]
            mid = left + int((right-left)/2)
            
            if nums[0] < nums[mid]:
                left = mid+1
            elif nums[0] > nums[mid]:
                right = mid
            else:
                left += 1
        
        return nums[left]
