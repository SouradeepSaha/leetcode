class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f_k, nums_tot, nums_len = 0, sum(nums), len(nums)
        for i in range(nums_len):
            f_k += i*nums[i]
        
        i, res = len(nums)-1, f_k
        while i > 0:
            f_k = f_k+nums_tot-nums_len*nums[i]
            res = max(res, f_k)
            i -= 1
        return res
        
