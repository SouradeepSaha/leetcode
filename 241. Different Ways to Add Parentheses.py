class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        cache = defaultdict(list)
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        def recurse(s):
            if len(s) == 1:
                cache[s] = [int(s)]
            for i, char in enumerate(s):
                if char in '+-*':
                    left, right = s[0:i], s[i+1:]
                    if left not in cache:
                        recurse(left)
                    if right not in cache:
                        recurse(right)
                    
                    cache[s].extend([op[char](x,y) for x in cache[left] for y in cache[right]])
            if s not in cache:
                cache[s] = [int(s)]
        
        recurse(expression)
        return cache[expression]
