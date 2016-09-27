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
       
        if self.sumOfLeftLeaves(root.right) !=0:
                sum += self.sumOfLeftLeaves(root.right)
        if self.sumOfLeftLeaves(root.left) !=0:
                sum += self.sumOfLeftLeaves(root.left)
        elif root.left:
            if root.left.left is None and root.left.right is None:
                sum += root.left.val
        return sum

            