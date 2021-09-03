# 4. Median of Two Sorted Arrays

from typing import List


class Solution:
    
    # Time Complexity: O(log(min(nums1, nums2))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # nums1 is the smaller array and nums2 is the larger array
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        low, high = 0, len(nums1)

        while low <= high:
            nums1part = int((low+high)/2)
            nums2part = int((len(nums1) + len(nums2) + 1)/2) - nums1part

            #print(nums1part, nums2part, sep=" ")

            maxleft1 = -99999999 if nums1part == 0 else nums1[nums1part-1]
            maxleft2 = -99999999 if nums2part == 0 else nums2[nums2part-1]

            minright1 = 99999999 if nums1part == len(nums1) else nums1[nums1part]
            minright2 = 99999999 if nums2part == len(nums2) else nums2[nums2part]

            if maxleft1 <= minright2 and maxleft2 <= minright1:
                if (len(nums1) + len(nums2)) % 2:
                    return max(maxleft1, maxleft2)
                else:
                    return (max(maxleft1, maxleft2) + min(minright2, minright1)) / 2
            elif maxleft1 > minright2:
                high = nums1part - 1
            else:
                low = nums1part + 1
