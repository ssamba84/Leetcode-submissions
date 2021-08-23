# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def find(root, t, exclude):
            curr = root
            while curr:
                if curr.val == t and curr!=exclude:
                    return True
                if curr.val > t:
                    curr = curr.left
                else:
                    curr= curr.right
            return False
        def helper(curr, k):
            if curr is None:
                return False
            rem = k-curr.val
            return find(root, rem, curr) or helper(curr.left, k) or helper(curr.right, k)
            
        return helper(root, k)