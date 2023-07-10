# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if root == None:
            # return 0
        
        def depth(root):
            if root == None:
                return 0
            
            if  None in [root.left,root.right]:
                return max(1+depth(root.left),1+depth(root.right)) 
            
            else:
                return min(1+depth(root.left),1+depth(root.right))
            
        return depth(root)    