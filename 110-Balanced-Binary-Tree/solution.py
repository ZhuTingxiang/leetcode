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
        if root.right and not root.left :
            return self.findHeight(root.right)<=1
        if not root.right and root.left:
            return self.findHeight(root.left)<=1
        if root.left and root.right:
            if abs(self.findHeight(root.left) - self.findHeight(root.right)) > 1:
                return False
            if not self.isBalanced(root.left) or not self.isBalanced(root.right):
                return False
        return True

    def findHeight(self,root):
        if not root.left and root.right:
            height = self.findHeight(root.right) + 1
        elif not root.right and root.left:
            height = self.findHeight(root.left) + 1
        elif root.left and root.right:
            height = max(self.findHeight(root.left),self.findHeight(root.right)) + 1
        elif not root.right and not root.left:
            height = 1
        return height
        
    
        
        
        
        
        