from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def searchTimestamps(self, values, target):
        l,r = 0, len(values) - 1
        m = 0
        largestMin = -1
        largestVal = None
        while l <= r:
            m = (l + r) // 2
            if values[m][1] == target:
                return values[m][0]
            
            if values[m][1] > target:
                r = m - 1
            else:
                if values[m][1] > largestMin:
                    largestMin = values[m][1]
                    largestVal = values[m][0]
                l = m + 1
        if values[m][1] == target:
            return values[m][0]
        if largestVal:
            return largestVal
        return ""

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        return self.searchTimestamps(values, timestamp)
        
    


        

