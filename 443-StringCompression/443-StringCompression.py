# Last updated: 8/2/2025, 4:53:33 PM
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        insert = 0
        i = 0
        n = len(chars)
        while i < n:
            group = 1
            while (i + group) < n and chars[i+group] == chars[i]:
                group += 1
            chars[insert] = chars[i]
            insert += 1
            if group > 1:
                string = str(group)
                chars[insert:insert+len(string)] = list(string)
                insert+= len(string)
            i += group
        return insert