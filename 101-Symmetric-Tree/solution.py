# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    #recursively solution
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root:
    #         return True
    #     return self.isMirror(root.left,root.right)
    
    # def isMirror(self,left,right):
    #     if not left and not right:
    #         return True
    #     if not left or not right:
    #         return False
    #     if left.val == right.val:
    #         if self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left):
    #             return True
    #     return False
        
    #iteratively solution:

    def isSymmetric(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        stack1 = [root.left]
        stack2 = [root.right]
        while len(stack1) > 0 and len(stack2) > 0:
            left = stack1.pop()
            right = stack2.pop()
            if left.val != right.val:
                return False
            if left.left is not None and right.right is None:
                return False
            if left.left is None and right.right is not None:
                return False
            if left.right is not None and right.left is None:
                return False
            if left.right is None and right.left is not None:
                return False
            if left.left and right.right:
                stack1.append(left.left)
                stack2.append(right.right)
            if left.right and right.left:
                stack1.append(left.right)
                stack2.append(right.left)
        return True
                    
                    
                
                    
                
                
            
                
        
        
            
        
        