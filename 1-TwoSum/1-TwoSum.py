# Last updated: 8/2/2025, 4:54:25 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i in range(len(nums)):
            numsDict[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in numsDict and not i == numsDict[target - nums[i]]:
                return [i, numsDict[target - nums[i]]]
        