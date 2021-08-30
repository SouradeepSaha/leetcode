class Solution:
    def twoSum(self, nums, target: int):
        hash = dict()
        n = len(nums)
        for i in range(n):
            cur = nums[i]
            if cur in hash:
                hash[cur].append(i)
            else:
                hash[cur] = [i]

        for i in range(n):
            cur = nums[i]
            comp = target-cur

            if comp in hash:
                if comp == cur and len(hash[comp]) == 2:
                    return hash[comp]
                elif comp != cur:
                    return [i, hash[comp][0]]


sol = Solution()
print(sol.twoSum([3,2,4], 6))
