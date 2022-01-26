# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        i = 0
        def inorder(tree, lst):
            if tree is None:
                return
            inorder(tree.left, lst)
            lst.append(tree.val)
            inorder(tree.right, lst)
        def helper(tree):
            nonlocal res
            nonlocal i
            if tree is None and i >= len(lst):
                return
            if tree is None:
                #res+=lst[i:]
                return
            #print (i, tree)
            helper(tree.left)
            if i >= len(lst) or tree.val <= lst[i]:
                res.append(tree.val)
            else:
                while i < len(lst) and lst[i] < tree.val:
                    res.append(lst[i])
                    i += 1
                res.append(tree.val)
            helper(tree.right)
                
        lst = []
        inorder(root1, lst)
        #print (lst)
        helper(root2)
        while i < len(lst):
            res.append(lst[i])
            i += 1
        return res
            