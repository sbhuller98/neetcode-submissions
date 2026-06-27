from sortedcontainers import SortedList
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.atomicNum = 0
        self.atomicNumMin = 0
        self.atomic = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache[key] = (val[0], self.atomicNum)
        del self.atomic[val[1]]
        self.atomic[self.atomicNum] = key
        self.atomicNum += 1
        return val[0]

    def put(self, key: int, value: int) -> None:
        print(self.cache)
        if key in self.cache:
            val = self.cache[key]
            del self.atomic[val[1]]
        else:
            while len(self.cache) >= self.capacity:
                if self.atomicNumMin in self.atomic:
                    del self.cache[self.atomic[self.atomicNumMin]]
                self.atomicNumMin += 1

        self.atomic[self.atomicNum] = key
        self.cache[key] = (value, self.atomicNum)
        self.atomicNum += 1
        return
        
        
        
       


        
