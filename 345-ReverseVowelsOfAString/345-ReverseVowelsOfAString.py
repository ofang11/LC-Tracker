# Last updated: 8/2/2025, 4:53:37 PM
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vs = []
        idxs = []
        for i in range(len(chars)):
            char = chars[i]
            if char.lower() in vowels:
                vs.append(char)
                idxs.append(i)
        vs.reverse()
        for i in range(len(vs)):
            chars[idxs[i]] = vs[i]
        s =  "".join(chars)
        return s

            