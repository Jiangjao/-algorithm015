"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        result = []
        if not root:
            return result
        curr_level = [root]
        while curr_level:
            temp = []
            nex_level = []
            for node  in curr_level:
                temp.append(node.val)
                nex_level += node.children
            result.append(temp)
            curr_level = nex_level
        return result