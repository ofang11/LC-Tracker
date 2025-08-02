# Last updated: 8/2/2025, 4:53:22 PM
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        transposed = [[0]*rows for i in range(cols)]
        
        for row in range(rows):
            for col in range(cols):
                transposed[col][row] = matrix[row][col]
        
        return transposed