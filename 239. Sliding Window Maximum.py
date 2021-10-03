from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq, res = deque(), []
        
        for i in range(len(nums)):
            while len(dq) and nums[dq[-1]] < nums[i]:
                    dq.pop()
            dq.append(i)
            
            if i+1 >= k:
                if i-k+1 > dq[0]:
                    dq.popleft()
                
                res.append(nums[dq[0]])
        
        return res
