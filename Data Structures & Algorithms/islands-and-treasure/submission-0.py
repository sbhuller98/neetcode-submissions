class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def BFS(coordinates: Tuple[int, int]) -> None:
            sourceHandled = False
            # queue for BFS: Tuple[int, int, int] whcih is x,y, distance from source
            q = deque()
            seen = set()
            q.append((coordinates[0], coordinates[1], 0))

            while q:
                x,y,distance = q.pop()
                
                seen.add((x,y))
                val = grid[x][y]
                if val >= 0:
                    if val == 0:
                        if sourceHandled:
                            continue
                        sourceHandled = True
                    elif distance >= val:
                        continue
                    grid[x][y] = distance
                    for location in dirs:
                        nx,ny = x + location[0], y + location[1]
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                            if (nx,ny) not in seen:
                                q.appendleft((nx,ny,distance + 1))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    BFS((i,j))


