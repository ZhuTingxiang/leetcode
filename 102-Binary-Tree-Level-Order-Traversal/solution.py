# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res,nextline,line = [],[],[]
        if root is None:
            return []
        line.append(root)
        res.append(line)
        while line:
            nextline = []
            for i in line:
                print "i",i
                if i.left:
                    nextline.append(i.left)
                if i.right:
                    nextline.append(i.right)
            if nextline != []:
                res.append(nextline)
            line = nextline
            
        return [[v.val for v in x] for x in res]
        
            
            
            
        
        