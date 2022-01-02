# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid # Anything to the left including mid could be first bad version
            else:
                left = mid + 1 # The next bad version has to be to the right of mid
    
        return left

# Key Insight: To prove binary search or 
# any recursive algorithm works, 
# test on inputs of size 1 and 2 with all possibilities
# And see if it produces correct output
