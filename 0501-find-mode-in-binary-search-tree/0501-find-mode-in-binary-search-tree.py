# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        f = defaultdict(int)
        maxx = 0
        def dfs(node):
            
            if not node:
                return 
            
            f[node.val] += 1
            nonlocal maxx
            maxx = max(maxx,f[node.val])
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        answer = []
        for key in f.keys():
            if f[key] == maxx:
                answer.append(key)
        
        return answer