# Last updated: 8/2/2025, 4:54:07 PM
class Solution(object):
    def binSearch(self, nums, target):
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                res = mid
                break
        return res != -1

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        t, b = 0, len(matrix) - 1
        while t<=b:
            mid = (t+b) // 2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]:
                return self.binSearch(matrix[mid], target)
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                t = mid + 1
        return False
                