# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <2:
            return head
        instart = inend = outstart = outend = None
        curr = head
        count = 0
        '''
        cn = 2
         c n
        [4,5]
        
        3 
        is
        ie
        2  1
        os oe
        '''
        while curr:
            nxt = curr.next
            curr.next = instart
            instart = curr
            count += 1
            
            if inend is None:
                inend = curr
            if count == k:
                if outstart is None:
                    outstart = instart
                    
                else:
                    outend.next = instart
                outend = inend
                instart = inend = None
                count = 0
            curr = nxt
        rev = None
        while instart:
            nxt = instart.next
            instart.next = rev
            rev = instart
            instart = nxt
        outend.next = inend
        return outstart