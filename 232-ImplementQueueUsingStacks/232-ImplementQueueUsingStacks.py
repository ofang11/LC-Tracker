# Last updated: 8/2/2025, 4:53:44 PM
class MyQueue(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.len = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.q1:
            self.q2.append(self.q1.pop())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.q1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()