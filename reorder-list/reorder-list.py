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
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        rev = None
        while mid:
            nxt = mid.next
            mid.next = rev
            rev = mid
            mid = nxt
        rp = rev
        hp = head
        while rp:
            nxtr = rp.next
            nxth = hp.next
            hp.next = rp
            rp.next = nxth
            rp = nxtr
            hp = nxth
            