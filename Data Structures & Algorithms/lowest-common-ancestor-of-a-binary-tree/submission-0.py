# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        
        def lca(node):
            print(node.val) if node is not None else "\n"
            if node is None:
                return False
            
            if node == p or node == q:
                return True
            
            left = lca(node.left)
            right = lca(node.right)

            nonlocal res
            if left and right:
                res = node
            elif left and (node.left == p or node.right == q):
                res = node.left
            elif right and (node.right == p or node.right == q):
                res = node.right
            return left or right

        lca(root)
        return res
