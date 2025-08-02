# Last updated: 8/2/2025, 4:53:45 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = fast = head
        
        # finding the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reversing the linkedlist
        prev = None
        while slow:
            dummy = slow
            slow = slow.next
            dummy.next = prev
            prev = dummy
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
        
