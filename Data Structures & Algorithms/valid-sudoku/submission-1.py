from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # (row, col, section)
        seen = defaultdict(lambda: (set(), set(), set()))
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                item = board[row][col]
                if item == ".":
                    continue
                # check row

                if row in seen[item][0]:
                    return False
                seen[item][0].add(row)

                # check col
                if col in seen[item][1]:
                    return False
                seen[item][1].add(col)

                # check section
                section = (row // 3, col // 3)
                if section in seen[item][2]:
                    return False
                seen[item][2].add(section)
        
        return True