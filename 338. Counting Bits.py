class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        power = 1
        for i in range(1, n+1):
            ans = 1
            if i == power:
                power *= 2
            else:
                ans = res[i-power]+1
            res.append(ans)
        
        return res
