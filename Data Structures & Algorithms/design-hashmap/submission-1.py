class LinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self. next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.arr = [None] * self.size

    def put(self, key: int, value: int) -> None:
        result = hash(key) % self.size
        arrayField = self.arr[result]
        newNode = LinkedListNode(key, value)

        if arrayField is None:
            self.arr[result] = newNode
            return
        
        while arrayField is not None:
            if arrayField.key == key:
                arrayField.val = value
                return
            if arrayField.next == None:
                arrayField.next = newNode
                return
            arrayField = arrayField.next

        
        

    def get(self, key: int) -> int:
        result = hash(key) % self.size
        arrayField = self.arr[result]

        while arrayField is not None:
            if arrayField.key == key:
                return arrayField.val
            arrayField = arrayField.next

        return -1

    def remove(self, key: int) -> None:
        result = hash(key) % self.size
        arrayField = self.arr[result]

        if arrayField is None:
            return

        if arrayField.key == key:
            self.arr[result] = arrayField.next
            return

        prev = arrayField
        arrayField = arrayField.next
        
        while arrayField is not None:
            if arrayField.key == key:
                prev.next = arrayField.next

            prev = arrayField
            arrayField = arrayField.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)