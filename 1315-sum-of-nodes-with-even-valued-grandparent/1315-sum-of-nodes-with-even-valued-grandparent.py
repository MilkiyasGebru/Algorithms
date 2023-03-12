# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.total = 0
        def evenGrandparent(node,parent,grandParent):
            
            if not node:
                return 
            
            if grandParent and grandParent.val%2 == 0:
                self.total += node.val
            
            evenGrandparent(node.left,node,parent)
            evenGrandparent(node.right,node,parent)
        
        evenGrandparent(root,None,None)
        return self.total