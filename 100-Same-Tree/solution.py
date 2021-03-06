# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) and p.val == q.val or p is q:
            return True
        else:
            return False
        