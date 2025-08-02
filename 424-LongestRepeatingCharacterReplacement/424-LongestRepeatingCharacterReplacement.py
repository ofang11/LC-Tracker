# Last updated: 8/2/2025, 4:53:35 PM
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l, r, res = 0, 0, 0
        dic = {}
        while r < len(s):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            numReplacements = (r-l+1) - max(dic.values())
            if numReplacements <= k:
                res = max(res, r-l+1)
                r += 1
            else:
                dic[s[l]] -= 1
                dic[s[r]] -= 1
                l += 1
        return res