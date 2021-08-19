# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return None
            root.left = helper(root.left)
            root.right = helper(root.right)
            if root.left:
                root.val += root.left.val
            if root.right:
                root.val += root.right.val
            root = TreeNode(root.val, root.left, root.right)
            return root
        helper(root)
        #print (root)
        ret = 0
        totalsum = root.val
        def helper2(root, par):
            if root is None:
                return
            nonlocal ret
            ret = max(ret, root.val*(totalsum-root.val))
            #print (par, root.val)
            helper2(root.left, root.val)
            helper2(root.right, root.val)
        helper2(root,0)
        return ret%(7+10**9)