class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        ans = []
        pacificAccess =  [[0] * len(heights[0]) for _ in range(len(heights))]
        atlanticAccess =  [[0] * len(heights[0]) for _ in range(len(heights))]

        seenPacific = set()
        seenAtlantic = set()
        def checkAccess(x,y, ocean, history):
            if (x,y) in history:
                return
            ocean[x][y] = 1
            history.add((x,y))

            for dr in dirs:
                newX, newY = x + dr[0], y + dr[1]
                if 0 <= newX < len(heights) and 0 <= newY < len(heights[0]) and heights[newX][newY] >= heights[x][y] and (newX,newY) not in history:
                    checkAccess(newX,newY,ocean, history)


        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    checkAccess(i,j,pacificAccess, seenPacific)
                if i == len(heights) - 1 or j == len(heights[0]) - 1 :
                    checkAccess(i,j,atlanticAccess, seenAtlantic)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacificAccess[i][j] and atlanticAccess[i][j]:
                    ans.append([i,j])

        return ans





