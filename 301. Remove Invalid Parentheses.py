class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = 0, 0
        # Calculate the exact number of mismatched parentheses
        for paren in s:
            if paren == '(' or paren == ')':
                if paren == '(':
                    left += 1
                elif left > 0:
                    left -= 1
                else:
                    right += 1
        
        result = set()
        
        def backtrack(ind, left, right, cur, stack):
            if ind >= len(s) and left == 0 and right == 0:
                result.add(cur)
            if ind < len(s):
                if s[ind] == '(':
                    if left:
                        backtrack(ind+1, left-1, right, cur, stack)
                    backtrack(ind+1, left, right, cur+s[ind], stack+1)
                elif s[ind] == ')':
                    if right:
                        backtrack(ind+1, left, right-1, cur, stack)
                    if stack:
                        backtrack(ind+1, left, right, cur+s[ind], stack-1)
                else:
                    backtrack(ind+1, left, right, cur+s[ind], stack)
                        
        backtrack(0, left, right, '', 0)
        return list(result)
