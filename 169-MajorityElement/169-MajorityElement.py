# Last updated: 8/2/2025, 4:53:52 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countHash = {}
        for num in nums:
            if num in countHash:
                countHash[num] += 1
            else:
                countHash[num] = 1
        majority = len(nums) - len(nums)//2
        for key in countHash:
            if countHash[key] >= majority:
                return key
        return nums[0]