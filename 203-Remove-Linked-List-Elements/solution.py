# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head:
            if head.next == None:
                return head
            else:
                n = head
                while n.next != None:
                    if n.val == val:
                        n.val = n.next.val
                        n.next = n.next.next
                    n = n.next
                        
                return head
        else:
            return []