# Last updated: 8/2/2025, 4:53:35 PM
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ptr1 = ptr2 = 0
        while ptr1 < len(s) and ptr2 < len(t):
            if s[ptr1] == t[ptr2]:
                ptr1 += 1
            ptr2 += 1
        if ptr1 == len(s):
            return True
        return False