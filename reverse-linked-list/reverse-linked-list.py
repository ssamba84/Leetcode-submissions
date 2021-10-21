# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = None
        while head:
            nxt = head.next
            head.next = ret
            ret = head
            head = nxt
        return ret