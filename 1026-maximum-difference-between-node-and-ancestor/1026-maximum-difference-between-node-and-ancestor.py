# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,minn,maxx):
            
            if not node:
                return maxx - minn
            
            return max(dfs(node.left,min(node.val,minn),max(node.val,maxx)),
                      dfs(node.right,min(node.val,minn),max(node.val,maxx)))
        
        return dfs(root,root.val,root.val)