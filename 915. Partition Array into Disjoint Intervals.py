class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        local_max, next_local_max = 0,0
        ans = 1
       
        for i in range(1, len(nums)):
            # Save the next local max value
            if nums[i] > nums[next_local_max]:
                next_local_max = i
            
            # In this case, set the local_max to the previously stored max
            elif nums[i] < nums[local_max]:
                local_max = next_local_max
                
                # This is crucial, can't return local_max
                ans = i+1
        
        return ans
