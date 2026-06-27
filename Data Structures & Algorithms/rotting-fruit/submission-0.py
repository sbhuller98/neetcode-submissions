class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        goodFruit = set()
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    goodFruit.add((i,j))
                elif grid[i][j] == 2:
                    q.append((i,j,0))

        minMinutes = 0
        seen = {}

        while q:
            x,y,minutes = q.pop()

            if (x,y) in seen and seen[(x,y)] < minutes:
                continue
            
            seen[(x,y)] = minutes

            if (x,y) in goodFruit:
                goodFruit.remove((x,y))

            minMinutes = max(minMinutes, minutes)

            for direction in dirs:
                nx,ny = direction[0] + x, direction[1] + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 1:
                        q.appendleft((nx,ny,minutes + 1))
        
        return minMinutes if len(goodFruit) == 0 else -1


