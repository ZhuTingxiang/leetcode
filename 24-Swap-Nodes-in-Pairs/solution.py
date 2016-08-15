# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            cur = temp = head
            n = head.next
            while cur.next is not None:
                cur.next = cur.next.next
                n.next = cur
                cur = cur.next
                n = cur.next
            return temp.next
        return 
                
                
            