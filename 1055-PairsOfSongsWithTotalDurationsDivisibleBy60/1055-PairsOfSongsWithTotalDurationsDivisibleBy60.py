# Last updated: 8/2/2025, 4:53:17 PM
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = {60 : 1}
        res = 0
        for t in time:
            curr = t % 60
            comp = 60 - curr
            if curr == 0:
                if curr in dic:
                    res += dic[curr]
            elif comp in dic:
                res += dic[comp]
            
            if curr in dic:
                dic[curr] += 1
            else:
                dic[curr] = 1          
        return res