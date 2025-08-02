# Last updated: 8/2/2025, 4:53:15 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd = math.gcd(len(str1), len(str2))
        return str1[0:gcd]
