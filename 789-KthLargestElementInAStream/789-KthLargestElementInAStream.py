# Last updated: 8/2/2025, 4:53:26 PM
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.scores = nums
        heapq.heapify(self.scores)
        while len(self.scores) > self.k:
            heapq.heappop(self.scores)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.scores, val)
        if len(self.scores) > self.k:
            heapq.heappop(self.scores)
        return self.scores[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)