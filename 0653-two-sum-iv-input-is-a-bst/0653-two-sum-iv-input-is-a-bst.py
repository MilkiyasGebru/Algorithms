# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        f =defaultdict(bool)
        def dfs(n):
            if not n:
                return 
            if f[k-n.val]:
                return True
            f[n.val]=True
            return dfs(n.left) or dfs(n.right)
        return dfs(root)