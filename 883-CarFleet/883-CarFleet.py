# Last updated: 8/2/2025, 4:53:23 PM
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        stack = []
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True)

        for car in cars:
            time = (target - car[0])*1.0/car[1]
            if len(stack) == 0:
                stack.append(time)
            else:
                if stack[-1] >= time:
                    continue
                else:
                    stack.append(time)
        return len(stack)