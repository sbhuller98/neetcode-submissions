class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        seen = {}

        while q:
            x,y,distance = q.pop()
            
            if (x,y) in seen and seen[(x,y)] <= distance:
                continue
            seen[(x,y)] = distance
            val = grid[x][y]
            grid[x][y] = distance
            for location in dirs:
                nx,ny = x + location[0], y + location[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] > 0 and ((nx,ny) not in seen or seen[nx,ny] > distance):
                        q.appendleft((nx,ny,distance + 1))


