# 209. Minimum Size Subarray Sum
# Sliding Window Approach: O(n)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, cur, min_len = 0, 0, nums[0], len(nums)+1
        while left <= right < len(nums):
            if cur < target:
                right += 1
                if right < len(nums):
                    cur += nums[right]
            else:
                min_len = min(right-left+1, min_len)
                cur -= nums[left]
                left += 1
        return min_len if min_len <= len(nums) else 0
