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
            while head.next != None:
                head = head.next
                if head.val == val:
                    head.val = head.next.val
                    head.next = head.next.next
            return head
        else:
            return []