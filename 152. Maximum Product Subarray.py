# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_p, max_n, tot_max = 1, 1, -99999999
        
        for num in nums:
            t1 = max(num, num * max_p, num * max_n)
            t2 = min(num, num * max_n, num * max_p)
            max_p, max_n = t1, t2
            tot_max = max(max_p, max_n, tot_max)
            
        return tot_max
        
