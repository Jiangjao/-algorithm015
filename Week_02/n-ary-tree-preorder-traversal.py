"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def dfs(root):
            if root:
                res.append(root.val)
                for i in root.children:
                    dfs(i)
        dfs(root)
        return res
        # 类似栈的方式,及层序遍历
        