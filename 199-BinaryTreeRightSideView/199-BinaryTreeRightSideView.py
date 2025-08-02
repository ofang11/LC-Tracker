# Last updated: 8/2/2025, 4:53:50 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        q = collections.deque()
        q.append(root)
        while len(q) != 0:
            n = len(q)
            
            for _ in range(n-1):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            right = q.popleft()
            if right:
                res.append(right.val)
                if right.left:
                    q.append(right.left)
                if right.right:
                    q.append(right.right)
        return res