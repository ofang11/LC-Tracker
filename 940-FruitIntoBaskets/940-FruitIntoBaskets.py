# Last updated: 8/2/2025, 4:53:21 PM
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l = r = 0
        res = 0
        dic = collections.defaultdict(int)
        while r < len(fruits):
            rFruit = fruits[r]
            lFruit = fruits[l]
            dic[rFruit] += 1
            while len(dic) > 2:
                lf = fruits[l]
                dic[lf] -= 1
                if dic[lf] == 0:
                    del dic[lf]
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res