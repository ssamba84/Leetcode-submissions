# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oh = ot = None
        curr = head
        '''
          n
        2 3 4 5
        p2
        
        2 1
        p2 p1
        '''
        
        if curr is None or curr.next is None:
            return head
        while curr and curr.next:
            p1 = curr
            p2 = curr.next
            nxt = p2.next
            curr = nxt
            p1.next = None
            p2.next = p1
            if oh is None:
                oh = p2
            else:
                ot.next = p2
            ot = p1
        if ot:
            ot.next = curr
        return oh