# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lhead = head
        ispalin = True
        def helper(rhead):
            nonlocal lhead
            nonlocal ispalin
            if rhead is None or ispalin is False:
                return
            helper(rhead.next)
            ispalin &= (rhead.val == lhead.val)
            lhead = lhead.next
        helper(head)
        return ispalin