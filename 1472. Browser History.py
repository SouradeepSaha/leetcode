class ListNode:
    def __init__(self, val, back = None, forward = None):
        self.val = val
        self.back = back
        self.forward = forward


class BrowserHistory:

    def __init__(self, homepage: str):
        self.start = ListNode(homepage)
        self.end = ListNode("")
        self.start.forward = self.end
        self.end.back = self.start
        self.cursor = self.start

    def visit(self, url: str) -> None:
        newnode = ListNode(url)
        self.cursor.forward.backward = None
        newnode.forward = self.end
        newnode.back = self.cursor
        self.cursor.forward = newnode
        self.end.back = newnode
        self.cursor = newnode
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.cursor.back:
            self.cursor = self.cursor.back
            steps -= 1
        return self.cursor.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cursor.forward and self.cursor.forward.val != "":
            self.cursor = self.cursor.forward
            steps -= 1    
        return self.cursor.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
