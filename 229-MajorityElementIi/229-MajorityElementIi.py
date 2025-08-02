# Last updated: 8/2/2025, 4:53:47 PM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        t = len(nums) / 3
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        for key in dic:
            if dic[key] > t:
                res.append(key)
        return res