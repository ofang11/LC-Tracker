# Last updated: 8/2/2025, 4:54:06 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inLimits(self, root, lower, upper):
        if not root:
            return True
        if root.val > lower and root.val < upper:
            leftValid = self.inLimits(root.left, lower, root.val)
            rightValid = self.inLimits(root.right, root.val, upper)
            return leftValid and rightValid
        else:
            return False

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.inLimits(root, float('-inf'), float('inf'))

        