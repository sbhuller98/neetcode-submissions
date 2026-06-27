class LinkedList:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.arr = [None for i in range(self.size)]

    def add(self, key: int) -> None:
        result = hash(key) % self.size
        newKey = LinkedList(key)
        curr = self.arr[result]
        if curr is None:
            self.arr[result] = newKey
            return
        while curr.next is not None:
            curr = curr.next
        curr.next = newKey
            

    def remove(self, key: int) -> None:
        result = hash(key) % self.size
        print(self.arr[result])
        curr = prev = self.arr[result]
        if curr == None: return
        if curr.key == key: 
            print("here")
            print(self.arr[result])
            self.arr[result] = None
            print(self.arr[result])
            return
        curr = curr.next
        while curr is not None:
            if curr.key == key:
                prev.next = None
                return
            curr = curr.next
            prev = prev.next
        print(self.arr[result])


    def contains(self, key: int) -> bool:
        result = hash(key) % self.size
        curr = self.arr[result]
        while curr is not None:
            if curr.key == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)