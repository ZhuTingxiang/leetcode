# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if not root:
            return 0
        if root.left and root.left.left is None and root.left.right is None:
                sum += root.left.val
        sum += self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
        return sum

            