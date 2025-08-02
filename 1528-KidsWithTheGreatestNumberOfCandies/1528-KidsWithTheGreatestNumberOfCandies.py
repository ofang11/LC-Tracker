# Last updated: 8/2/2025, 4:53:14 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandies = max(candies)
        res = []
        for kid in candies:
            if kid + extraCandies >= maxCandies:
                res.append(True)
            else:
                res.append(False)
        return res