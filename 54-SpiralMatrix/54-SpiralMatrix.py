# Last updated: 8/2/2025, 4:54:13 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        t, b, l, r = 0, len(matrix), 0, len(matrix[0])
        while t < b and l < r:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1

            if t == b:
                break

            for i in range(t, b):
                res.append(matrix[i][r-1])
            r -= 1

            if r == l:
                break
            
            for i in range(r-1, l-1, -1):
                res.append(matrix[b-1][i])
            b -= 1

            if t == b:
                break
            

            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            l += 1
        return res

