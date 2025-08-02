# Last updated: 8/2/2025, 4:53:26 PM
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        hmap = defaultdict(list)
        for i, v in enumerate(s):
            hmap[v].append(i)
        
        def bs(lst, i):
            l, r = 0, len(lst)
            while l < r:
                mid = (l + r) // 2
                if lst[mid] > i:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        for wrd in words:
            prev, flag = -1, True
            for ch in wrd:
                if ch not in hmap:
                    flag = False
                    break
                idx = bs(hmap[ch], prev)
                if idx >= len(hmap[ch]):
                    flag = False
                    break
                else:
                    prev = hmap[ch][idx]
            if flag:
                res += 1
        return res
        
