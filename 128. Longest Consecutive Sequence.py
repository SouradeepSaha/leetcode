# 128. Longest Consecutive Sequence
# Time complexity: O(n)

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxlen = 0
        starts, ends = dict(), dict()
        elems = set()

        for num in nums:
            if num not in elems:
                elems.add(num)
                if num-1 not in ends and num+1 not in starts:
                    starts[num] = num
                    ends[num] = num

                elif num-1 in ends and num+1 in starts:
                    st = ends[num-1]
                    en = starts[num+1]
                    del ends[num-1]
                    del starts[num+1]
                    starts[st] = en
                    ends[en] = st
                    maxlen = abs(st-en) if abs(st-en) > maxlen else maxlen

                elif num-1 in ends:
                    st = ends[num-1]
                    del ends[num-1]
                    ends[num] = st
                    starts[st] = num
                    maxlen = abs(num-st) if abs(num-st) > maxlen else maxlen

                else:
                    en = starts[num+1]
                    del starts[num+1]
                    starts[num] = en
                    ends[en] = num
                    maxlen = abs(num-en) if abs(num-en) > maxlen else maxlen
        return maxlen+1

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
