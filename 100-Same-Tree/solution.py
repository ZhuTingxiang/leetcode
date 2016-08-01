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
        if not p or not q:
            return False
        elif p.left == None and p.right == None and q.right == None and q.left == None:
            return True
        else:
            if isSameTree(p.left,q.left) and isSameTree(p.right,q.right):
                return True
            else:
                return False
        