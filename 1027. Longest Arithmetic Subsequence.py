# 1027. Longest Arithmetic Subsequence
# Time Complexity: O(n^2)

from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dist = dict()
        globmax = 2
        for outer in range(len(nums)):
            inner = 0
            dist[nums[outer]] = dict()
            while inner < outer:
                diff = nums[outer] - nums[inner]
                if diff in dist[nums[inner]]:
                    curmax = dist[nums[inner]][diff] + 1
                    dist[nums[outer]][diff] = curmax
                    if curmax > globmax:
                        globmax = curmax
                else:
                    dist[nums[outer]][diff] = 2

                inner += 1
        return globmax


s = Solution()
print(s.longestArithSeqLength([3,6,9,12]))
