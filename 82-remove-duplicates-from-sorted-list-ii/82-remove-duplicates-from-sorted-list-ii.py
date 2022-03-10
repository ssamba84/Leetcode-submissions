# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
       [1,2,3,3,4,4,5]
    nh  
           p         c
    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newhead = prev = ListNode(next = head)
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                prev.next = None
                ignoreval = curr.val
                while curr and curr.val == ignoreval:
                    curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        if curr:
            prev.next= curr
        return newhead.next