class Solution:
    # Recursive Solution
    def decodeString2(self, s: str) -> str:
        index = 0
        def recurse():
            nonlocal index
            res, mult = "", ""
            
            while index < len(s) and s[index].isalpha():
                res += s[index]
                index += 1
            
            if index < len(s) and s[index].isdigit():
                while s[index].isdigit():
                    mult += s[index]
                    index += 1
                mult = int(mult)
                index += 1
                res += mult * recurse()
            
            if index >= len(s) or s[index] == ']':
                index += 1
                return res
            
            return res + recurse()
        return recurse()
    
    # Iterative Solution
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
