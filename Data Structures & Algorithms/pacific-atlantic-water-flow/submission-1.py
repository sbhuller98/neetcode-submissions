class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ccess(pacific, atlantic)
        coords = [[0,1],[1,0],[-1,0],[0,-1]]

        seen = {}
        ans = []

        def traverse(start):
            nonlocal seen

            if start in seen:
                return seen[start]
            
            access = [0,0]

            if start[0] == 0 or start[1] == 0:
                access[0] = 1
            if start[0] == len(heights) - 1 or start[1] == len(heights[0]) - 1:
                access[1] = 1

            seen[start] = access

            for co in coords:
                newx, newy = co[0] + start[0], co[1] + start[1]

                if newx >= 0 and newx < len(heights) and newy >= 0 and \
                    newy < len(heights[0]) and heights[newx][newy] <= heights[start[0]][start[1]]:
                    val = traverse((newx,newy))
                    if val[0] > access[0]:
                        access[0] = val[0]

                    if val[1] > access[1]:
                        access[1] = val[1]
            
            seen[start] = access
            return access
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                access = traverse((i,j))

                if access[0] == access[1] == 1:
                    ans.append([i,j])
        
        return ans

            
                

                    
