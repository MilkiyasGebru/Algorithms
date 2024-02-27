# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        def rec(node,max_,min_):
            if not node:
                return max_ - min_
            max_ = max(node.val,max_)
            min_ = min(node.val,min_)
            return max(rec(node.left,max_,min_),rec(node.right,max_,min_))
        
        return rec(root,-math.inf,math.inf)
            
            