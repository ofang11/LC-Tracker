# Last updated: 8/2/2025, 4:53:28 PM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temperatures)
        for i, a in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([i, a])
            else:
                while len(stack) != 0 and a > stack[-1][1]:
                    top = stack.pop()
                    res[top[0]] = i - top[0]
                stack.append([i, a])
        return res