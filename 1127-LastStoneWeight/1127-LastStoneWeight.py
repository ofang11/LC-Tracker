# Last updated: 8/2/2025, 4:53:16 PM
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)
            diff = first-second

            if diff > 0:
                heapq.heappush(stones, -1*diff)
        
        heapq.heappush(stones, 0)
        return heapq.heappop(stones) * - 1