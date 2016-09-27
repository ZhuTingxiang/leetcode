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
        elif len(self.leftLeavesList(root)) != 0:
            for i in self.leftLeavesList(root):
                sum += i.val
        return sum
        
            
    def leftLeavesList(self,root):
        list = []
        if not root:
            return list
        if root.left:
            if root.left.left is None and root.left.right is None:
                list.append(root.left)
            
        if len(self.leftLeavesList(root.right)) !=0:
            for i in self.leftLeavesList(root.right):
                list.append(i)
        if len(self.leftLeavesList(root.left)) !=0:
            for i in self.leftLeavesList(root.left):
                list.append(i)
        return list

            