# Time: O(nlog(max))
# Space: O(1)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        def mycount(num): 
            res = 0
            row, col = 0, n-1
            while row < n and col >= 0:
                if matrix[row][col] <= num:
                    res += col+1
                    row += 1
                else:
                    col -= 1
            
            return res
        
        low, high = matrix[0][0], matrix[n-1][n-1]
        while low < high:
            mid = (low+high)//2
            if mycount(mid) < k:
                low = mid+1
            else:
                high = mid
        
        return high
