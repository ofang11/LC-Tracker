# Last updated: 8/2/2025, 4:53:11 PM
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for ch in s:
            if ch != '*':
                res.append(ch)
            else:
                res.pop()
        return ''.join(res)