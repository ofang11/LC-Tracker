# Last updated: 8/2/2025, 4:53:47 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root
        else:
            return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))