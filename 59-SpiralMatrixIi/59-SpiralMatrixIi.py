# Last updated: 8/2/2025, 4:54:11 PM
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        nums = []
        for i in range(1, (n*n)+1):
            nums.append(i)
        
        top, bottom = 0, len(res)
        left, right = 0, len(res[0])

        while top < bottom and left < right:
            for i in range(left, right):
                res[top][i] = nums[0]
                nums = nums[1:]
            top+=1


            for i in range(top, bottom):
                res[i][right-1] = nums[0]
                nums = nums[1:]
            right -= 1


            for i in range(right-1, left-1, -1):
                res[bottom-1][i] = nums[0]
                nums = nums[1:]
            bottom-=1

            for i in range(bottom-1, top-1, -1):
                res[i][left] = nums[0]
                nums = nums[1:]
            left+=1
        return res
