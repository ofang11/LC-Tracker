# Last updated: 8/2/2025, 4:53:43 PM
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        pProd = [0]*n
        sProd = [0]*n
        for i in range(n):
            r = i*-1+(n-1)
            if i == 0:
                pProd[i]=nums[i]
                sProd[r]=nums[r]
            else:
                pProd[i]=nums[i] * pProd[i-1]
                sProd[r]=nums[r] * sProd[r+1]
        
        for i in range(n):
            if i == 0:
                res.append(sProd[i+1])
            elif i == n-1:
                res.append(pProd[i-1])
            else:
                currProd = pProd[i-1] * sProd[i+1]
                res.append(currProd)
        return res
        
