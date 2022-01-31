# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fhead = head
        ans = True
        def helper(head):
            nonlocal fhead
            nonlocal ans
            if head is None:
                return
            helper(head.next)
            ans &= (head.val == fhead.val)
            fhead = fhead.next
        helper(head)
        return ans