# Last updated: 8/2/2025, 4:53:31 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        for i in range(0, len(s2)):
            if i+n > len(s2):
                break
            if sorted(s2[i:i+n]) == sorted(s1):
                return True
        return False