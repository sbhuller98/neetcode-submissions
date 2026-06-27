class MyQueue:

    def __init__(self):
        self.q = [0] * 10
        self.first = 0
        self.last = 0

    def push(self, x: int) -> None:
        if self.last - self.first + 1 == len(self.q):
            self.q.append([0] * len(self.q))
        if self.first > len(self.q) // 2:
            self.q = self.q[self.first:]
            self.first = 0
            self.last -= self.first
        self.q[self.last] = x
        self.last += 1

    def pop(self) -> int:
        self.first +=1 
        return self.q[self.first - 1]

    def peek(self) -> int:
        return self.q[self.first]
        

    def empty(self) -> bool:
        return (self.first == self.last)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()