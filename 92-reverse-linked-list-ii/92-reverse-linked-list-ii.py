# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        newhead = ListNode(next = head)
        def advance(head, k):
            while k > 1:
                head = head.next
                k -= 1
            return (head, head.next)
        (lend, midhead) = advance(newhead, left)
        (midend, rhead) = advance(newhead, right+1)
        lend.next = None
        midend.next = None
        midrev = None
        oldmidhead = midhead
        midrev = None
        while midhead:
            nxt = midhead.next
            midhead.next = midrev
            midrev = midhead
            midhead = nxt
        lend.next = midrev
        oldmidhead.next = rhead
        return newhead.next