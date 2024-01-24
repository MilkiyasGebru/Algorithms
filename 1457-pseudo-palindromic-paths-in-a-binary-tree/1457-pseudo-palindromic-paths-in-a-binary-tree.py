# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def checkPalindrom(self,f):
        ones = 0
        for i in range(1,10):
            
            ones += f[i]%2
        
        return 1 if ones <= 1 else 0
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            
            if not node:
                return 0
            f[node.val] += 1
            if not node.left and not node.right:
                
                val = self.checkPalindrom(f)
                f[node.val] -= 1
                return val
            
            value = dfs(node.left) + dfs(node.right)
            f[node.val] -= 1
            
            return value
        f = defaultdict(int)
        return dfs(root)