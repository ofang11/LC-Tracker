# Last updated: 8/2/2025, 4:53:59 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        # getting middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        # reversing
        second = slow.next
        slow.next = prev = None
        while second:
            dummy = second
            second = second.next
            dummy.next = prev
            prev = dummy

        first, second = head, prev
        while second:
            d1, d2 = first.next, second.next
            first.next = second
            second.next = d1
            first = d1
            second = d2



        
        