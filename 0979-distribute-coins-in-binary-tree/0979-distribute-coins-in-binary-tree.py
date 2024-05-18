# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def dfs(node):
            
            if not node:
                return 0
            
            
            left_value = dfs(node.left)
            right_value = dfs(node.right)
            self.ans += abs(left_value) + abs(right_value)
            return left_value + right_value + node.val - 1
        
        dfs(root)
        return self.ans