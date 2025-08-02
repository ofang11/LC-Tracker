# Last updated: 8/2/2025, 4:54:08 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque()
        q.append(root)
        while len(q) != 0:
            temp = []
            n = len(q)
            for i in range(n):
                tree = q.popleft()
                if tree:
                    temp.append(tree.val)
                    if tree.left:
                        q.append(tree.left)
                    if tree.right:
                        q.append(tree.right)
            if len(temp) != 0:
                res.append(temp)
        return res