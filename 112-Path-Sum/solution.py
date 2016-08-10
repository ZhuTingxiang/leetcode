# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left or root.right:
            return self.hasPatchSum(root.left, sum-root.left) or self.hasPatchSum(root.right, sum-root.right)
        else:
            return False
            
        