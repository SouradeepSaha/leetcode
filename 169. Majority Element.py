class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        nums.sort()
        if len(nums) < 3:
            return nums[0]
        count = 0
        for i in range(len(nums)-1):
            count += 1
            
            if nums[i] != nums[i+1]:
                if count > len(nums)//2:
                    return nums[i]
                count = 0
        return nums[-1]
        '''
        # Boyer moore voting algorithm O(n)
        
        majority_elem, count = nums[0], 0
        for num in nums:
            if num == majority_elem:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority_elem = num
                    count = 1
        
        return majority_elem
