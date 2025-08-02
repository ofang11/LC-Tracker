# Last updated: 8/2/2025, 4:53:57 PM
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        res = 0
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                denom = stack.pop()
                numer = stack.pop()
                q = (1.0*numer)/denom
                quotient = int(math.ceil(q)) if q < 0 else numer//denom
                stack.append(quotient)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first-second)
            else:
                stack.append(int(token))
        return stack[0]