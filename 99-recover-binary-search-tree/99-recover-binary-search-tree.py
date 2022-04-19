# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        greaternode = prev = smallernode = None
        def findgreater(root):
            nonlocal greaternode 
            nonlocal prev
            if root is None:
                return
            findgreater(root.left)
            if prev is not None:
                if prev.val > root.val:
                    if greaternode is None:
                        greaternode = prev
                        print (greaternode.val)
                    return
            prev = root
            findgreater(root.right)
        findgreater(root)
        prev = None
        def findsmaller(root):
            nonlocal smallernode 
            nonlocal prev
            if root is None:
                return
            findsmaller(root.right)
            if prev is not None:
                if prev.val < root.val:
                    if smallernode is None:
                        smallernode = prev
                        print (smallernode.val)
                    return
            prev = root
            findsmaller(root.left)
        prev = None
        findsmaller(root)
        
        #print(greaternode.val)
        #print (smallernode.val)
        smallernode.val, greaternode.val = greaternode.val, smallernode.val