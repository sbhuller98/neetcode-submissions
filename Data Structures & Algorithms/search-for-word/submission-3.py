class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def checkPath(soFar, coords, prev):
            x,y = prev

            if soFar == word:
                return True
            if len(soFar) >= len(word):
                return False
            
            letter = word[len(soFar)]
            for dir in dirs:
                nx,ny = nx, ny = x + dir[0], y + dir[1]
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and letter == board[nx][ny] and (nx,ny) not in coords:
                    coords.add((nx,ny))
                    if checkPath(soFar + board[nx][ny], coords, (nx,ny)):
                        return True
                    coords.remove((nx,ny))


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    s = set()
                    s.add((i,j))
                    if checkPath(word[0], s, (i,j)):
                        return True

        return False