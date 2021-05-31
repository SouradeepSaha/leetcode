class Solution:
    def checkPossibility(self, nums) -> bool:
        done, curmax, n = False, -999999, len(nums)

        if n < 3:
            return True

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if done:
                    return False
                if i+2 >= n:
                    return True
                elif curmax <= nums[i+1] or nums[i+2] >= nums[i]:
                    done = True
                else:
                    return False
            else:
                curmax = nums[i]

        return True
