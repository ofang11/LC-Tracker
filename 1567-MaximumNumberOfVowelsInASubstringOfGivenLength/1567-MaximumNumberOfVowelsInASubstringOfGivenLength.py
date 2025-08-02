# Last updated: 8/2/2025, 4:53:13 PM
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}

        def numVowels(st):
            res = 0
            for ch in st:
                if ch in vowels:
                    res += 1
            return res

        n = len(s)
        res = curr = numVowels(s[:k])

        for i in range(n-k):
            if (s[i] in vowels and s[i+k] in vowels) or (s[i] not in vowels and s[i+k] not in vowels):
                continue
            elif s[i] in vowels:
                curr -= 1
            else:
                curr += 1
            res = max(res, curr)
        return res