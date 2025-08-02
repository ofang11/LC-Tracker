# Last updated: 8/2/2025, 4:53:10 PM
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for i in range(n-2)]

        def findLargest(miniGrid: List[List[int]]) -> int:
            greatest = miniGrid[0][0]
            for row in miniGrid:
                for col in row:
                    if col > greatest:
                        greatest = col
            return greatest

        for row in range(1, n-1):
            for col in range(1, n-1):
                cell = grid[row][col]
                surround = []
                surround.append(grid[row-1][col-1 : col + 2])
                surround.append(grid[row][col-1 : col +2])
                surround.append(grid[row + 1][col-1: col +2])
                maxLocal[row-1][col-1] = findLargest(surround)
        return maxLocal
