# Last updated: 8/2/2025, 4:54:21 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l, r = 0, 0
        charSet = set()
        while r < len(s) and l <= r:
            while r <len(s) and s[r] not in charSet:
                charSet.add(s[r])
                res = max(res, len(charSet))
                r += 1
            charSet.remove(s[l])
            l += 1
        return res