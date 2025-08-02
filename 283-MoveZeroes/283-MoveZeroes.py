# Last updated: 8/2/2025, 4:53:38 PM
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        z = i = 0
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[z]
                nums[z] = temp
                z += 1
            i += 1
        
        