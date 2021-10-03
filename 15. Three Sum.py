# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Algorithm: For each element, use 2-pointers to solve the Two sum problem.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for ind in range(len(nums)-2):
            rem = 0-nums[ind]
            if ind == 0 or nums[ind] != nums[ind-1]:
                l, r = ind+1, len(nums)-1
                while l < r:
                    if nums[l] + nums[r] == rem:
                        ans.append([nums[l], nums[r], nums[ind]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        r -= 1
                        l += 1
                    elif nums[l] + nums[r] > rem:
                        r -= 1
                    else:
                        l += 1
        
        return ans
