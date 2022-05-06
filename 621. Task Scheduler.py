from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksCounter = Counter(tasks)
        h1, dq = [], deque()
        
        for key, val in tasksCounter.items():
            heapq.heappush(h1, -val)
        
        time = 0
        while len(h1) or len(dq):
            if not len(h1):
                time = dq[0][1]
            
            if len(dq) and dq[0][1] == time:
                heapq.heappush(h1, dq.popleft()[0])
            
            top = heapq.heappop(h1)
            time += 1
            if top+1 != 0:
                dq.append((top+1, time+n))
            
        return time
