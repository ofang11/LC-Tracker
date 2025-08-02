# Last updated: 8/2/2025, 4:53:38 PM
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)