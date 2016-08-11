# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is not ListNode and l2 is not ListNode:
            return []
        l3 = temp = ListNode(0)
        
        while l1 is not ListNode and l2 is ListNode
            return l2
        while l1 is ListNode and l2 is not ListNode:
            return l1
        while l1.next is not None and l2.next is not None:
            print "both"
            if l1.val >l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        while l1.next is not None:
            print "l1 not None"
            l3.next = l1
            l1 = l1.next
            l3 = l3.next
        while l2.next is not None:
            print "l2 is not None"
            l3.next = l2
            l2 = l2.next
            l3 = l3.next
        return temp.next
            