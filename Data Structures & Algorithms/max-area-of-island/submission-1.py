class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0

        def searchIsland(coordinates):
            size = 0
            stack = [coordinates]

            while stack:
                curr = stack.pop()
                if grid[curr[0]][curr[1]] == 1:
                    size += 1
                    grid[curr[0]][curr[1]] = 0

                    if curr[0] > 0 and grid[curr[0]-1][curr[1]] == 1:
                        stack.append((curr[0]-1,curr[1]))
                    if curr[1] > 0 and grid[curr[0]][curr[1]-1] == 1:
                        stack.append((curr[0],curr[1]-1))
                    if curr[0] < len(grid) - 1 and grid[curr[0]+1][curr[1]] == 1:
                        stack.append((curr[0]+1,curr[1]))
                    if curr[1] < len(grid[0]) - 1 and grid[curr[0]][curr[1]+1] == 1:
                        stack.append((curr[0],curr[1]+1))
                
            
            return size
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxSize = max(maxSize, searchIsland((i,j)))

        return maxSize