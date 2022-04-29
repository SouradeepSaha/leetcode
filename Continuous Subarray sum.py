class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = dict()
        cursum = 0
        for index, num in enumerate(nums):
            cursum += num
            if cursum % k == 0 and index != 0:
                return True
            if cursum % k in rem:
                if index-rem[cursum % k] >1:
                    return True 
            else:
                rem[cursum % k] = index
        return False
