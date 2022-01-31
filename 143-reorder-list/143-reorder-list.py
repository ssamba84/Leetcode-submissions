# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        prev = None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rem = slow.next
        slow.next = None
        right = None
        while rem:
            nxt = rem.next
            rem.next = right
            right = rem
            rem = nxt
        left = head
        while right:
            rnxt = right.next
            lnext = left.next
            left.next = right
            right.next = lnext
            left = lnext
            right = rnxt
        