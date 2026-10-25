class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        xToZero = set()
        yToZero = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    xToZero.add(i)
                    yToZero.add(j)

        for x in xToZero:
            for j in range(len(matrix[0])):
                matrix[x][j] = 0

        for x in yToZero:
            for j in range(len(matrix)):
                matrix[j][x] = 0

