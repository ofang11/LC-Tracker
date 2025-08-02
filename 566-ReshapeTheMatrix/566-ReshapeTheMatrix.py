# Last updated: 8/2/2025, 4:53:32 PM
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = []
        reshaped = []

        for row in mat:
            for col in row:
                flat.append(col)
        
        if r*c != len(flat):
            return mat
        else:
            for row in range(r):
                reshaped.append(flat[row*c : row*c + c])
            return reshaped