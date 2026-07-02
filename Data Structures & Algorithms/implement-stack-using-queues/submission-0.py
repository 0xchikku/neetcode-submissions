class MyStack:

    # space - O(n)
    def __init__(self):
        self.queue = deque([])
        self.peek = -1

    # time - O(1)
    def push(self, x: int) -> None:
        self.queue.append(x)
        self.peek = x

    # time - O(n)
    def pop(self) -> int:
        for _ in range(0, len(self.queue)-1):
            value = self.queue.popleft()
            self.peek = value if self.queue else -1
            self.queue.append(value)
        return self.queue.popleft()
            
    # time - O(1)
    def top(self) -> int:
        return self.peek

    # time - O(1)
    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()