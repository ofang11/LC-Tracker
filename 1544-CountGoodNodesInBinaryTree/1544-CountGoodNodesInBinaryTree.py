# Last updated: 8/2/2025, 4:53:14 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root, greatest):
        if not root:
            return 0
        elif root.val < greatest:
            return self.dfs(root.left, greatest) + self.dfs(root.right, greatest)
        else:
            return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
        