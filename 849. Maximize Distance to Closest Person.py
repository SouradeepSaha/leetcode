# 849. Maximize Distance to Closest Person

class Solution:
    def maxDistToClosest(self, seats) -> int:
        right = 0
        while seats[right] != 1:
            right += 1
        max_dist = right

        left = right
        while right < len(seats):
            if seats[right] == 1:
                cur_dist = int((right + left)/2) - left
                if cur_dist > max_dist:
                    max_dist = cur_dist
                left = right
            right += 1

        cur_dist = len(seats) - left - 1
        if cur_dist > max_dist:
            max_dist = cur_dist

        return max_dist


s = Solution()
print(s.maxDistToClosest([1,0,0,1]))
