class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        seen = set()

        def mapIsland(coordinates):
            stack = [coordinates]
            
            while stack:
                curr = stack.pop()

                if curr not in seen:
                    seen.add(curr)
                    if curr[0] < (len(grid) - 1) and grid[curr[0]+1][curr[1]] == "1":
                        stack.append((curr[0]+1,curr[1]))
                    if curr[1] < (len(grid[0]) - 1) and grid[curr[0]][curr[1]+1] == "1":
                        stack.append((curr[0],curr[1]+1))
                    if curr[0] > 0 and grid[curr[0]-1][curr[1]] == "1":
                        stack.append((curr[0]-1,curr[1]))
                    if curr[1] > 0 and grid[curr[0]][curr[1]-1] == "1":
                        stack.append((curr[0],curr[1]-1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in seen:
                    islands += 1
                    mapIsland((i,j))
                    
        return islands