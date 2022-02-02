# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        # 1 2 3 4
        # 
        # 2 1   4 3
        # oh ot ih it
        newhead = ListNode(next = head)
        currlen = 0
        ohead = otail = ihead = itail = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = ihead
            ihead = curr
            if itail is None:
                itail = curr
            currlen += 1
            if currlen == k:
                if ohead is None:
                    ohead = ihead
                    
                else:
                    otail.next = ihead
                otail = itail
                itail = ihead = None
                currlen = 0
            curr = nxt
        revihead = None
        while ihead:
            nxt = ihead.next
            ihead.next = revihead
            revihead = ihead
            ihead = nxt
        otail.next = revihead
        return ohead