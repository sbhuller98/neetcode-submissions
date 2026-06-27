class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        newList = []

        for i in range(len(position)):
            newList.append((position[i], speed[i]))
        
        newList.sort(reverse = True)

        for i in range(len(newList)):
            item = newList[i]
            turns = (target - item[0]) / item[1]
            if not fleets or fleets[-1] < turns:
                fleets.append(turns)

        return len(fleets)