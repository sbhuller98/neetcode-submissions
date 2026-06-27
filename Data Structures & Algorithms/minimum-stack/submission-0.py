class MinStack:

    def __init__(self):
        self.q = []
        self.lowest = []
        

    def push(self, val: int) -> None:
        self.q.append(val)
        self.lowest.append(min(val, self.lowest[-1] if self.lowest else val))

    def pop(self) -> None:
        self.q.pop()
        self.lowest.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.lowest[-1]
