# Last updated: 8/2/2025, 4:53:21 PM
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = r
        while l < r:
            k = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(float(pile)/k)
            if total <= h:
                r = k
                res = k
            else:
                l = k + 1
        return res