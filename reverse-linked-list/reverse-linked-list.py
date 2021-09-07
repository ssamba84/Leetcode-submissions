# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rethead = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = rethead
            rethead = curr
            curr = nxt
        return rethead