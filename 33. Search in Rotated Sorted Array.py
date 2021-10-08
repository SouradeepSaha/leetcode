class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, 0 if nums[0] < nums[-1] else len(nums)-1
        
        while left < right:
            mid = left + int((right-left)/2)
            if nums[0] <= nums[mid]:
                left = mid+1
            else:
                right = mid
        
        if nums[left] <= target <= nums[-1]:
            left, right = left, len(nums)-1
        else:
            left, right = 0, max(0, left-1)
        
        while left <= right:
            mid = int((left+right)/2)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        
        return -1
