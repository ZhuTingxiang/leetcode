# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head and head.next:
            slow = fast = temp = head
            fast = head.next
            while fast.next is not None:
                if slow == fast:
                    return True
                slow = slow.next
                fast = fast.next
        return False
        
        