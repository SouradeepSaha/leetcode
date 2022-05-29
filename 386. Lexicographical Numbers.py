class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        n_digits = 0
        tmp = n
        while tmp:
            n_digits += 1
            tmp /= 10
        
        
        res, digits = [], [i for i in range(10)]
        def dfs(num, digit):
            if len(num) > n_digits or digit > 9 or int(num) > n:
                return
            
            res.append(num)
            dfs(num+'0', 0)
            if digit+1 < 10:
                dfs(num[:-1]+f"{digits[digit+1]}", digit+1)
        
        dfs("1", 1)
        return res
