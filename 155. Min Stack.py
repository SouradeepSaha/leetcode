class Node:
    def __init__(self, val: int, min_val: int, right = None):
        self.val = val
        self.min_val = min_val
        self.right = right
    

class MinStack:

    def __init__(self):
        self.stack = None
        

    def push(self, val: int) -> None:
        if self.stack is None:
            self.stack = Node(val, val, None)
        else:
            self.stack = Node(val, min(self.stack.min_val, val), self.stack)
        
    def pop(self) -> None:
        if self.stack:
            self.stack = self.stack.right
        

    def top(self) -> int:
        return self.stack.val
        

    def getMin(self) -> int:
        return self.stack.min_val
