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
        old_head = pre = ListNode(0)
        old_head.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return old_head.next
                
        