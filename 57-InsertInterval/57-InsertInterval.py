# Last updated: 8/2/2025, 4:54:10 PM
class Solution(object):
    def overlap(self, intervals, newInterval):
        for i in range(len(intervals)):
            itvl = intervals[i]
            if not (newInterval[0] > itvl[1] or newInterval[1] < itvl[0]):
                newItvls = intervals[:i] + intervals[i+1:]
                newIt = [min(itvl[0], newInterval[0]), max(itvl[1], newInterval[1])]
                return (True, newItvls, newIt)
        return (False, [], [])


    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        new = self.overlap(intervals, newInterval)
        if not new[0]:
            intervals.append(newInterval)
            intervals.sort()
            return intervals
        newIntervals = new[1]
        addInterval = new[2]
        return self.insert(newIntervals, addInterval)

        