# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = []
        def helper(root, path):
            if root is None:
                path.append("None")
                return
            path.append(str(root.val))
            helper(root.left, path)
            helper(root.right, path)
        helper(root, path)
        return ",".join(path)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        stk = []
        data = data.split(',')
        prev = -1
        root = None
        for node in data:
            if node != 'None':
                tnode = TreeNode(int(node))
                if root is None:
                    root = tnode
                if stk:
                    pnode = stk[-1]
                    if pnode.left is None and prev is not None:
                        pnode.left = tnode
                    else:
                        pnode.right = tnode
                        stk.pop()
                stk.append(tnode)
            else:
                node = None
                if prev is None:
                    stk.pop()
            prev = node
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))