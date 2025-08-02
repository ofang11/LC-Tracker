# Last updated: 8/2/2025, 4:53:49 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 1
        return False