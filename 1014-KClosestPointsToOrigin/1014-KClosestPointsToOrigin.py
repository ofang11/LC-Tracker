# Last updated: 8/2/2025, 4:53:19 PM
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = []
        res = []
        for i in range(len(points)):
            point = points[i]
            dist = point[0]**2 + point[1]**2
            distances.append([dist, i])
        heapq.heapify(distances)
        while k > 0:
            closest = heapq.heappop(distances)
            res.append(points[closest[1]])
            k -= 1
        return res
