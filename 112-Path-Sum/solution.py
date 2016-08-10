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
        if root:
            result = root.val
            while root.left is not None:
                result += root.left
                
            if result == sum:
                return True
            else:
                return False
        else:
            return False
        