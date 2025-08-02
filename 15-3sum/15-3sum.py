# Last updated: 8/2/2025, 4:54:21 PM
class Solution(object):
    def twoSum(self, nums, target):
        numSet = set()
        for num in nums:
            comp = target-num
            if comp in numSet:
                return [num, comp]
            else:
                numSet.add(num)
        return []

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            curr = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                cSum = curr + nums[l] + nums[r]
                if  cSum == 0:
                    res.append([curr, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif cSum < 0:
                    l += 1
                elif cSum > 0:
                    r -= 1
        return res