# 41. First Missing Positive
# Space O(1), time O(n)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        
        for i in range(l): # Get rid of useless elements
            if nums[i] < 1 or nums[i] > l:
                nums[i] = l+2
        
        for i in range(l): # Mark valid elements
            temp = abs(nums[i])-1
            if abs(temp) <= l:
                nums[temp] = nums[temp] if nums[temp] < 0 else -1 * nums[temp]
                
        for i in range(l): # Return first invalid element
            if nums[i] > 0:
                return i+1
            
        return l+1
