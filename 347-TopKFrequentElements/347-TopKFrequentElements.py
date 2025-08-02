# Last updated: 8/2/2025, 4:53:40 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp = []
        res = []
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for key in dic:
            temp.append([dic[key], key])

        temp.sort(reverse=True)
        
        for i in range(k):
            res.append(temp[i][1])
        
        return res
                