# Last updated: 8/2/2025, 4:53:51 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = None
        while head:
            dummy = head
            head = head.next
            dummy.next = res
            res = dummy
        return res