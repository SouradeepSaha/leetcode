class Solution:
    def isValid(self, s: str) -> bool:
        paren = ['(', '{', '[']
        match = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in paren:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != match[c]:
                    return False
                else:
                    stack.pop(-1)
        if len(stack) != 0:
            return False
        return True
