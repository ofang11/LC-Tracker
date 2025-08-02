# Last updated: 8/2/2025, 4:53:36 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterdict = {}

        for char in ransomNote:
            if char in letterdict:
                letterdict[char]+=1
            else:
                letterdict[char] = 1
        
        for char in magazine:
            if char in letterdict:
                letterdict[char] -=1
                if letterdict[char] == 0:
                    letterdict.pop(char)
            if len(letterdict) == 0:
                return True
        return False
                
                  