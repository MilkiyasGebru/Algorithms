# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def find(node):
            if not node:
                return None
            if node.val == val:
                return node
            if node.val > val:
                return find(node.left)
            if node.val < val:
                return find(node.right)
        return find(root)