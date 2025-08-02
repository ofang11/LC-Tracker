# Last updated: 8/2/2025, 4:53:11 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        while len(word1) > 0 and len(word2) > 0:
            res += word1[0]
            res += word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        if len(word1) > 0:
            res += word1
        if len(word2) > 0:
            res += word2
        return res
        