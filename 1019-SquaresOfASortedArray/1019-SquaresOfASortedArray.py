# Last updated: 8/2/2025, 4:53:20 PM
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        neg = []
        pos = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < 0:
                neg = nums[0:i+1]
                break
            else:
                pos.append(nums[i])

        while len(neg) > 0 and len(pos) > 0:
            negSq = neg[-1]**2
            posSq = pos[-1]**2
            if negSq < posSq:
                res.append(negSq)
                neg.pop()
            else:
                res.append(posSq)
                pos.pop()
        if len(neg) == 0:
            while len(pos) > 0:
                res.append(pos.pop()**2)
        else:
            while len(neg) > 0:
                res.append(neg.pop() **2)
        return res