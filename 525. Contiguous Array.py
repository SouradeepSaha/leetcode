class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumIndex = {0:-1}
        maxLen = 0
        curSum = 0

        # Solution Idea: Notice that we have a binary array
        # Therefore, we add 1 whenever we see a 1 and we 
        # subtract 1 whenver we see 0
        # Thus, whenever we have the same count twice
        # This means that the 1s and 0s cancel each other out
        # Only store the first index of that sum

        for ind, num in enumerate(nums):
            curSum = curSum+1 if num == 1 else curSum-1

            if curSum in sumIndex:
                maxLen = max(maxLen, ind-sumIndex[curSum])
            else:
                sumIndex[curSum] = ind
        
        return maxLen
