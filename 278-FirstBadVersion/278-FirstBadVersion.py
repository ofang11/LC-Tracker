# Last updated: 8/2/2025, 4:53:39 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                high = mid
            else:
                low = mid+1
        return low