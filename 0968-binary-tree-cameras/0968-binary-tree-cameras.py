# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(None)
        def dp(node,viewed,camera):
            
            if not node:
                
                return 0 if viewed else float("inf")
            
            
            must_place = 1 + dp(node.left,True,True) + dp(node.right,True,True)
            left_viewed = dp(node.left,True,False)
            right_viewed = dp(node.right,True,False)
            left_place = dp(node.left,False,False)
            right_place = dp(node.right,False,False)
            
            if camera:
                
                return min( must_place, left_viewed + right_viewed )
            
            if viewed:
                
                return min(must_place, left_place + right_viewed, right_place + left_viewed)
            
            return must_place
            
        
        
        return dp(root,True,False)
            
            
            
            
            