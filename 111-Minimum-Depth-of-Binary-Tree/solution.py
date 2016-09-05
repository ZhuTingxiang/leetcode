# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ########################## recursive solution ######################
        
        # if not root:
        #     return 0
        # if root.right is None:
        #     return self.minDepth(root.left)+1
        # if root.left is None:
        #     return self.minDepth(root.right)+1
        # else:
        #     return min(self.minDepth(root.left),self.minDepth(root.right))+1
        
        ######################### iterative solution ######################
        if not root:
            return 0
        level = []
        depth = 1
        if root.left is not None:
            level.append(root.left)
        if root.right is not None:
            level.append(root.right)
        while len(level) != 0:
            nextlevel = []
            depth += 1
            for i in level:
                if i.right is None and i.left is None:
                    return depth
                if i.right is None:
                    nextlevel.append(i.left)
                elif i.left is None:
                    nextlevel.append(i.right)
                else:
                    nextlevel.append(i.right)
                    nextlevel.append(i.left)
            level = nextlevel
        return depth
            
            
        
        