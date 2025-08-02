# Last updated: 8/2/2025, 4:53:12 PM
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
        
        for num in nums:
            comp = k - num
            if comp in hmap:
                if comp == num:
                    if hmap[comp] > 1:
                        res += 1
                        hmap[comp] -= 2
                else:
                    if hmap[comp] > 0 and hmap[num] > 0:
                        res += 1
                        hmap[comp] -= 1
                        hmap[num] -= 1
        return res
            