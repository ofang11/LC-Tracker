# Last updated: 8/2/2025, 4:53:55 PM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def cutSpaces(s):
            l, r = 0, len(s) - 1
            while s[l] == ' ' or s[r] == ' ':
                if s[l] == ' ':
                    l += 1
                if s[r] == ' ':
                    r -= 1
            s = s[l:r+1]
            return s
            
        s = cutSpaces(s)
        l = r = 0
        stack = []
        res = ""
        while r < len(s):
            if r == len(s) - 1:
                stack.append(s[l:r+1])
                break
            if s[l] == ' ' and s[r] == ' ':
                l+=1
                r+=1
            elif s[l] == ' ':
                l += 1
            elif s[r] == ' ':
                stack.append(s[l:r])
                l = r
            else:
                r += 1
        while len(stack) > 1:
            res += stack.pop()
            res += " "

        res += stack.pop()
        return res

        
