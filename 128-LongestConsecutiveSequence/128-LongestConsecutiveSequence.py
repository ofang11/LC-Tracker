# Last updated: 8/2/2025, 4:54:01 PM
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num-1 in numSet:
                continue
            else:
                temp = num
                newRes = 0
                while temp in numSet:
                    newRes += 1
                    temp += 1
                res = max(res, newRes)
        return res