# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        lres = [root.val]
        curr = root.left
        def helperleft(node, isleft):
            if node:
                if isleft or (node.left is None and node.right is None):
                    lres.append(node.val)
                if node.left:
                    helperleft(node.left, True and isleft )
                if node.right:
                    helperleft(node.right, (node.left is None) and isleft)
        rres = []
        def helperright(node, isright):
            if node:
                if isright or (node.left is None and node.right is None):
                    rres.append(node.val)
                if node.right:
                    helperright(node.right, True and isright)
                if node.left:
                    helperright(node.left, (node.right is None) and isright)
        helperleft(root.left, True)
        helperright(root.right, True)
        #print (lres)
        #print (rres)
        return lres+rres[::-1]