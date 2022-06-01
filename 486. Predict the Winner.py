class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        
        def recurse(i, j):
            if (i,j) not in dp:
                if i == j:
                    dp[(i,j)] = (nums[i], 0)
                else:
                    left = recurse(i, j-1)
                    right = recurse(i+1, j)
                    
                    if left[1] + nums[j] > right[1] + nums[i]:
                        dp[(i,j)] = (left[1] + nums[j], left[0])
                    else:
                        dp[(i,j)] = (right[1] + nums[i], right[0])
                    
            return dp[(i,j)]
        
        
        res = recurse(0, len(nums)-1)
        return res[0] >= res[1]
