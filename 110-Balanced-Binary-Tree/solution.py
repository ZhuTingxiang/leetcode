# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.right is not None and root.left is None:
            return self.findHeight(root.right)<=1
        if root.right is None and root.left is not None:
            return self.findHeight(root.left)<=1
        if root.left and root.right:
            if abs(self.findHeight(root.left) - self.findHeight(root.right)) > 1:
                return False
            if !self.isBalanced(root.left) or (!self.isBalanced(root.right)):
                return False
        return True

    def findHeight(self,root):
        if root.left is None and root.right is not None:
            height = self.findHeight(root.right) + 1
        elif root.right is None and root.left is not None:
            height = self.findHeight(root.left) + 1
        elif root.left and root.right:
            height = max(self.findHeight(root.left),self.findHeight(root.right)) + 1
        elif root.right is None and root.left is None:
            height = 1
        return height
        
    
        
        
        
        
        