# Last updated: 8/2/2025, 4:54:13 PM
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for string in strs:
            table = [0] * 26
            for ch in string:
                table[ord(ch) - ord('a')] += 1
            if tuple(table) in res:
                res[tuple(table)].append(string)
            else:
                res[tuple(table)] = [string]
        return res.values()