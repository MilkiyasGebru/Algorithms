# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        visited=set()
        ans=[]
        
        def dfs(node,par=None):
            
            if not node:
                return
            
            node.par=par
            dfs(node.left,node)
            dfs(node.right,node)
            
        dfs(root)
        
        def find(node,l):
            
            if not node:
                return 
            
            visited.add(node)
            
            if l == k:
                ans.append(node.val)
                
            for n in [node.par,node.left,node.right]:
                
                if n and n not in visited:
                    
                    find(n,l+1)
                    
        find(target,0)
        
        return ans
            