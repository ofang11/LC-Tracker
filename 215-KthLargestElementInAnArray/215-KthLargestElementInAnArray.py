# Last updated: 8/2/2025, 4:53:48 PM
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i] = -1*nums[i]
        heapq.heapify(nums)
        
        for _ in range(1, k):
            heapq.heappop(nums)
        return heapq.heappop(nums) * -1