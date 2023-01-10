class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
      # Greedy algorithm : O(nlogn time)
        points.sort()
        prev = points[0]
        result = 1

        for i in range(1, len(points)):
            point = points[i]

            if prev[1] >= point[0]:
                prev = [prev[0], min(prev[1], point[1])]
        
            else:
                prev = point
                result += 1

        return result
