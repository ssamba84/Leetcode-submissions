# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        while k>1:
            curr = curr.next
            k -= 1
        
        kahead = curr
        kbehind = head
        while curr.next:
            curr = curr.next
            kbehind = kbehind.next
        #print (kahead.val, kbehind.val)
        kahead.val,kbehind.val = kbehind.val, kahead.val
        return head