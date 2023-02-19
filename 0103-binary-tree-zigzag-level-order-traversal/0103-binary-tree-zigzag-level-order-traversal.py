# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        
        def dfs(node,height):
            
            if not node:
                return 
            if len(q) < height + 1:
                q.append(deque())
                
            if height % 2 == 0:
                
                q[height].append(node.val)
            else:
                q[height].appendleft(node.val)
            dfs(node.left,height+1)
            dfs(node.right,height+1)
        
        dfs(root,0)
        return q