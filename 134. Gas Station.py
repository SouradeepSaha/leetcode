class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, debt = 0, 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i]-cost[i]
            if tank < 0:
                debt += tank
                tank = 0
                start = i+1
                # if tank becomes negative, then all previous index will not yield result as our petrol reaches negative value hence //result will be atleast greater than index at which petrol is negative
            
        return start if tank+debt >= 0 else -1
