class MinStack:

    def __init__(self):
        self.q = []
        

    def push(self, val: int) -> None:
        self.q.append((val, min(val, self.q[-1][1] if self.q else val)))

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        return self.q[-1][0]

    def getMin(self) -> int:
        return self.q[-1][1]
