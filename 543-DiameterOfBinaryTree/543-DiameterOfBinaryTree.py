# Last updated: 8/2/2025, 4:53:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal res
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            

            currDiam = left + right
            res = max(res, currDiam)

            return 1 + max(left, right)

        depth(root)
        return res
        