# Last updated: 8/2/2025, 4:53:29 PM
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        cur = image[sr][sc]
        h = len(image)
        w = len(image[0])

        def dfs(sr, sc):
            if 0 <= sr < h and 0 <= sc < w and image[sr][sc] == cur and image[sr][sc] != color:
                image[sr][sc] = color
                dfs(sr+1, sc)
                dfs(sr-1, sc)
                dfs(sr, sc+1)
                dfs(sr, sc-1)
        dfs(sr,sc)
        return image