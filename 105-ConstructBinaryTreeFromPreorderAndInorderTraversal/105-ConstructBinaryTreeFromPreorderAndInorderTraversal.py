# Last updated: 8/2/2025, 4:54:04 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        elif len(preorder) < 1:
            return None
        else:
            rootVal = preorder[0]
            leftLen, rightLen = 0, 0
            leftPreOrder, rightPreOrder = [], []
            leftInOrder, rightInOrder = [], []
            for i in range(len(inorder)):
                if inorder[i] == rootVal:
                    leftLen = i
                    leftInOrder = inorder[0:i] or []
                    leftPreOrder = preorder[1:1+i] or []

                    rightLen = len(inorder) - i - 1
                    rightInOrder = inorder[i+1:] or []
                    rightPreOrder = preorder[i+1:] or []
                    break
            leftSub = self.buildTree(leftPreOrder, leftInOrder)
            rightSub = self.buildTree(rightPreOrder, rightInOrder)
            return TreeNode(rootVal, leftSub, rightSub)



        