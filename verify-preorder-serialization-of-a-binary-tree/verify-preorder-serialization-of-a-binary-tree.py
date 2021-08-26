class TreeNode(object):
    def __init__(self, val, left=-1, right=-1):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:

    def isValidSerialization(self, preorder: str) -> bool:
 
        if len(preorder) == 1 and preorder[0] == '#':
            return True
        if preorder[0] == '#':
            return False
        preorder = preorder.split(',')
        stk = [TreeNode(preorder[0])]
        for i,c in enumerate(preorder[1:]):
            if len(stk) == 0:
                return False
            else:   
                n = stk[-1]
                if n.left == -1:
                    if c == '#':
                        stk[-1].left = None
                    else:
                        n = TreeNode(c)
                        stk[-1].left = n
                        stk.append(n)
                else:
                    if c == '#':
                        n = stk.pop()
                        while len(stk) > 0 and stk[-1].right != -1 and stk[-1].right.val == n.val:
                            n = stk.pop()
                    else:
                        stk[-1].right = TreeNode(c)
                        stk.append(stk[-1].right)
        return len(stk) == 0