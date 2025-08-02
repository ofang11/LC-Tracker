# Last updated: 8/2/2025, 4:54:19 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        numOpen = 0
        numClose = 0
        for brack in s:
            if brack == '{':
                stack.append('}')
                numOpen+=1
            elif brack == '[':
                stack.append(']')
                numOpen+=1
            elif brack == '(':
                stack.append(')')
                numOpen+=1
            else:
                numClose+=1
                if brack == stack[-1]:
                    stack.pop()
                    
        return len(stack) == 1 and numOpen == numClose
        