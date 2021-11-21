from collections import deque

class MyQueue:

    def __init__(self):
        self.insertStack = deque()
        self.popStack = deque()

    def push(self, x: int) -> None:
        self.insertStack.append(x)

    def pop(self) -> int:
        if not len(self.popStack):
            while len(self.insertStack):
                self.popStack.append(self.insertStack.pop())
        
        return self.popStack.pop()
            
    def peek(self) -> int:
        if not len(self.popStack):
            while len(self.insertStack):
                self.popStack.append(self.insertStack.pop())

        return self.popStack[-1]
        

    def empty(self) -> bool:
        return not (len(self.insertStack) + len(self.popStack))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
