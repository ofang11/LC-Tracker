# Last updated: 8/2/2025, 4:53:31 PM
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        res = True
        while n > 0:
            planted = False
            for i in range(len(flowerbed)):
                if flowerbed[i] == 1:
                    continue
                elif i > 0 and flowerbed[i-1] == 1:
                    continue
                elif i < len(flowerbed)-1 and flowerbed[i+1] == 1:
                    continue
                else:
                    planted = True
                    flowerbed[i] = 1
                    break
            if not planted:
                res = False
                break
            n -= 1
        return res