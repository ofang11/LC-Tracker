# Last updated: 8/2/2025, 4:54:02 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r, res = 0, 1, 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                res = max(prices[r] - prices[l], res)
                r += 1
        return res