# Last updated: 1/21/2026, 6:05:55 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        n = len(nums)
4        res = 0
5        hmap = defaultdict(int)
6        for num in nums:
7            hmap[num] += 1
8            if hmap[num] > n / 2:
9                res = num
10                break
11        return res
12        