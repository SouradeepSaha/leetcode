class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time: O(n), Space: O(n)
        # Approach: Compute Prefix Sum
        #   Store prefix sum in a map, so that prefixSum-k
        #   Can be easily queried.

        prefixMap = {0: 1}
        curSum = 0
        result = 0

        for num in nums:
            curSum += num
            if curSum-k in prefixMap:
                result += prefixMap[curSum-k]
            
            if curSum not in prefixMap:
                prefixMap[curSum] = 1
            else:
                prefixMap[curSum] += 1
        

        return result
