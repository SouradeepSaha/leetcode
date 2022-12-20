class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivotInd = -1
        i = len(nums)-1

        while i > 0:
          if nums[i] > nums[i-1]:
            pivotInd = i-1
            break
          i -= 1

        if pivotInd != -1:
          pivotElem = nums[pivotInd]
          i = len(nums) - 1
          pivot2Ind = -1
          pivot2Elem = 99999

          while i > pivotInd:
            if nums[i] > nums[pivotInd]:
              temp = nums[i]
              if (temp < pivot2Elem):
                pivot2Elem = temp
                pivot2Ind = i
            i -= 1
          
          nums[pivotInd], nums[pivot2Ind] = nums[pivot2Ind], nums[pivotInd]
        
        # Reverse the sublist from the leftmost pivot position + 1
        nums[pivotInd+1:]=nums[pivotInd+1:][::-1]
