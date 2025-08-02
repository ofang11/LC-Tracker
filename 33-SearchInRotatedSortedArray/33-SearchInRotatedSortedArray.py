# Last updated: 8/2/2025, 4:54:16 PM
class Solution(object):
    def binSearch(self, offSet, nums, target):
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                res = m
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if res == -1:
            return res
        return res + offSet


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

    
        res = self.binSearch(0, nums[0:l], target)
        if res == -1:
            res = self.binSearch(l, nums[l:len(nums)], target)
        return res