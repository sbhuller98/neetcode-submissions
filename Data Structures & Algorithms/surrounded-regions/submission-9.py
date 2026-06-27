from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        regionsToInvestigate = []

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == "O":
                    regionsToInvestigate.append((i,j))

        # (x,y)
        seen = set()
        
        

        def BFS(region):
            q = deque([region])
            currentList = []
            touchesBorder = False
            while q:
                x,y = q.pop()
                if (x,y) in seen:
                    continue
                if x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) - 1:
                    touchesBorder = True


                seen.add((x,y))
                currentList.append((x,y))

                for direction in dirs:
                    nx,ny = x + direction[0], y + direction[1]
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        if board[nx][ny] == "O" and (nx,ny) not in seen:
                            q.appendleft((nx,ny))

            return [] if touchesBorder else currentList

        for region in regionsToInvestigate:
            itemsToMark = BFS(region)
            for x,y in itemsToMark:
                board[x][y] = "X"




        