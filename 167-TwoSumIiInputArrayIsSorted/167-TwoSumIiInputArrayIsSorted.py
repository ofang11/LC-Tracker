# Last updated: 8/2/2025, 4:53:54 PM
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 1, len(numbers)
        
        while l < r:
            currSum = numbers[l-1] + numbers[r-1]
            if  currSum == target:
                return [l, r]
            elif currSum < target:
                l += 1
            else:
                r -= 1
        return [l, r]