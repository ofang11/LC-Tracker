# Last updated: 8/2/2025, 4:53:34 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        charDict = {}
        for c in s:
            if c in charDict:
                charDict[c] += 1
            else:
                charDict[c] = 1
        oddCount = 0
        for key in charDict:
            if not charDict[key] % 2 == 0:
                oddCount+=1
        if oddCount > 0:
            return len(s) - oddCount + 1
        else:
            return len(s)
        
        