class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        left, right = 0, len(nums)-1
              
        while left <= right:
            mid = left + int((right-left)/2)
            if nums[mid] == target:
                output[0] = mid
            if nums[mid] >= target:
                right = mid-1
            else:
                left = mid+1
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + int((right-left)/2)
            if nums[mid] == target:
                output[1] = mid
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid-1

        return output
