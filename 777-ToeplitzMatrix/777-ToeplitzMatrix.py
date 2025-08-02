# Last updated: 8/2/2025, 4:53:27 PM
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            if row == rows-1:
                break
            if matrix[row][:-1] != matrix[row+1][1:]:
                return False
        for row in range(rows-1, -1, -1):
            if row == 0:
                break
            if matrix[row][1:] != matrix[row-1][:-1]:
                return False
        return True