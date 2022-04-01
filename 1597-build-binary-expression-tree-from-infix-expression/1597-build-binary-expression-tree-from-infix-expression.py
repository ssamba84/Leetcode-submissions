# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        def infix2postfix(s):
            operandstack = []
            res = ""
            for c in s:
                if c.isdigit():
                    res += c
                else:
                    if c == '(':
                        operandstack.append(c)
                    if c in '*/':
                        while operandstack and operandstack[-1] in '*/': 
                            res += operandstack.pop()
                        operandstack.append(c)
                    if c in '-+':
                        while operandstack and operandstack[-1] in '*/-+':
                            res += operandstack.pop()
                        operandstack.append(c)
                    if c == ')':
                        while operandstack[-1]!='(':
                            res += operandstack.pop()
                        operandstack.pop()
            while operandstack:
                res += operandstack.pop()
            return res
        postfix = infix2postfix(s)
        #print (postfix)
        
        stk = []
        for c in postfix:
            if c.isdigit():
                stk.append(TreeNode(val=c))
            else:
                rop = stk.pop()
                lop = stk.pop()
                stk.append(TreeNode(val=c, left = lop, right=rop))
        #print (stk)
        return stk[0]
        return None