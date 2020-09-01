from collections import deque
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.min_store = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if (not self.min_store) or (x <= self.min_store[-1]):
            self.min_store.append(x)
        return None
        

    def pop(self) -> None:
        p = self.stack.pop()
        if p == self.min_store[-1]:
            self.min_store.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_store[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
