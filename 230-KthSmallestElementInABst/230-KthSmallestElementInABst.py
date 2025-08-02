# Last updated: 8/2/2025, 4:53:46 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        inOrderList = []
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            inOrderList.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return inOrderList[k-1]
        