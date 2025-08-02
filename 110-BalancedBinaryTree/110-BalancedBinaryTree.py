# Last updated: 8/2/2025, 4:54:05 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root):
        if not root:
            return [True, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left[0] and right[0]:
            diff = abs(left[1] - right[1])
            if diff <= 1:
                return [True, 1 + max(left[1], right[1])]
        return [False, 1 + max(left[1], right[1])]


    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.helper(root)[0]
        