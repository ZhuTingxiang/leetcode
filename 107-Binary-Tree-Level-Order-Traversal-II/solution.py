# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = []
        level.insert(0,root)
        while len(level) >= 1:
            tmp = [i.val for i in level]
            result.insert(0,tmp)
            nextlevel = []
            for i in level:
                if i.right is not None:
                    nextlevel.insert(0,i.right)
                if i.left is not None:
                    nextlevel.insert(0,i.left)
            level = nextlevel
        return result
                
                
            
        
        