# Last updated: 8/2/2025, 4:53:25 PM
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        res = 0
        
        def helper(xShift, yShift):
            overlaps = 0
            for r in range(n):
                for c in range(n):
                    if 0<=r+yShift<n and 0<=c+xShift<n:
                        overlaps += img2[r][c] == 1 and img1[r+yShift][c+xShift] == 1
            return overlaps
        
        return max([helper(left, right) for left in range(-n, n) for right in range(-n, n)])