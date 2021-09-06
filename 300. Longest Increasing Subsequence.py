# 300. Longest Increasing Subsequence
# Time Complexity: O(nlog(n)) using patience sorting

from typing import List


class Solution:
    def BinarySearch(self, arr, x):
        low, high = 0, len(arr) - 1

        while 0 <= low <= high < len(arr):
            mid = int((low + high) / 2)
            if arr[mid] == x:
                return mid
            elif x > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return high + 1

    def lengthOfLIS(self, nums: List[int]) -> int:
        dist = []

        for val in nums:
            if len(dist) == 0 or val > dist[-1]:
                dist.append(val)
            elif val < dist[0]:
                dist[0] = val
            else:
                index = self.BinarySearch(dist, val)
                dist[index] = val

        return len(dist)
