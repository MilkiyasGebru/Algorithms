# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        self.answer= "z"*8500
        
        def rec(node,q):
            
            if not node:
                return 
            
            q.appendleft(chr(ord("a") + node.val))
            
            if not node.left and not node.right :
                
                self.answer = min(self.answer, "".join(q))
                
            rec(node.left,q)
            rec(node.right,q)
            
            q.popleft()
            
        
        rec(root,deque())
        return self.answer