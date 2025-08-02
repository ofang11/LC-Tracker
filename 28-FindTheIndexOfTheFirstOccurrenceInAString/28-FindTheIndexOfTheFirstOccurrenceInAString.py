# Last updated: 8/2/2025, 4:54:15 PM
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l, r = 0, len(needle)
        while r <= len(haystack):
            if haystack[l:r] == needle:
                return l
            l += 1
            r += 1
        return -1