class MyHashSet:

    def __init__(self):
        self.arr = [[] for i in range(100)]
        self.size = 100

    def add(self, key: int) -> None:
        result = hash(key) % self.size
        if key not in self.arr[result]:
            self.arr[result].append(key)

    def remove(self, key: int) -> None:
        result = hash(key) % self.size
        if key in self.arr[result]:
            self.arr[result].remove(key)

    def contains(self, key: int) -> bool:
        result = hash(key) % self.size
        return (key in self.arr[result])

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)