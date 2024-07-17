# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        to_delete.add(0)
        self.ans = []
        new_root = TreeNode(0,root)
        def rec(node):
            if not node:
                return None
            
            node.left = rec(node.left)
            node.right = rec(node.right)
            
            if node.val in to_delete:
                if node.left:
                    self.ans.append(node.left)
                if node.right:
                    self.ans.append(node.right)
                return None
            
            return node
        
        rec(new_root)
        return self.ans