class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.curr
        self.curr.next = node
        self.curr = node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
                
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next:
                self.curr = self.curr.next

        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)