from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque()
        cur, maxlen = len(s), 0
        
        for ind, char in enumerate(s):
            if char == '(':
                stack.append(ind)
            else:
                if len(stack) and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(ind)
        
        if not len(stack):
            return len(s)
        
        stack.appendleft(-1)
        while len(stack):
            temp = stack.pop()
            maxlen=max(maxlen, cur-temp-1)
            cur = temp
        
        return maxlen
                
# Using dynamic Programming                
def longestValidParentheses(self, s):
    dp, stack = [0]*(len(s) + 1), []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                p = stack.pop()
                dp[i + 1] = dp[p] + i - p + 1
    return max(dp)
