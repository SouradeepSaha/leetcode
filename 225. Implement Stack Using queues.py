from collections import deque

# O(n) push, O(1) all other operations
class MyStack:

    def __init__(self):
        self.queue = deque()
        self.length = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(self.length):
            self.queue.append(self.queue.popleft())
        self.length += 1
        
    def pop(self) -> int:
        self.length -= 1
        return self.queue.popleft()
        
    def top(self) -> int:
        return self.queue[0]
        
    def empty(self) -> bool:
        return not self.length
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
