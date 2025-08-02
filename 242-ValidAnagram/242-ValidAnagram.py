# Last updated: 8/2/2025, 4:53:40 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lmap = {}
        res = 0
        for i in range(len(s)):
            lmap[s[i]] = lmap.get(s[i], 0) + 1
            lmap[t[i]] = lmap.get(t[i], 0) - 1
        for key in lmap:
            if lmap[key] != 0:
                return False
        return True
            
