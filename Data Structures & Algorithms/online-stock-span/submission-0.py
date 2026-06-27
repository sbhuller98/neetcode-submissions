class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = -1
        while (count * -1 <= len(self.stack)) and price >= self.stack[count]:
            count -= 1
        self.stack.append(price)
        return (count * -1)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)