# BFS Solution

from collections import deque

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        cur = abs(jug1Capacity-jug2Capacity)
        s = set()
        l = deque([jug1Capacity, jug2Capacity])
        while len(l):
            s.add(l[0])
            cur = l[0]
            l.popleft()
            if abs(jug1Capacity-cur) not in s:
                l.append(abs(jug1Capacity-cur))
            if abs(jug2Capacity-cur) not in s:
                l.append(abs(jug2Capacity-cur))
        
        for item in s:
            if targetCapacity in s or targetCapacity-item in s:
                return True
        
        return False

# Math Solution using Bezout's lemma
from fractions import gcd      
def canMeasureWater(self, x, y, z):
    return z == 0 or x + y >= z and z % gcd(x, y) == 0
