# Last updated: 8/2/2025, 4:54:09 PM
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        else:
            dp = [0] * (n+1)
            dp[1] = 1
            dp[2] = 2
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]