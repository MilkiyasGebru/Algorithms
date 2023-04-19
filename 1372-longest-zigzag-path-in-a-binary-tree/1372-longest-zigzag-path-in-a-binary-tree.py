# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.answer = 0
        def dfs(node):
            
            if not node:
                return 0,0
            
            left_values = dfs(node.left)
            right_values = dfs(node.right)
            self.answer = max(left_values[1],right_values[0],self.answer)
            return left_values[1] + 1, right_values[0] + 1 
        
        dfs(root)
        return self.answer
            