class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)
        
        if r-l <= 1:
            return nums
        
        mid = (l+r)//2
        arr1 = self.sortArray(nums[l:mid])
        arr2 = self.sortArray(nums[mid:r])
        
        i, j, k = 0,0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                nums[k] = arr1[i]
                i += 1
            else:
                nums[k] = arr2[j]
                j += 1
            k += 1
        
        while i < len(arr1):
            nums[k] = arr1[i]
            i, k = i+1, k +1
        
        while j < len(arr2):
            nums[k] = arr2[j]
            j, k = j+1, k+1
        
        return nums
        
