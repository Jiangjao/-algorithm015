# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 代码不知如何优化
        if not (preorder and inorder):
            return None
        # temp = preorder[0]
        node = TreeNode(preorder[0])
        nodeIndex = inorder.index(preorder[0])

        leftList = [i for i in inorder[:nodeIndex]]
        rightList = [j for j in inorder[nodeIndex+1:]]

        node.left= self.buildTree(preorder[1:nodeIndex+1], leftList)
        node.right = self.buildTree(preorder[nodeIndex+1:], rightList)
        return node