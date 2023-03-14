# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        def rec(node,total):
            
            if not node:
                return 0
            if not node.left and not  node.right:
                return total*10 + node.val
            
            return rec(node.left,total*10 + node.val) + rec(node.right , total * 10 + node.val)
        return rec(root,0)