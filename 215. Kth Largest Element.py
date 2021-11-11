# Quickselect Algorithm
# Time complexity: O(n) average, O(n^2) worst case
class Solution:
    # Using manual quickselect algorithm and rightmost
    # element as pivot, very slow
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        
        left, right, pivot = 0, len(nums)-1, -1
        
        while len(nums)-k != pivot:
            leftIndex, rightIndex= left, right-1
            
            while leftIndex < rightIndex:
                if nums[leftIndex] > nums[right] and nums[rightIndex] <= nums[right]:
                    nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
                
                if nums[leftIndex] <= nums[right]:
                    leftIndex += 1
                
                if nums[rightIndex] > nums[right]:
                    rightIndex -= 1
            
            pivot = leftIndex
            if nums[leftIndex] < nums[right]:
                pivot += 1
            nums[pivot], nums[right] = nums[right], nums[pivot]
            
            if len(nums)-k < pivot:
                left, right = left, pivot-1
            
            elif len(nums)-k > pivot:
                left, right = pivot+1, right
                
        return nums[len(nums)-k]
    

    # Using random integer as pivot, very fast
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
            
