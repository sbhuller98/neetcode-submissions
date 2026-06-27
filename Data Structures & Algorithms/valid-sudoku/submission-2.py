from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # (row, col, section)
        row = [0] * 9
        col = [0] * 9
        section = [0] * 9
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                item = board[i][j]
                if item == ".":
                    continue
                # check row
                item = int(item) - 1

                if (1 << item) & row[i]:
                    return False
                row[i] |= (1 << item) 

                # check col
                if (1 << item) & col[j]:
                    return False
                col[j] |= (1 << item) 

                # check section
                sectionNum = (i // 3 * 3) + (j // 3)
                if (1 << item) & section[sectionNum]:
                    return False
                section[sectionNum] |= (1 << item) 
        
        return True