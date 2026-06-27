class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l,r = 0, rows * cols - 1

        while l <= r:
            m = (l + r) // 2
            x = m // cols
            y = m % cols

            val = matrix[x][y]


            if val == target:
                return True
            elif val > target:
                r = m - 1
            else:
                l = m + 1

        return False