class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]*(n+1)
        prod = 1
        for i in range(1,n+1):
            prod *= i
            factorials[i] = prod
        
        def recurse(arr, k, res):
            n = len(arr)
            if n == 0:
                return res
            cur_digit_ind = k//factorials[n-1]
            res += str(arr[cur_digit_ind])
            arr.pop(cur_digit_ind)
            return recurse(arr, k-cur_digit_ind*factorials[n-1], res)
        
        return recurse([i for i in range(1, n+1)], k-1, "")
