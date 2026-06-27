class Node:
    def __init__(self, word = False):
        self.word = word
        self.children = dict()

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        coords = [[0,1],[1,0],[-1,0],[0,-1]]

        root = Node()

        ans = set()

        for word in words:
            curr = root
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = Node()
                curr = curr.children[letter]
            curr.word = True
        
        pathSoFar = set()
        letterSoFar = []
        def dfs(start, nd):
            if start in pathSoFar:
                return

            pathSoFar.add(start)
            letterSoFar.append(board[start[0]][start[1]])

            if nd.word:
                ans.add(''.join(letterSoFar))

            for co in coords:
                newX, newY = start[0] + co[0], start[1] + co[1]
                if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and board[newX][newY] in nd.children:
                    dfs((newX,newY), nd.children[board[newX][newY]])
            
            pathSoFar.remove(start)
            letterSoFar.pop()


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    dfs((i,j), root.children[board[i][j]])

        return list(ans)
        
