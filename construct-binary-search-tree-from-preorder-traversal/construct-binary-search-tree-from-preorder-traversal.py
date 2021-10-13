# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(arr):
            if len(arr) == 0:
                return None

            root = TreeNode(arr[0])
            rightindex = 1
            while rightindex<len(arr):
                if root.val < arr[rightindex]:
                    break
                rightindex += 1
            root.left = helper(arr[1:rightindex])
            root.right = helper(arr[rightindex:])
            return root
        return helper(preorder)