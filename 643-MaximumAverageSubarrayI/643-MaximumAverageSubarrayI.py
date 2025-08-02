# Last updated: 8/2/2025, 4:53:30 PM
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = 0
        res = sum(nums[l:l+k])
        current = res
        while l + k < len(nums):
            r = l + k
            current = current - nums[l] + nums[r]
            res = max(res, current)
            l += 1
        return res / (float(k))